# Requirements and acceptance ownership

[Roadmap](overview.md) · [Specification](../../ZENDOOH.md)

This matrix prevents requirements from disappearing between phases. Detailed scenarios
live in the owning phase. **All implementation evidence is pending.** Replace “Pending”
with evidence links and implementation revisions as work completes; a plan is not
evidence. Rows may close only after their prerequisite gates and applicable human
approval.

## Beta requirements

| Requirement                                                               | Owner / gate                                                        | Required evidence                                                               | Status   |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------- | -------- |
| Reproducible Android delivery and truthful task coverage                  | [00](00-foundation.md), G00                                         | Pinned-tool checks, APK and Android execution procedure                         | Complete |
| Replaceable shared/platform boundaries and encrypted SQLite compatibility | [01](01-persistence.md), G01                                        | Android encryption integration, desktop/shared tests and decision record        | Pending  |
| Exact money, explicit currency and stable identities                      | [01](01-persistence.md), G01; [02](02-manual-ledger.md), G02        | Boundary/overflow/rounding and persisted identity tests                         | Pending  |
| Manual/cash entries, transfers and fees                                   | [02](02-manual-ledger.md), G02                                      | End-to-end totals, repeat/save and failure tests                                | Pending  |
| Draft Save/Discard, revisions, logical deletion and restore               | [02](02-manual-ledger.md), G02                                      | UI navigation and saved-history tests                                           | Pending  |
| First useful phone application                                            | [02](02-manual-ledger.md), H01                                      | Redmi fictional-data checklist and user acceptance                              | Pending  |
| Provenance, independent uncertainty and source availability               | [02](02-manual-ledger.md), G02; [05](05-acquisition-review.md), G05 | No false verification; missing source remains neutral                           | Pending  |
| Privacy, portable backup/replacement restore and upgrades                 | [03](03-protection-recovery.md), G03                                | Fresh-install recovery, malformed input, interruption and migration tests       | Pending  |
| Permission to use real data in verified workflows                         | [03](03-protection-recovery.md), H02                                | H01, G03 and explicit user approval                                             | Pending  |
| Personal/business allocations and relationships                           | [04](04-profiles-relationships.md), G04                             | Mixed purchase, partial refund, grouped totals and custom-label invariance      | Pending  |
| Controlled input and permission-denied fallback                           | [05](05-acquisition-review.md), G05                                 | Manual/import journey without SMS access                                        | Pending  |
| Historical/incremental scans, repeat imports and interruption             | [05](05-acquisition-review.md), G05                                 | Adapter fixtures, checkpoint/cancellation tests and Android evidence            | Pending  |
| Dual-SIM provenance and mapping ambiguity                                 | [05](05-acquisition-review.md), G05                                 | Reference-device script plus synthetic missing/reused subscription tests        | Pending  |
| Seven-day bounded teaching cache                                          | [05](05-acquisition-review.md), G05                                 | Completion/expiry/manual-clear tests and backup exclusion inspection            | Pending  |
| Learnable formats, independent evaluation and rollback                    | [06](06-adaptive-learning.md), G06                                  | Held-out datasets, recorded promotion policy and regression/rollback tests      | Pending  |
| Correction-preserving reparse and local learning forget                   | [06](06-adaptive-learning.md), G06                                  | Stable IDs, explicit correction precedence and privacy tests                    | Pending  |
| M-Pesa and Airtel Money coverage                                          | [07](07-provider-coverage.md), G07                                  | Per-family coverage matrix, positive/negative and multi-account journeys        | Pending  |
| Fuliza and M-Shwari financial semantics                                   | [07](07-provider-coverage.md), G07                                  | Borrow/principal/fee/savings fixtures including incomplete evidence             | Pending  |
| Reconciliation and incomplete balances                                    | [07](07-provider-coverage.md), G07                                  | Expected/observed balances, late evidence and gap explanations                  | Pending  |
| Debt forecasts and versioned personal defaults                            | [08](08-debt-forecasts.md), G08                                     | Independent fictional calculations, date/rate boundaries and no ledger mutation | Pending  |
| Categories, rules, merchant aliases and confirmed feedback                | [09](09-reports-budgets.md), G09                                    | Deterministic precedence, profile isolation and no draft/prediction training    | Pending  |
| Daily reports, filters, comparisons and monthly budgets                   | [09](09-reports-budgets.md), G09                                    | Independently calculated totals and drill-down/report-period tests              | Pending  |
| Recurring commitments, unusual spending and reminder controls             | [10](10-recurring-backups.md), G10                                  | Suggestions versus facts, deduplication, quiet hours and device evidence        | Pending  |
| Scheduled backup and visible failures                                     | [10](10-recurring-backups.md), G10                                  | Revoked access/rotation failure and independent restore                         | Pending  |
| Accessibility, light/dark and state handling                              | Each UI phase; [11](11-beta-acceptance.md), G11                     | Focused UI tests and reference-device checklist                                 | Pending  |
| Performance, upgrade and complete beta journeys                           | [11](11-beta-acceptance.md), G11                                    | Versioned stress fixtures, measured budgets and upgrade/recovery results        | Pending  |
| Beta accepted with privacy-safe feedback                                  | [11](11-beta-acceptance.md), H03                                    | APK, limitations, findings and explicit acceptance                              | Pending  |

## After beta

| Requirement                                                               | Owner / gate                              | Required evidence                                               | Status   |
| ------------------------------------------------------------------------- | ----------------------------------------- | --------------------------------------------------------------- | -------- |
| Portable merge, branching conflicts and reversible identity links         | [12](12-portable-merge.md), G12           | Idempotence, compatibility/invariant and conflict tests         | Pending  |
| Dependency-aware undo and no resurrection                                 | [12](12-portable-merge.md), G12           | Import/edit/undo/reimport state-machine fixtures                | Pending  |
| Scoped export and allocation privacy                                      | [13](13-scoped-sync.md), G13S             | Payload/history/metadata inspection before transmission         | Pending  |
| Scope expansion, grant enforcement and partial identities                 | [13](13-scoped-sync.md), G13S             | No duplicates or leaked private context across grants           | Pending  |
| Authenticated pairing, resumable wireless exchange and multi-hop behavior | [13](13-scoped-sync.md), G13              | Protocol tests and two-phone acceptance                         | Pending  |
| Investment/MMF forecasts, hosted rules, iOS and other deferred features   | [Future directions](future-directions.md) | Dedicated plans and their entry decisions before implementation | Deferred |

## Coverage audit procedure

- At phase start, reconcile this matrix with the current specification and the phase's
  entry gates.
- At handoff, link evidence, name unsupported cases and update downstream assumptions.
- Add new requirements to the additions log and matrix before coding their dependent
  behavior.
- Do not mark a provider covered solely because one message parsed or a report compiled.
- A failed or stale gate must be reopened. An approved scope change records what moved,
  why, who accepted it and which phase now owns it.
