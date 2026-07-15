# Conditional Domain Modules

Activate modules only from observable signals. Record `Signal -> Module -> Checks`. A keyword alone may be insufficient when it appears in placeholder content; use surrounding UI and user context.

| Module | Observable signals | Additional checks |
|---|---|---|
| Transactions and billing | price, cart, invoice, purchase, subscription, refund, payment instrument | price ownership, currency/tax, authorization, payment states, retries, refunds, reconciliation |
| Content and media | publish, upload, feed, playback, episode, draft, media controls | lifecycle, rights, moderation, processing, quality, playback failure, removal |
| Advertising, entitlements, incentives | ad placement, reward, points, benefits, eligibility, campaign | qualification, caps, frequency, attribution, issuance, expiry, abuse prevention |
| Social and user-generated content | follow, comment, reaction, message, report, audience | visibility, relationship states, moderation, blocking, counts, notifications |
| Enterprise workflow | organization, team, approver, queue, role, audit | role matrix, assignment, self-action, delegation, escalation, concurrency, audit |
| AI-assisted feature | prompt, generation, model output, confidence, regenerate | input limits, safety, provenance, latency, failure, review, correction, fallback |
| Location, hardware, or device | map, GPS, camera, sensor, Bluetooth, device status | permission, precision, disconnect, background behavior, unavailable hardware |
| Multi-tenant or international | tenant, workspace, region, locale, timezone, multiple languages | isolation, inheritance, formats, translation length, regional variation |
| Regulated or high-impact | diagnosis, credit, legal decision, identity verification, regulated record | consent, disclosure, recordkeeping, human review, access, retention, jurisdiction |

## Negative-Trigger Rules

- No transaction signal: do not ask about payment, refunds, tax, or currency.
- No identity or role signal: do not invent login, accounts, permissions, or sessions.
- No remote-system signal: do not invent APIs, backend storage, synchronization, or network errors.
- No analytics or success-metric request: treat event tracking as optional, not a mandatory implementation.
- No platform evidence: do not choose Web, mobile, desktop, or responsive breakpoints.
- No implementation request: describe product behavior, not database tables, endpoint shapes, algorithms, or framework choices.

## Multiple Modules

Activate all evidenced modules, but keep their questions separate. Deduplicate cross-cutting concerns through the universal framework; for example, timeout belongs to reliability, while the transaction module adds the transaction-specific consequence.
