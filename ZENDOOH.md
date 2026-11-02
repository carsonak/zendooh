# Zendooh — Product and Architecture Specification

**Reviewed:** 2 November 2026

**Purpose:** Define Zendooh's product behavior, architecture, implementation priorities,
and unresolved design choices for developers and contributors. Focus on product intent and
decisions costly to change later; concrete schemas, APIs, modules and library versions
remain implementation work.

**Status key:** **Confirmed** identifies an established product requirement. **Accepted
recommendation** identifies an adopted design approach whose implementation details may be
refined. **Open** identifies an unresolved choice. **Deferred** identifies future work
rather than an initial delivery requirement. These labels describe design status, not
whether a feature has shipped.

The intended foundation is Kotlin Multiplatform with shared Compose UI, an Android-first
prototype, local financial processing, adaptive parsing, and selective encrypted device
synchronisation. Backups and synchronisation belong to the intended product. Early
fictional-data prototypes may precede them, but portable recovery is required before
real-data trials; wireless sync follows the agreed beta. Library candidates, example
figures, and provisional performance targets require validation before becoming
implementation or release requirements.

## Contents

1. [Product vision and principles](#1-product-vision-and-principles)
2. [System overview](#2-system-overview)
3. [Platform and architectural foundation](#3-platform-and-architectural-foundation)
4. [Workspaces, identities and access](#4-workspaces-identities-and-access)
5. [Acquiring financial evidence](#5-acquiring-financial-evidence)
6. [Adaptive interpretation](#6-adaptive-interpretation)
7. [Canonical financial records](#7-canonical-financial-records)
8. [Learning financial meaning](#8-learning-financial-meaning)
9. [Insights and everyday experience](#9-insights-and-everyday-experience)
10. [Editing history and merging](#10-editing-history-and-merging)
11. [Sharing backups and recovery](#11-sharing-backups-and-recovery)
12. [Privacy security and data lifecycle](#12-privacy-security-and-data-lifecycle)
13. [Verification and delivery](#13-verification-and-delivery)
14. [Future directions and open decisions](#14-future-directions-and-open-decisions)

## 1. Product vision and principles

### Purpose and priorities

**Confirmed:** Zendooh should feel like a personal financial assistant: it automatically
interprets transaction evidence, learns the user's categorisation preferences, and shows
useful financial insights with little repetitive work. Users should open it to understand
their finances, rather than maintain a database or classify 10–20 transactions every day.
Kenyan mobile-money usage is an important starting context.

**Confirmed:** Build a useful tool for me and my peers first. A commercial product is a
secondary possibility. Rapid AI-assisted development is intended; useful complexity is
acceptable when it improves robustness and the user experience.

**Accepted recommendations:**

- Operate offline by default, with local financial records and learning. Normal use should
  not depend on a cloud account or server.
- Reconstruct and explain finances; do not initiate payments or transfers, collect
  bank-login credentials, or scrape logged-in banking sessions. Target mobile-money, bank,
  savings, cash, and loan records through authorised evidence.
- Organise intelligence into **perception** (extract and reconcile events),
  **understanding** (categories, entities, relationships), and **insight** (questions,
  comparisons, trends).
- Automate reliable, reversible work; keep uncertain interpretations provisional and ask
  for clarification selectively. Insufficient evidence should produce an incomplete
  answer, not invented certainty.

### Name and brand

**Confirmed:** Use **Zendooh** as the application name. Parent-company naming is deferred.

**Accepted recommendations:** Keep Zendooh as a provisional working brand, with a calm,
friendly financial identity. “Zen + money” and **“Money, minus the stress.”** are the
proposed brand story and positioning, not completed branding work.

**Open:** Trademark clearance, similar-name conflicts, domains, handles, and final visual
identity. Conduct formal clearance before public launch and prioritize a word mark if
clearance succeeds. Legal ownership and name availability have not been established.

## 2. System overview

### From evidence to insight

The flow below describes responsibilities, not a fixed schema or execution schedule.
Structured inputs bypass text extraction but pass the same financial validation.
Reconciliation can revisit records as new evidence arrives.

```text
Authorized sources / manual input
  → acquisition and source provenance
  → adaptive extraction (where needed)
  → validation, confidence review and duplicate detection
  → canonical events, postings and allocations
  → categorization and relationships
  → budgets, reports and insights

Confirmed corrections → saved revisions → parser/category learning
Authorized records and operations → scoped exports, backups and device sync
```

| Intelligence layer | Purpose                                                                       |
| ------------------ | ----------------------------------------------------------------------------- |
| Perception         | Extract events and reconcile evidence: what happened?                         |
| Understanding      | Identify categories, entities and relationships: what does it mean?           |
| Insight            | Answer questions, compare periods and reveal trends: what can the user learn? |

### Responsibility boundaries

**Accepted recommendation:** Use one local encrypted database containing multiple
financial profiles, with stable account identities and authorization scoped to
profiles/accounts. Keep these conceptual responsibilities separate; they need not each
become a module immediately.

- **Finance core:** accounts, ledger, parsing, categorization, allocations,
  reconciliation, budgets, analytics.
- **Data core:** identities, persistence, saved revisions, branching, identity linking,
  and merge/undo.
- **Sync core:** peer trust, authorized replication, protocol, checkpoints, encryption,
  and interchangeable transports.
- **Platform adapters:** message acquisition, permissions, secure key storage, local
  authentication, background execution, and presentation integration.

The finance layer creates permitted financial representations; the generic sync layer
exchanges them. Neither the ledger nor the merge engine should depend on a wireless
transport or Android message API.

## 3. Platform and architectural foundation

### Technology direction

**Confirmed:** Use Kotlin as the primary language. Prioritize a working Android proof of
concept, keep transaction acquisition separate from the core, and preserve opportunities
to reuse the system elsewhere. Store distribution and monetization should not block the
prototype.

**Accepted recommendation:** Start with **Kotlin Multiplatform + Compose Multiplatform**,
sharing UI and business logic while implementing Android integrations natively. Target
Android first; add and validate iOS after core workflows stabilize.

| Area                   | Adopted starting direction / implementation flexibility                                                            |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------ |
| UI                     | Shared Compose UI; Android uses the Compose ecosystem and Material 3                                               |
| Structure              | MVVM with unidirectional state flow; clear domain, data, UI, and platform boundaries                               |
| Concurrency            | Kotlin coroutines and StateFlow                                                                                    |
| Storage                | SQLite as the financial source of truth; Room is the recommended persistence starting point                        |
| Supporting tools       | Gradle Kotlin DSL; DataStore for preferences; Android background scheduling where appropriate                      |
| Candidate dependencies | Koin preferred for shared dependency injection; navigation and other libraries must suit the actual shared project |
| Verification           | Domain/unit tests, integration tests, and focused Compose UI tests                                                 |

Library versions, encryption integration, exact modules, and final dependency choices
remain implementation decisions. Use SQLite as the canonical store and derive graph
structures from it when useful; a separate graph database is unnecessary for the current
scope.

**Accepted implementation guidance:** Keep platform APIs in `androidMain`/platform modules
and reusable logic in shared Kotlin. Prefer interfaces and dependency injection; use
`expect`/`actual` where justified. Enable only needed targets. Android-only simplification
is a fallback if KMP materially obstructs progress. Validate Room's
multiplatform/encryption integration before selection.

Test on physical Android devices early. Share signed release APKs with early testers,
retaining a consistent signing key for updates. Android development can proceed on
Windows; local iOS builds/testing require access to macOS/Xcode, with TestFlight a
proposed beta route. iOS remains desirable rather than an immediate requirement. Validate
distribution details when implementing.

### Sharing and platform tradeoffs

**Accepted guidance:** Share financial models, parsing, validation, deduplication,
categorization, use cases, repository contracts and practical UI in Kotlin. Keep the
parser independently testable without UI or platform services. Android-only APIs belong in
platform source sets; shared code should use narrow interfaces.

KMP supports reuse while adding build, dependency and interoperability complexity. Sharing
is practical rather than absolute: native integration and platform-specific UI adjustments
remain appropriate. Keep targets and modules limited to demonstrated needs. Performance
and platform polish require measurement on actual devices.

Source adapters may expose historical scans, one-time imports or streams according to
capability; do not force every source into a universal streaming contract. Normalized
records share financial rules regardless of source while retaining their provenance. iOS
ingestion must be designed around permitted manual, import or sharing workflows; shared
code does not promise identical acquisition capabilities.

## 4. Workspaces, identities and access

### Identity and authority

**Confirmed:** Preserve personal/business separation across phones, support selective
account transfer and sync, and provide editable, human-friendly identifiers alongside
internal IDs.

**Accepted identity model:**

| Identity                                         | Meaning and lifecycle                                                        |
| ------------------------------------------------ | ---------------------------------------------------------------------------- |
| Workspace/dataset                                | Stable financial collection across backups, imports, and authorized replicas |
| Profile                                          | Personal, business, or another financial scope                               |
| Account                                          | Stable financial account, independently transferable                         |
| Installation                                     | Current installation; changes after reinstall/reset                          |
| Device key                                       | Cryptographic identity of a trusted peer                                     |
| SIM identity                                     | App-managed identity mapped to observed subscriptions                        |
| Event, evidence, allocation, revision, operation | Globally unique record identities preserved through replication              |

Use random, collision-resistant IDs without embedded personal information. Friendly names
can change without changing IDs. IDs identify data; possession of an ID never authorizes
access.

Keep SMS-observation, importing, operation-authoring, and restored-backup lineage
distinct; the original receiving device can be unknown. Access may distinguish read,
append, edit, export, and delegation rather than treating pairing as unrestricted
ownership. Exact grants and administration remain design work.

Link genuinely equivalent identities through a versioned, undoable canonical-ID/alias
mapping, normally retaining an existing canonical ID. Do not equate profiles merely
because their names match or they belong to one person. A combined dashboard does not
require merging identities.

### Providers, accounts and source relationships

**Accepted guidance:** Providers describe institutions/product families; users own logical
accounts within financial profiles. A provider is not itself an account. An account may
have multiple source feeds and observed SIM aliases. Preserve explicit relationships
rather than forcing all evidence, accounts and allocations into a single parent tree.
Combined reporting does not require collapsing the underlying identities.

## 5. Acquiring financial evidence

### Ingestion and scanning

**Accepted recommendations:** Manual entry and controlled message/record imports are
permanent ingestion paths, enabling a complete prototype without automatic SMS access.
Already structured input can bypass text parsing while still passing common financial
validation and deduplication.

- Onboarding explains local processing, requests permissions contextually, lets users
  choose a historical scan period, and confirms provider/account/SIM mappings.
- Scan promptly on app entry/resume and Refresh; support historical import, full rescans,
  and reparsing. Optional scheduled scans are best-effort. Continuous SMS/notification
  listeners are not the default. Notification ingestion remains an independent,
  permission-controlled adapter.
- Use incremental checkpoints plus overlap, scoped source fingerprints, indexes, bounded
  batches, cancellation, and visible progress. Android SMS row IDs are installation-local,
  not global financial identities. Handle restored/edited/late messages, permission
  revocation, unreadable inputs, and missing metadata without duplication or loss.
- Track unmatched financial-looking inputs for later learning/reprocessing, using
  references/minimal metadata consistent with retention rules. Reparsing must not
  duplicate events or silently overwrite user corrections.
- Start with M-Pesa coverage and representative fixtures; expand to Airtel Money, banks,
  M-Shwari, Pochi, savings, and loan formats. The agreed beta covers M-Pesa, Airtel Money,
  Fuliza and M-Shwari; enumerate supported message families and review-only limitations
  during implementation. Other providers follow. Use adaptive patterns to support new
  formats rather than relying on a handwritten parser for every provider.

Permission denial must leave manual/import workflows usable. Prototype OS permissions and
later store approval are separate concerns; successful sideloading does not establish
public-distribution eligibility.

### SIM provenance

**Confirmed:** Track receiving-SIM provenance so two SIMs from the same provider can
remain distinct, including after moving between phones. **Accepted recommendation:** Keep
receiving SIM and referenced financial account as separate fields. Treat Android
subscription IDs/slots as local observations rather than permanent SIM identities; ask the
user to resolve ambiguous mappings.

Sender names and message threads cannot reliably distinguish two receiving SIMs from the
same provider. Keep missing mappings unresolved until evidence or user confirmation can
resolve them; never fill gaps with a guessed permanent identity.

## 6. Adaptive interpretation

### Teaching and extraction

**Confirmed:** Make adaptive parsing a defining capability. Users can highlight reference,
amount, fee, balance, and other fields; Zendooh tests its interpretation on similar
messages, learns from corrections, and needs less verification as reliability improves.
New provider formats should be learnable without an application update.

**Accepted parser design:**

1. Identify the source, message family, and likely transaction type.
2. Apply learned templates using token alignment, anchors, typed extractors, optional
   fields, and template clustering.
3. Use similarity/entity extraction as a fallback for unfamiliar structures.
4. Validate extracted fields and financial semantics before creating ledger records.
5. Apply a confidence/review policy and learn from confirmed corrections.

Maintain multiple formats per provider, per-field confidence, and confidence per message
family. Version learned parsers; new versions must pass previously verified examples
before promotion and support rollback. Detect format drift and occasionally verify trusted
patterns. Prioritize unfamiliar, ambiguous, or representative unresolved examples that
teach the system most. More processed messages alone do not establish correctness.

Start with explainable adaptive patterns. Add specialized on-device ML only where
evaluation demonstrates value; a general-purpose LLM or cloud model is not required. ML
Kit entity extraction and LiteRT are candidate technologies. Automation thresholds must be
calibrated against independent labeled examples before use.

### Learning cycle and confidence

**Accepted guidance:** An unfamiliar message leads to annotation or correction, pattern
induction, predictions on similar messages, and selective confirmation. Infer obvious
fields where possible; ordinary corrections should teach the system without requiring
users to annotate every message. Keep pattern learning, the versioned pattern registry,
extraction, validation, confidence evaluation and feedback as distinct responsibilities.

Confidence can differ by field, pattern, message family and overall transaction. Consider
example diversity, held-out accuracy, missing fields, structural changes and previous
corrections. A confident amount must not conceal an uncertain balance or status.
Confidence scores and numeric automation thresholds require calibration against
independent labeled data before adoption.

Treat interpretation as uncertain inference surrounded by deterministic financial
safeguards. Arithmetic consistency supports an interpretation without proving payment.
Cancelled, failed, pending and reversed messages require their own semantics even when all
fields extract successfully. Balance inquiries and promotional messages must not become
payments merely because they contain monetary values.

### Reparsing and evidence lifetime

Reprocessing must preserve user corrections and event identity. When an original source is
unavailable, use retained structured information, request new evidence where useful, or
leave fields unresolved. Never reconstruct supposedly original text from an inference. See
[data lifecycle](#12-privacy-security-and-data-lifecycle) for retention and deletion.

## 7. Canonical financial records

### Records and accounting invariants

**Accepted recommendations:** Normalize every source into a common financial model. Keep
source evidence, extraction, canonical events, ledger postings, allocations, balance
observations, and inferred relationships distinct. Evidence and events may have
many-to-many links. Use deterministic integer minor-unit or exact-decimal money arithmetic
with explicit currency; never stored binary floating point. Do not sum currencies without
an explicit conversion/valuation policy. Preserve timestamps as instants with original
timezone/offset where available.

- Recognize transaction semantics: a failed, pending, or reversed message must not
  silently become a confirmed successful payment.
- Distinguish actual money movement from its economic purpose. Transfers between the
  user's own accounts must not inflate spending or income.
- Support category splits and profile-scoped allocations; totals must reconcile exactly,
  with an explicit unallocated remainder where incomplete. Do not infer an itemized
  purchase breakdown from a payment total alone.
- Separate loan principal/liabilities from income/spending; record interest and fees
  separately. Distinguish withdrawals, deposits, refunds, reversals, and savings
  movements. A balanced, double-entry-inspired ledger is recommended; the exact accounting
  model remains open.
- Use balance arithmetic and other evidence to detect discrepancies, while accounting for
  missing messages, delayed delivery, overdrafts, and incomplete histories.
- Keep uncertain matches and inferred relationships distinguishable from established
  facts.

Support first-class manual/cash entries and corrections, including logical deletion
without SMS evidence. Validate currency, sign, dates, account rights, split totals, and
duplicate likelihood. User-confirmed manual records do not imply provider verification.
Keep provider-reported balances distinct from calculated holdings; reports must state
their account/profile scope, transfer/fee treatment, uncertain-record inclusion, and
missing coverage. Rebuild analytics from canonical records rather than treating cached
totals as authoritative.

### Matching and reconciliation

**Accepted guidance:** Transaction references, amounts and dates are matching evidence,
not globally unique identities. Assess account context, direction, providers, chronology,
fees and textual clues. Low-confidence duplicate/transfer links remain suggestions;
automatic links must be attributable and undoable.

Compare observed balances with intervening canonical postings and explain discrepancies
using expected/observed values, coverage and alternative explanations. Out-of-order
messages, separate fee entries and different balance definitions can limit reconciliation.

### Allocations across privacy boundaries

**Accepted cross-profile privacy decision:** For a KES 6,000 personal-account payment
split into KES 4,000 business and KES 2,000 personal spending, a business-only device
receives the authorized KES 4,000 allocation. It does not receive the original message,
private balance, private allocation, or total payment merely to hide them in the UI. Count
the source movement once; the allocation must not fabricate another payment.

Restricted representations need stable identities so later permission expansion can link
them to the full event without duplicating expenses. Enforce authorization before
transmission, including metadata and links that could reveal private information.

Mark restricted replicas as partial. Beta supports personal/business allocations and links
between expenses and repayments, but dedicated reimbursement balances and formal
owner-contribution accounting are deferred. Do not report an amount owed or owner equity
merely from a descriptive link; those later capabilities need explicit accounting
policies. One encrypted SQLite file does not itself isolate profiles cryptographically
from a reader with its key. Restrict transmitted data and evaluate profile-scoped
keys/containers where stronger isolation is required.

### Transaction relationships

**Confirmed beta direction:** Separate actual movements, economic allocations and
contextual relationships. Support typed links with tested financial semantics, such as
refunds and transfers, alongside custom descriptive links/groups for investment, returns,
losses, expenses and other user-defined purposes. Linked views should help users explore
money flows without creating another movement or counting the same amount repeatedly.

Custom labels do not silently change balances or establish realized gains/losses. Partial
amounts, multiple links, cycles and later corrections need explicit validation and report
behavior. New financial semantics require domain support even when text extraction or
custom labeling is possible. A universal user-programmable accounting rule language is not
a beta requirement.

## 8. Learning financial meaning

### Categorization and entities

**Accepted categorization design:** User rules → similar confirmed transactions/merchant
aliases → lightweight personalized classification. Experiment with Naive Bayes, logistic
regression, similarity matching, and incremental learning before larger models. Consider
merchant, type, account/profile, amount, timing, description, and corrections together.
Explain results and preserve manual correction.

Train primarily from user-confirmed labels rather than recycled predictions. Use the final
confirmed saved correction as learning feedback; exclude intermediate draft edits and
discarded changes. Preserve saved revision history independently. Keep profile-specific
behavior isolated unless sharing is authorized. Sync permitted labels and rules, then
rebuild local models, rather than trying to merge independently trained weights. Learning
should arise naturally from corrections; onboarding must not turn ordinary users into
full-time annotators.

Use deterministic rule priorities, manual overrides, and exceptions. Normalize merchant
names/till aliases through evidence-based entity resolution. Store feature/model versions
and validation results; identify automatic classifications explicitly. Whether
personalized parser knowledge should sync, and which examples it may require, remain open
separately from syncing confirmed category labels/rules.

### Context and enrichment

A supermarket payment does not establish an itemized grocery purchase. A recurring
person-to-person transfer may represent savings, debt repayment, family support or
business activity. Merchant identity and recurrence are contextual evidence, not proof of
economic purpose. Keep relationship inference explainable and correctable.

**Deferred enrichment:** Preserve an extension path for purchased items, quantities, unit
prices, assets, investments, projects and income-generating activities. These may link to
existing financial events without creating a second payment. Their detailed models and
attribution rules remain open.

## 9. Insights and everyday experience

### Review and progressive autonomy

**Accepted UX:** A Review Center groups uncertain classifications, possible transfers,
conflicts, and summaries of completed automation. Include budget reminders,
unusual-spending insights, quiet hours, and frequency controls. Progressive autonomy
should reduce interruptions as demonstrated reliability improves. Use **Balanced** as the
default autonomy mode, with **Careful** asking more and **Quiet** minimizing prompts while
leaving uncertain results provisional. Users may ignore low-priority reviews; daily
streaks, penalties, and engagement pressure are outside the intended experience. Exact
controls remain adaptable.

Review summaries should include parser changes, transfer matches and sync outcomes as well
as classifications and merges. Avoid repeatedly requesting already supplied context.

### Questions and dashboards

**Confirmed insight goals:** Compare categories and periods, reveal financial flows and
trends, and eventually answer questions such as whether grocery spending exceeded eating
out, whether egg prices changed, or whether an income-generating machine paid for itself.

**Accepted data limits:** Item-price comparisons require item-level prices, quantities,
and comparable products. Asset profitability requires attributable earnings and costs.
Payment SMS alone cannot supply either. Enrich the common model over time; do not promise
these answers from absent evidence. Natural-language search and embeddings are later
possibilities, not requirements for initial insights.

**Accepted dashboard scope:** Overview/holdings; income, spending and net cash flow;
account composition; category/merchant breakdowns; spending calendars and velocity;
budgets; recurring commitments; fee trends; transfer/money-flow views;
reconciliation/source coverage; and automation review. Possible displays include stacked
time series, heatmaps, breakdown charts, and Sankey graphs; these are visualization
options, not mandatory chart libraries.

Filter by period, account/profile, provider, category/merchant, currency, source, and
verification/confidence. Enable comparison, zoom/selection, drill-down to records, and
local chart/aggregate exports. Label forecasts, incomplete holdings, estimated balances,
and uncertain amounts explicitly. Support accessible labels, light/dark modes, useful
empty states, sparse data, and responsive device performance.

### Report meanings and user controls

**Accepted guidance:** Distinguish holdings, liabilities/net worth, external cash flow,
income, spending and savings movement. Internal transfers change account composition; fees
and exchange-rate valuation have separate effects. State the coverage and valuation basis
before presenting any total as complete.

Support user-defined category/account/profile budget limits with progress and trajectory,
and opt-in reminders. Recurring commitments inferred from history remain predictions until
confirmed. Reports should distinguish established totals from additional uncertain amounts
so apparently precise charts do not hide incomplete interpretation.

### Debt-cost forecasting

**Confirmed beta direction:** Provide explainable Fuliza and M-Shwari debt-cost forecasts
with explicit, versioned personal defaults, effective dates and assumptions. Keep
predicted charges separate from observed transactions and balances; forecasts never create
ledger postings. Missing or unsupported rates, fee structures or account history must
produce a qualified/incomplete result rather than invented precision.

Beta links to official provider terms and lets users enter, edit and save their defaults.
Validate current official sources when implementing product-specific calculations; this
specification establishes no current rates. Test exact arithmetic, rounding, date/charge
boundaries, repayment assumptions and historical reproducibility with fictional rules.

Hosted rule distribution is deferred until after multi-user beta feedback. Future checks
and downloads are optional and user-initiated, possibly prompted when using forecasts;
they must not silently overwrite personal defaults. Investment and Money Market Fund
forecasting is desired future work requiring its own valuation, yield, fee/tax and data
policies.

## 10. Editing history and merging

### Saved edits and conflicts

**Confirmed:** Avoid saving a revision on every keystroke. Preserve branching edit
histories, allow users to merge conflicting changes, and explicitly identify automatic
merges while retaining both histories. The merge engine must be independent of how data
arrives.

**Accepted editing behavior:** Keep an in-memory draft. Save validates and commits one
meaningful revision; discard abandons it. Leaving a changed screen prompts
save/discard/continue editing so navigation does not silently commit changes.

Use an append-only, author-attributed revision graph/operation log with rebuildable
current-state views. Expose revision diffs and Restore Previous Version; undo records a
compensating operation rather than erasing audit history.

**Accepted merge behavior:**

- Validate incoming data, preview changes, and apply atomically.
- Use stable event/revision/operation IDs for idempotence. Treat independently created
  records with matching financial evidence as possible duplicates requiring conservative
  reconciliation.
- Merge compatible independent edits automatically; preserve incompatible branches for
  review. Record parent revisions, automatic/manual resolution, and automatic-merge
  algorithm version.
- Journal changes in merge batches so undo stores actual changes rather than full database
  snapshots.
- If later edits depend on a merge, preview consequences and let the user preserve
  dependent work. Synchronize tombstones or compensating/revocation operations so future
  sync does not simply resurrect undone data.
- Keep imports/transfers non-destructive by default. Removing source records after a
  verified transfer requires a separate explicit action.

Unlimited undo and history retention have storage costs; compaction policy remains open.

### Conflict and retention boundaries

Competing amounts, category splits and identity assignments require review or an explicit,
documented resolution policy. Independent-field edits are automatically compatible only
when the combined result still satisfies financial invariants.

Compaction must respect agreed undo, retention and replica guarantees. Those guarantees
remain open; do not discard history prematurely. Backup imports, file exchanges and
wireless sync use the same core merge semantics, with source-specific validation at the
boundary.

## 11. Sharing backups and recovery

### Device pairing and replication

**Confirmed:** Implement wireless device-to-device merging/synchronization as part of the
intended product. Paired phones should recognize one another, offer sync, and optionally
sync automatically. Discover periodically while the app is open; an active transfer may
continue in the background where supported.

**Accepted recommendations:**

- Pair initially through QR or a verification flow, establish device keys, and explicitly
  grant selected profile/account scopes. QR contents should be temporary pairing
  information, not permanent database/recovery secrets.
- Authenticate every session cryptographically even for remembered peers. A matching
  workspace ID, device name, or successful connection does not establish authorization.
- Separate replication, merge resolution, and transport. Nearby Connections is the
  recommended first Android transport to investigate; local Wi-Fi, Wi-Fi Direct,
  Bluetooth, and encrypted file import remain alternatives. Final transport choice needs
  privacy and platform validation.
- Exchange missing authorized operations incrementally. Checkpoints need
  reconciliation/inventory support for selective history and later scope changes; stable
  operation IDs prevent duplicate application.
- Version protocol/schema contracts, preserve causal dependencies, and validate canonical
  serialization, authenticity, grant versions, and compatibility before applying data.
  Re-check authorization if grants change during a transfer; rejected/incompatible input
  must leave live records intact. Final wire format and handshake remain open.
- Support resumable encrypted batches with identities, integrity checks, ordering, and
  acknowledgments. Stage transfers independently and apply complete data atomically;
  finish a captured batch set before exchanging newer changes.
- Scope sharing by profile/account, with selectable history and potentially data types.
  Expansion fills gaps without duplicates. Revocation prevents future access but cannot
  guarantee erasure of data already received by an offline peer.
- Provide a user-initiated Sync now path and visible active-transfer status. Background
  continuation is conditional, not an unconditional promise.

Build local merge/import correctness before production wireless sync. Wireless
synchronization remains an intended product feature rather than a prerequisite for the
first working prototype.

### Protocol responsibilities

| Responsibility            | Boundary                                                                |
| ------------------------- | ----------------------------------------------------------------------- |
| Transport                 | Discovery and byte delivery without financial semantics                 |
| Session and authorization | Authenticate peers, establish protected sessions and enforce grants     |
| Replication               | Identify missing authorized operations and causal dependencies          |
| Validation                | Check integrity, authenticity, compatibility, scope and resource bounds |
| Merge                     | Stage and apply idempotently, preserve branches and journal effects     |
| Reporting                 | Show progress, interruptions, imports, automatic merges and conflicts   |

Discovery is untrusted, and pairing does not make received content safe. Validate every
incoming batch. Concurrent writes belong to a later delta after the captured transfer
frontier. Transport privacy implications and background constraints require validation
before selection.

### Backups and portable subsets

**Confirmed:** Support a “set and forget” experience for categorization, budgets, and
backups, with useful summaries of automatic classifications and merges.

**Accepted backup approach:** Scheduled encrypted backups to a user-selected destination;
portable passphrase/recovery-key restoration, with locally protected keys enabling
convenient automatic backups. Use biometrics or device credentials for local unlock,
keeping unlock, device pairing, and backup recovery separate. Clearly distinguish
device-bound protection from recovery on a replacement phone. Offer optional recovery
checks instead of forcing password entry solely for muscle memory. Never imply a backup is
recoverable after device loss when its only key remains on that device.

Exports should be versioned, integrity-protected containers preserving IDs, history,
provenance, and authorized restore metadata. Use the platform document picker with
persistent access where supported; disclose if the selected destination is cloud-backed.
Validate and stage restores, preview replace versus merge, and commit atomically. Rotate
retained backups, surface failures, and test restoration independently of the original
phone's key.

Support explicit encrypted export/import of a workspace, selected profile or selected
account within the user's authorization. Scope filtering applies to history, provenance
and restore metadata as well as current records. Backup failures must leave live records
intact. Restore on a replacement phone must be tested without the original device key.

## 12. Privacy security and data lifecycle

### Retention and trust

**Confirmed:** Missing original messages after a reset or device change are not errors or
warnings; transaction details should still show that the reference is unavailable. Source
availability and financial integrity are separate properties.

**Accepted storage design:** Persist structured transactions, necessary provenance, and
privacy-reviewed learned information. Process raw messages transiently by default; do not
permanently duplicate the SMS inbox. Re-read an authorized original when it exists. Any
necessary temporary copy needs encryption, expiry, and deletion rules.

**Confirmed beta retention:** A bounded encrypted teaching cache may retain selected raw
messages for a concrete teaching/evaluation task until that task completes or seven days
elapse, whichever comes first. Allow manual clearing and exclude the cache from backups
and sync. Enforce expiry on access/startup even when background cleanup is delayed; do not
renew retention indefinitely or retain original text disguised as learned features.
Structured corrections and privacy-reviewed templates have separate retention rules.
Document cleanup and key-lifecycle limits without promising physical flash erasure.

Store parser version and extraction provenance. If the original disappears, retain the
valid structured record but acknowledge that full reparsing may be impossible. Distinguish
**delete source message**, **delete imported transaction and dependent derived data**, and
**forget relevant learned information**. Automatic propagation of source deletion is not
an agreed feature.

**Accepted trust model:** Keep parsing confidence, entity/match confidence, source
availability, consistency findings, and verification status independent. Facts/fields
should identify their source, extraction method/version, corrections, and
observed/inferred/user-confirmed status. An SMS or successful parser validation is not
independent proof of payment. Never label data externally verified without actual
independent evidence. Explain contradictions and plausible missing-data causes without
automatically declaring fraud.

**Accepted privacy safeguards:** Local learning and processing by default; no raw
financial messages or sensitive values in ordinary logs, analytics, crash reports, or
AI-agent fixtures. Use platform-backed key protection where appropriate. Apply
retention/deletion choices to caches, temporary files, and backups. Learned patterns may
memorize private values and need scrutiny too. Privacy guarantees must state their threat
model and limits rather than promise absolute protection.

Keep analytics/crash reporting off by default or omit it. Minimize permissions/networking;
omit production `INTERNET` permission unless an intentional feature needs it. Configure OS
backup exclusions; protect clipboard, exports, notifications, temporary files, and
screenshots, with an optional secure-screen mode. Use audited cryptographic libraries,
authenticated encryption, and reviewed key management. SQLCipher storage and Argon2id
recovery-key derivation are candidates. Validate untrusted QR/import/peer data with size,
schema, resource, authorization, and integrity checks. Plan security review before public
release.

### Threat model and source availability

Account for device theft, malware, forged messages, malicious archives, compromised paired
peers, unauthorized profile access, accidental disclosure and loss of keys. State limits
in rooted/debug environments and against an attacker able to read unlocked data. A locally
encrypted file alone cannot provide every profile-isolation guarantee.

Financial data must not be silently uploaded or sent to remote inference services. Any
future external processing requires deliberate authorization and disclosure.

Distinguish unavailable evidence after migration from evidence observed disappearing on
the same installation. Neither condition alone establishes fraud. Source deletion,
transaction deletion and forgetting learned information remain separate operations;
replica and backup effects must be explicit.

## 13. Verification and delivery

### Datasets and evaluation

**Accepted verification strategy:**

- Maintain synthetic fixtures, carefully sanitized real-format fixtures, and separately
  controlled private on-device examples.
- Sanitize identities, references, account details, amounts, dates/times, merchants, and
  identifying combinations; preserve useful structure and review exports locally. Consent
  and sanitization do not make every sample safe to export.
- Keep private data outside coding-agent access. Share aggregate failures or synthetic
  reproductions instead.
- Use extraction unit tests, property-based variations, independently verified golden
  datasets, and learning/regression tests. Separate teaching examples from held-out
  evaluation; test across message families and format/time changes.
- Exercise reinstalls, restored backups, moved SIMs, repeated imports, changed sync scope,
  interrupted sync, divergent edits, merge undo, and restricted allocations.
- Test malformed/spoofed inputs, replay, corrupt/oversized backups, wrong passphrases,
  missing recovery keys, migration/rollback, and process death. Verify restricted data is
  absent from payloads, metadata, inventories, search indexes, charts, logs, and model
  features—not just hidden in screens. Benchmark large inboxes, revision histories, and
  bounded-memory sync/backup on representative devices; 10k–100k SMS is a proposed
  stress-test range.

Measure critical-field precision, recall, field accuracy, automation coverage, confidence
calibration, regressions, intervention rate, and unknown-format detection. Provisional
long-term goals are **99.9% critical-field precision, 98% recall, and 90% automated
coverage**. These are unvalidated aspirations, not achieved performance or initial release
gates.

### End-to-end acceptance journeys

| Journey           | Expected behavior                                                                                                                                      |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| First import      | Historical examples map to accounts, events, fees and balances; dashboard shows unresolved review items; repeat import adds no duplicates.             |
| Mixed purchase    | A KES 6,000 payment splits into KES 4,000 business and KES 2,000 personal; restricted replicas receive only authorized data and no duplicate movement. |
| Nearby sync       | Pair, grant scope, reconnect, preserve conflicting edits and resume an interrupted transfer without repeated application.                              |
| Replacement phone | Restore with portable recovery credentials, retain record IDs, create a new installation identity and show missing source messages without an error.   |
| Merge undo        | Import, edit an imported record, then preview undo and resolve dependencies without silently losing later work.                                        |
| Learning          | Confirm a pattern or category, evaluate unseen examples, explain later automation, correct mistakes and verify regression behavior.                    |

Use deterministic fictional data for these journeys. Exercise multiple-hop replication,
concurrent edits, scope expansion and state-machine/property-based tests where useful.

### Agreed beta and incremental delivery

**Confirmed beta scope:** An installable Android application, including development-mode
installation when needed, with personal/business profiles, multiple accounts/SIMs, cash,
M-Pesa, Airtel Money, Fuliza and M-Shwari. Include adaptive SMS learning/review,
corrections, allocations/relationships, debt forecasts, categories, basic
reports/comparisons, monthly budgets, confirmed recurring commitments, optional reminders,
unusual-spending suggestions, encrypted storage, portable recovery and scheduled backups.

Daily beta reports cover balances with coverage, income/spending/cash flow, category and
merchant breakdowns, period comparisons, fee trends and linked transactions. Advanced
visualizations, item/investment insights and natural-language queries remain later work.
Use explicit currencies; initial journeys emphasize KES. Reporting starts with a
configurable Africa/Nairobi workspace timezone while preserving instants and known source
offsets.

**Confirmed delivery gates:** Use fictional data first. Require user acceptance of the
first useful phone journey, then protection/upgrade/portable-recovery evidence and
explicit approval before real-data trials. New workflows must pass their own
technical/privacy checks before using real data. Beta acceptance is a later human
milestone; routine technically independent work need not wait for approval after every
slice.

The [phased application roadmap](plans/2026-11-02-application-roadmap/overview.md) owns
execution details, prerequisites, evidence and learning/change logs. Its sequence is:

1. Verify tooling and phone delivery; validate persistence/encryption and shared
   boundaries.
2. Deliver a fictional-data manual ledger and saved revisions, then portable replacement
   recovery and real-data protection gates.
3. Add profiles, allocations, relationships, controlled/SMS acquisition and adaptive
   learning.
4. Complete beta provider semantics, debt forecasts, categorization, reports and budgets.
5. Add recurring commitments, quiet automation and scheduled backups; harden and accept
   beta.
6. Implement portable merging/conflicts/undo, then authorized subsets and wireless sync.
7. Expand investment forecasting, hosted rule updates, iOS and other deferred capabilities
   after their prerequisites and dedicated decisions.

These are behavioral gates, not mandatory schemas, class hierarchies or library choices.
Agents may improve implementation approaches while preserving accepted behavior and
recording material decisions. Use small coherent local commits and keep implementation
commits unpushed until explicitly approved. Group necessary human actions at phase entry
or exit after completing available independent work.

**Accepted development guidance:** Deliver small end-to-end slices with deterministic
fixtures, migrations, and executable acceptance checks. Record material schema, protocol,
cryptographic, and authorization choices in architecture decision records, including
migration/rollback. Keep repository guidance/specifications aligned with implementation
and distinguish designed from shipped features.

## 14. Future directions and open decisions

### Deferred capabilities

| Direction                        | Decision and boundary                                                                                                                                                                                                                                            |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Receipt OCR                      | Explicitly deferred. Intended mainly to enrich and split an existing payment, avoiding duplicate transactions. On-device processing preferred; item categorization approach remains open.                                                                        |
| Personal item-price history      | Desired future insight using itemized receipts or other suitable records.                                                                                                                                                                                        |
| Crowdsourced prices / best deals | Future exploration with explicit opt-in, minimal contributions, aggregation/privacy safeguards, no raw receipt/transaction uploads by default, and no workspace-ID linkage.                                                                                      |
| Community parser library         | Welcomed future feature after reliable local learning. Share reviewed, sanitized, versioned declarative patterns with regression checks, withdrawal/rollback, and malicious-submission controls; never executable parsers or automatically trusted templates.    |
| Monetization                     | No paid tier or pricing selected. Keep adaptive parsing/basic community support central to the product's value. Advanced insights, business/asset analytics, imports, sync, and backup/recovery are candidate paid capabilities; feature gates remain undecided. |
| Other evidence sources           | Extend through adapters for statements, email receipts, invoices, forwarded/shared text, and other records.                                                                                                                                                      |
| iOS and other platforms          | Preserve shared foundations; validate actual platform ingestion and delivery separately. No promise of Android-equivalent message access.                                                                                                                        |
| POS / employee-device products   | Potential reuse of sync/data technology. Do not add inventory, fiscal, or POS-specific assumptions to the initial finance model.                                                                                                                                 |

### Unresolved choices

The following choices remain open:

- **Release boundary:** The Android beta scope and post-beta sync ordering are agreed
  above. The exact public release, wider provider coverage, validated OS/device support
  and iOS timing remain unspecified; the current build minimum is not proof of
  compatibility.
- **Acquisition/distribution:** Prototype message ingestion can be tested separately from
  store release; production permissions, distribution requirements, and platform-specific
  acquisition need validation. Do not assume approval or unrestricted historical SMS
  access.
- **Detailed financial model:** Final tables/interfaces, full double-entry versus balanced
  postings, currency conversion/valuation, negative balances, and detailed reconciliation
  rules require specification and tests. Dedicated reimbursement/owner-contribution
  accounting is deferred; beta allocations and descriptive links must not imply it exists.
- **Learning policy:** Pattern representation, calibration, critical-field acceptance,
  review sampling, promotion/rollback rules, safe reprocessing, and personalized
  parser-knowledge sync remain open. No particular ML framework/model or natural-language
  query approach is selected.
- **Security/protocol:** Final cryptographic scheme, key lifecycle/recovery, lost-device
  handling, key rotation, multiple administrators, peer revocation, transports, protocol
  formats, retention/compaction and undo guarantees need implementation-level design.
  Whether a device may edit a restricted allocation, and the default profile/account grant
  granularity, remain open.
- **Deletion semantics:** Whether source deletion should trigger transaction deletion, and
  how forgetting learned information interacts with authorized replicas/backups, are not
  fully specified for the broader product. Beta does not automatically delete transactions
  when source messages disappear, and its teaching-cache lifetime is bounded as above.
- **Future data and business models:** Receipt/item normalization, asset attribution,
  community governance/privacy, pricing, and parent-company branding remain open. The
  repository currently uses Apache 2.0; future business/content licensing choices must not
  be confused with an unchosen repository license.

### Developer learning guidance

**Learning recommendation:** Study information extraction/template induction → ML
fundamentals → human-in-the-loop/active learning → probability/calibration/drift → entity
resolution → retrieval/embeddings. A small pure Kotlin parser with synthetic teaching
examples, held-out variations, financial checks, and correction/regression tests is the
proposed first exercise.
