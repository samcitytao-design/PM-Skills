#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""通用漏斗图渲染器（funnel-chart skill 的核心）。

输入：一个 JSON 配置（--config），或直接命令行给层名与人数
      python3 render_funnel.py --config funnel.json
      python3 render_funnel.py --title "XXX漏斗" --stage "A" --val 100 --stage "B" --val 60 --out out.png

配置里只放「层名 + 人数」即可：所有渗透率、累计、漏损、端到端转化率都由脚本现算，
不写死百分比。输出与脚本/配置同目录时用相对路径，整个文件夹可整体搬移。

JSON 结构见 references/config-schema.md。
"""
import argparse
import json
import os
import sys

from PIL import Image, ImageDraw, ImageFont

# ---------------------------------------------------------------- 默认配置
DEFAULTS = {
    "title": "",
    "subtitle": "口径为逐级渗透：每层分母是上一层人数；端到端渗透率 = 各层渗透率相乘。",
    "badge": "",
    "badge_prefix": "数据日期  ",
    "out": "funnel.png",
    "width": 1772,
    "kpi_base_label": "分析基数",
    "cum_label_prefix": "对 DAU 累计",
    "kpi_base_sub": "",
    "foot_source_prefix": "数据来源：",
    "foot_source_suffix": "；各层渗透率 = 该层人数 ÷ 上一层人数，由人数现算，未写死。",
    "foot_note": "",
    "stages": [],          # [{"name": str, "count": number, "color": [r,g,b]?, "note": str?}]
    "colors": [
        [247, 150, 70], [243, 124, 86], [237, 96, 110],
        [214, 82, 148], [166, 104, 186], [108, 128, 196],
        [126, 146, 178], [150, 160, 176],
    ],
}

# ---------------------------------------------------------------- 字体
PING = "/System/Library/Fonts/PingFang.ttc"
CJK_CANDIDATES = [
    PING,
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
    "/System/Library/Fonts/Songti.ttc",
]
LATIN_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
LATIN_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"

INK = (34, 44, 66)
GREY = (140, 150, 168)
GREY_SOFT = (162, 172, 190)
RED = (219, 68, 72)
LINE = (233, 238, 246)


def load_fonts(scale=1.0):
    def pick(cands, size):
        for p in cands:
            if os.path.exists(p):
                try:
                    return ImageFont.truetype(p, int(size * scale))
                except Exception:
                    pass
        return ImageFont.load_default()

    cjk = CJK_CANDIDATES
    return {
        "title": pick(cjk, 44),
        "sub": pick(cjk, 23),
        "kpi_l": pick(cjk, 19),
        "kpi_v": pick(cjk, 30),
        "name": pick(cjk, 28),
        "nsub": pick(cjk, 19),
        "val": pick(cjk, 36),
        "incum": pick(cjk, 20),
        "rate": pick([LATIN_BOLD] + cjk, 34),
        "rsub": pick(cjk, 20),
        "tag": pick(cjk, 18),
        "badge": pick(cjk, 21),
        "foot": pick(cjk, 17),
    }


def fmt_pct(x, nd=1):
    return f"{x:.{nd}f}%"


def build(cfg):
    stages = cfg["stages"]
    n = len(stages)
    if n < 2:
        raise SystemExit("至少需要 2 层（起点 + 终点）")
    for s in stages:
        if "name" not in s or "count" not in s:
            raise SystemExit("每层必须包含 name 与 count")
    counts = [float(s["count"]) for s in stages]
    for i in range(1, n):
        if counts[i] > counts[i - 1]:
            raise SystemExit(f"第 {i+1} 层人数大于上一层（漏斗应逐层递减）：{counts}")
    rates = [None] + [counts[i] / counts[i - 1] for i in range(1, n)]
    e2e = counts[-1] / counts[0]
    maxloss_i = max(range(1, n), key=lambda i: counts[i - 1] - counts[i])
    last_i = n - 1
    # 颜色：按层数在渐变色带上等距取样，保证首层最暖、末层最冷（4 层和 8 层观感一致）
    def sample_color(t):
        ramp = cfg["colors"]
        if len(ramp) == 1:
            return tuple(ramp[0])
        pos = t * (len(ramp) - 1)
        i0 = min(int(pos), len(ramp) - 2)
        f = pos - i0
        return tuple(int(ramp[i0][k] + (ramp[i0 + 1][k] - ramp[i0][k]) * f) for k in range(3))

    for i, s in enumerate(stages):
        s["_color"] = tuple(s.get("color") or sample_color(i / max(n - 1, 1)))

    W = int(cfg["width"])
    MG = 64
    BAR_X, BAR_R = 380, 1246
    BAR_W = BAR_R - BAR_X
    COL_X = 1300
    MAXV = counts[0]

    F = load_fonts()
    img = Image.new("RGB", (10, 10), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # ---- 画布高度：标题区 + KPI + 漏斗 + 行距 + 页脚（随层数自适应）
    TOP = 366
    BAR_H, GAP = 84, 42
    def _wrap(text, font, maxw):
        lines, cur = [], ""
        for ch in str(text):
            if ch == "\n":
                lines.append(cur); cur = ""; continue
            if d.textlength(cur + ch, font=font) <= maxw:
                cur += ch
            else:
                lines.append(cur); cur = ch
        if cur:
            lines.append(cur)
        return lines

    seq_txt = " → ".join(f"{int(c):,}" for c in counts)
    src_line = (cfg["foot_source_prefix"] or "") + str(cfg.get("foot_source_text") or seq_txt) + cfg["foot_source_suffix"]
    note_txt = cfg.get("foot_note") or "说明：漏斗宽度按人数开方压缩，仅影响观感、不影响数值；改人数请改配置后重跑本脚本。"
    foot_lines = len(_wrap(src_line, F["foot"], W - 2 * MG)) + len(_wrap(note_txt, F["foot"], W - 2 * MG))
    H = TOP + n * BAR_H + (n - 1) * GAP + 40 + 26 * foot_lines + 44

    img = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # ---- 标题
    title = cfg["title"] or "转化漏斗"
    d.text((MG, 46), title, font=F["title"], fill=INK)
    if cfg["subtitle"]:
        d.text((MG, 108), cfg["subtitle"], font=F["sub"], fill=GREY)
    d.line([(MG, 152), (W - MG, 152)], fill=LINE, width=2)

    # ---- 数据日期角标
    if cfg["badge"]:
        badge = cfg["badge_prefix"] + str(cfg["badge"])
        bw = d.textlength(badge, font=F["badge"]) + 44
        bx1, by0, by1 = W - MG, 54, 96
        bx0 = bx1 - bw
        d.rounded_rectangle([bx0, by0, bx1, by1], radius=(by1 - by0) / 2,
                            fill=(255, 241, 241), outline=(240, 178, 178), width=2)
        d.text(((bx0 + bx1) / 2, (by0 + by1) / 2 + 1), badge, font=F["badge"], fill=RED, anchor="mm")

    # ---- KPI 卡片
    cards = [
        ("端到端渗透率", fmt_pct(e2e * 100, 2),
         cfg.get("kpi_e2e_sub") or f"{stages[0]['name'].replace('渗透','')} → {stages[-1]['name'].replace('渗透','')}", RED),
        (cfg["kpi_base_label"], f"{int(counts[0]):,} 人", cfg.get("kpi_base_sub") or stages[0]["name"], INK),
        (stages[-1]["name"].replace("渗透", "") + "人数", f"{int(counts[-1]):,} 人",
         f"{stages[-2]['name']} {int(counts[-2]):,} 人", INK),
        ("最大单环节漏损", f"{stages[maxloss_i - 1]['name'].replace('渗透','')} → {stages[maxloss_i]['name'].replace('渗透','')}",
         f"漏损 {int(counts[maxloss_i - 1] - counts[maxloss_i]):,} 人 · 渗透率 {fmt_pct(rates[maxloss_i] * 100)}", RED),
    ]
    cy0, cy1, cgap = 176, 292, 26
    cw = (W - 2 * MG - 3 * cgap) / 4
    for i, (label, value, sub, col) in enumerate(cards):
        x0 = MG + i * (cw + cgap)
        d.rounded_rectangle([x0, cy0, x0 + cw, cy1], radius=16, fill=(249, 251, 254),
                            outline=(231, 237, 246), width=2)
        d.text((x0 + 26, cy0 + 22), label, font=F["kpi_l"], fill=GREY)
        vf = F["kpi_v"]
        size = 30
        while d.textlength(value, font=vf) > cw - 52 and size > 18:
            size -= 2
            vf = ImageFont.truetype(PING, size) if os.path.exists(PING) else vf
        d.text((x0 + 26, cy0 + 46), value, font=vf, fill=col)
        sf = F["kpi_l"]
        ssize = 19
        while d.textlength(sub, font=sf) > cw - 52 and ssize > 14:
            ssize -= 1
            sf = ImageFont.truetype(PING, ssize) if os.path.exists(PING) else sf
        d.text((x0 + 26, cy0 + 84), sub, font=sf, fill=GREY_SOFT)

    # ---- 列标题
    hy = TOP - 34
    d.text((MG, hy), "环节", font=F["kpi_l"], fill=GREY, anchor="ls")
    d.text((BAR_X, hy), "漏斗宽度 = 人数（开方压缩，便于看清尾部）", font=F["kpi_l"], fill=GREY, anchor="ls")
    d.text((COL_X, hy), "环节渗透率（相对上一层） / 累计与漏损", font=F["kpi_l"], fill=GREY, anchor="ls")

    # ---- 漏斗
    for i, s in enumerate(stages):
        val, rate, color = counts[i], rates[i], s["_color"]
        y0 = TOP + i * (BAR_H + GAP)
        y1 = y0 + BAR_H
        cy = (y0 + y1) / 2
        inset = 0 if i == 0 else (1 - (val / MAXV) ** 0.5) * (BAR_W / 2 - 6)
        x0, x1 = BAR_X + inset, BAR_R - inset

        if i > 0:
            pv = counts[i - 1]
            pinset = 0 if i == 1 else (1 - (pv / MAXV) ** 0.5) * (BAR_W / 2 - 6)
            py1 = y0 - GAP
            d.polygon([(BAR_X + pinset, py1), (BAR_R - pinset, py1), (x1, y0), (x0, y0)],
                      fill=tuple(int(c + (255 - c) * 0.80) for c in color))

        d.rounded_rectangle([x0, y0, x1, y1], radius=12, fill=color)
        d.text((x0 + 30, cy), f"{int(val):,}", font=F["val"], fill=(255, 255, 255), anchor="lm")
        d.text((x0 + 30 + d.textlength(f"{int(val):,}", font=F["val"]) + 12, cy + 2), "人",
               font=F["incum"], fill=(255, 242, 242), anchor="lm")

        # 左侧环节名
        d.text((MG, cy - 13), s["name"], font=F["name"], fill=INK, anchor="lm")
        if i == maxloss_i:
            tw = d.textlength(s["name"], font=F["name"])
            d.rounded_rectangle([MG + tw + 16, cy - 28, MG + tw + 16 + 104, cy - 6], radius=13, fill=RED)
            d.text((MG + tw + 68, cy - 17), "最大漏损", font=F["tag"], fill=(255, 255, 255), anchor="mm")
        d.text((MG, cy + 17), (cfg["kpi_base_sub"] or "分析基数") if rate is None else f"{int(val):,} 人",
               font=F["nsub"], fill=GREY, anchor="lm")

        # 右侧数据列
        if rate is None:
            d.text((COL_X, cy), "起点 · 100%", font=F["rsub"], fill=GREY, anchor="lm")
        else:
            lost = counts[i - 1] - val
            drop = lost / counts[i - 1] * 100
            col = RED if drop > 60 else INK
            last = i == last_i
            dy = 10 if (last and s.get("note")) else 0
            d.text((COL_X, cy - 20 - dy), fmt_pct(rate * 100), font=F["rate"], fill=col, anchor="lm")
            d.text((COL_X + d.textlength(fmt_pct(rate * 100), font=F["rate"]) + 16, cy - 14 - dy),
                   f"{cfg['cum_label_prefix']} {fmt_pct(val / MAXV * 100, 2)}",
                   font=F["rsub"], fill=GREY, anchor="lm")
            d.text((COL_X, cy + 18 - dy), f"漏损 {int(lost):,} 人 · {fmt_pct(drop)}",
                   font=F["rsub"], fill=GREY, anchor="lm")
            if last and s.get("note"):
                d.text((COL_X, cy + 44 - dy), s["note"], font=F["rsub"], fill=RED, anchor="lm")

    # ---- 页脚
    d.line([(MG, H - 96), (W - MG, H - 96)], fill=LINE, width=2)
    seq = " → ".join(f"{int(c):,}" for c in counts)
    fy = H - 26 * foot_lines - 20
    for ln in _wrap(src_line, F["foot"], W - 2 * MG) + _wrap(note_txt, F["foot"], W - 2 * MG):
        d.text((MG, fy), ln, font=F["foot"], fill=(152, 162, 180))
        fy += 26

    return img



def main():
    ap = argparse.ArgumentParser(description="通用漏斗图渲染器")
    ap.add_argument("--config", help="JSON 配置文件路径")
    ap.add_argument("--out", help="输出 PNG 路径（覆盖配置里的 out）")
    ap.add_argument("--title", help="标题（与 --stage/--val 连用时无需 config）")
    ap.add_argument("--badge", help="数据日期角标内容，例如 2026-09-22")
    ap.add_argument("--stage", action="append", default=[], help="层名，可重复")
    ap.add_argument("--val", action="append", type=float, default=[], help="该层人数，可重复")
    args = ap.parse_args()

    cfg = dict(DEFAULTS)
    if args.config:
        with open(args.config, encoding="utf-8") as f:
            user = json.load(f)
        cfg.update(user)
    if args.stage:
        if len(args.stage) != len(args.val):
            raise SystemExit("--stage 与 --val 数量必须一致")
        cfg["stages"] = [{"name": nm, "count": v} for nm, v in zip(args.stage, args.val)]
    if args.title:
        cfg["title"] = args.title
    if args.badge:
        cfg["badge"] = args.badge
    if args.out:
        cfg["out"] = args.out
    if not cfg["stages"]:
        raise SystemExit("没有层数据：请用 --config 或 --stage/--val 提供")

    img = build(cfg)
    out = cfg["out"]
    if not os.path.isabs(out):
        base = os.path.dirname(os.path.abspath(args.config)) if args.config else os.getcwd()
        out = os.path.join(base, out)
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    img.save(out, "PNG", optimize=True)
    counts = [float(s["count"]) for s in cfg["stages"]]
    rates = [None] + [counts[i] / counts[i - 1] for i in range(1, len(counts))]
    print(f"saved {out} {img.size}")
    for (st, r) in zip(cfg["stages"], rates):
        print(f"  {st['name']}: {int(st['count']):,} 人" + ("" if r is None else f"  环节渗透率 {r*100:.1f}%"))
    print("end-to-end %.2f%%" % (counts[-1] / counts[0] * 100))


if __name__ == "__main__":
    main()
