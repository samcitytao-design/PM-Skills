"""Output-contract regression cases, independent of any product domain."""
import importlib.util
from pathlib import Path
import re
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'scripts' / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
r = load('renderer_five', 'build_prd_markdown.py')
v = load('validator_five', 'validate_markdown.py')

class FiveSectionTests(unittest.TestCase):
    def model(self):
        return {'document_profile':'review_table', 'delivery':{
            'language':'zh-CN','outline_profile':'five_section','logic_placement':'row_complete',
            'image_mode':'external','output_target':'prd.md','update_mode':'new_file','acceptance_detail':'none'},
            'meta':{'title':'预约管理'}, 'overview':{'background':['预约状态需要可见。'],'goals':['让用户完成改期。']},
            'sources':['Approved booking screens'], 'decisions':[], 'blocking_decisions':[],
            'configuration_summary':['由服务端控制可预约时段。'],
            'tracking':[{'event':'预约提交','trigger':'用户确认改期','parameters':['预约标识','结果']}],
            'test_points':[{'id':'P01','name':'预约详情','variants':[
                {'id':'A','images':['https://example.org/a.png'], 'applicability':['预约有效时展示。'],
                 'display':['展示已选时间。'],'interactions':['点击改期→打开时间选择页。']},
                {'id':'B','images':['https://example.org/b.png'], 'applicability':['预约已取消时展示。'],
                 'display':['展示取消结果。'],'interactions':['点击返回→预约列表。']}
            ]}]}
    def validate(self, text, **kwargs):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'prd.md'; p.write_text(text)
            return v.validate_markdown(p, image_mode='external', **kwargs)
    def test_exact_outline_and_table_headers(self):
        text=r.render_prd(self.model())
        self.assertEqual(re.findall(r'^## (.+)$',text,re.M),['1. 需求背景','2. 需求目标','3. 需求详述','4. 云控项','5. 埋点'])
        self.assertEqual(text.count('| 原型图 | 具体需求逻辑 |'),1)
        self.assertIn('**交互逻辑**<br>1.',text)
        self.assertNotIn('已确认决策记录',text)
        self.assertEqual(self.validate(text),[])
    def test_extra_module_is_rejected(self):
        text=r.render_prd(self.model())+'\n## 6. 决策记录\n无\n'
        self.assertTrue(any('five-section' in i for i in self.validate(text,outline='five-section')))
    def test_prose_replacement_is_rejected(self):
        text=r.render_prd(self.model())
        text=re.sub(r'\| 原型图.*?(?=## 4\.)','说明文字。\n\n',text,flags=re.S)
        self.assertTrue(any('table' in i for i in self.validate(text,outline='five-section')))
    def test_unstructured_right_cell_is_rejected(self):
        text=r.render_prd(self.model())
        text=re.sub(r'\*\*[^*]+\*\*','',text)
        self.assertTrue(any('numbered' in i for i in self.validate(text,outline='five-section')))
    def test_wrong_columns_are_rejected(self):
        text=r.render_prd(self.model()).replace('| 原型图 | 具体需求逻辑 |','| 图片 | 长篇说明 |')
        self.assertTrue(any('原型图' in i for i in self.validate(text,outline='five-section')))
    def test_structural_model_conflict_fails_before_render(self):
        model=self.model(); model['delivery']['logic_placement']='shared_below'
        with self.assertRaisesRegex(ValueError,'row_complete'): r.render_prd(model)
    def test_does_not_drop_unplaced_rules(self):
        model=self.model(); model['rules']=['Critical cancellation rule']
        with self.assertRaisesRegex(ValueError,'rules'): r.render_prd(model)
    def test_blocks_unresolved_decisions(self):
        model=self.model(); model['blocking_decisions']=['Cancellation ownership unknown']
        with self.assertRaisesRegex(ValueError,'unresolved'): r.render_prd(model)
    def test_image_portability_remains_enforced(self):
        model=self.model(); model['test_points'][0]['variants'][0]['images']=['/tmp/a.png']
        with self.assertRaisesRegex(ValueError,'absolute'): r.render_prd(model)
    def test_module_purpose_stays_in_table(self):
        model=self.model(); model['test_points'][0]['purpose']='查看预约状态。'
        text=r.render_prd(model)
        self.assertEqual(self.validate(text),[])
        self.assertTrue(all(line.startswith('|') for line in text.splitlines() if '查看预约状态。' in line))
    def test_no_controls_or_tracking_does_not_invent_them(self):
        model=self.model(); model['configuration_summary']=['本期不涉及远程配置。']
        model['tracking']=['本期不新增埋点。']
        text=r.render_prd(model)
        self.assertEqual(self.validate(text),[])
        self.assertIn('本期不涉及远程配置。',text)
        self.assertNotIn('广告',text)
    def test_missing_image_still_fails(self):
        text=r.render_prd(self.model()).replace('![A prototype](https://example.org/a.png)','无图')
        self.assertTrue(any('no prototype image' in i for i in self.validate(text)))

if __name__ == '__main__': unittest.main()
