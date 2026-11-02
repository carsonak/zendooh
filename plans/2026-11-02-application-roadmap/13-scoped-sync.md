# Phase 13 — Implement authorized subsets and wireless synchronization

**Status:** Not started. No implementation gate is closed by creating this document.

[Roadmap and execution contract](overview.md) · [Acceptance matrix](acceptance-matrix.md)

## Goal and boundaries

First prove scoped encrypted file exchange, then reuse it over a replaceable Android
transport. A business-only peer receives authorized allocations without private source
totals or messages. Pairing does not authorize unrestricted access.

## Entry gates

G12. G13S below must close before production wireless exchange; two phones are required
only for final device acceptance.

Verify gate evidence against the current implementation before starting dependent work.
Investigation and independent work may proceed while a gate is pending; do not claim a
phase complete or use real data without the applicable technical and human gates.

## Implementation slices

- [ ] Document the threat model and grant/projection policy, including
      read/append/edit/export/delegation distinctions, scope changes and partial-replica
      limits.
- [ ] Implement scoped serialized representations and encrypted file export/import,
      filtering history, provenance, inventories and metadata before transmission.
- [ ] Close G13S with payload-level authorization and scope-expansion tests before
      enabling wireless financial exchange.
- [ ] Evaluate transport/privacy/platform compatibility; establish device-key pairing,
      temporary verification data and authenticated sessions through narrow interfaces.
- [ ] Implement captured-frontier incremental batches, bounded staging,
      checkpoints/inventory reconciliation, acknowledgments, cancellation and resumable
      transfer.
- [ ] Recheck grants during transfers; add Sync now/status and only then optional
      foreground discovery/automation with supported background continuation.
- [ ] Exercise two-phone and multi-hop fixtures, malicious peers and conflict/undo
      integration; update automation summaries.

Deliver each coherent slice with focused tests, a runnable demonstration where applicable,
and a local commit. Update this checklist and the gate register after meaningful progress.

## Interfaces, data and failure behavior

Separate transport, authentication/authorization, replication, validation, merge and
reporting. Use versioned authenticated protocols and vetted crypto. Device/workspace IDs
and names are not credentials. Restricted-allocation editing and delegation need a
documented safe policy before exposure; default-deny unsupported rights. Any capability
expansion must preserve privacy across metadata and derived learning features, not merely
hidden UI fields.

Apply the shared verification and compatibility contract in the overview. Extend
migrations, backup/restore, revisions and privacy checks whenever this phase introduces
persisted data.

## Acceptance and verification

- [ ] G13S: For the KES 6,000 mixed payment, a business-only payload contains the KES
      4,000 authorized allocation and no private total, balance, remainder, original
      message or revealing metadata/history.
- [ ] G13S: Scope expansion links partial identities to full records without duplication;
      read-only grants cannot authorize edits, and rejected scopes leave live state
      intact.
- [ ] G13: Every session authenticates peers; stale/revoked grants, replay and
      malformed/oversized batches fail safely.
- [ ] Interrupted transfer resumes without repeated application; concurrent new changes
      wait for a later delta; captured batches apply atomically.
- [ ] Multi-hop delivery and divergent edits converge or expose conflicts; transport
      changes require no change to financial meaning.
- [ ] Two-device tests cover initial pairing, remembered peers, interruption, scope
      changes and revocation, with explicit background/platform limits.
- [ ] Revocation prevents future unauthorized exchange without claiming erasure of data
      already held by an offline peer.

Record commands, results, fixture/dataset versions and device evidence below. A blocked or
unexecuted check is not a pass. Fix material failures before closing this phase's gate.

## Human actions

Beginning: prepare a request for a second Android phone with required capabilities and
test steps; it need not block file/protocol development. End: complete automated
grants/protocol tests before grouping the two-phone pairing/interruption checklist. User
can obtain another Android phone later.

## Decisions to resolve during implementation

Choose transport after validation; Nearby Connections is a candidate, not a commitment.
Document protocol compatibility, peer revocation, key lifecycle, grant versioning and
restricted-edit semantics before dependent slices. Hosting, internet relays and
multiple-administrator governance are not implicitly included.

Record the decision, rationale and validation before its dependent slice begins. Routine
implementation choices belong to the implementing agent; material product-scope or privacy
changes require user agreement. Add durable architecture decisions where needed.

## Completion evidence and local commits

- Checks and demonstrations: not run; this is an implementation plan.
- Gate result and limitations: pending.
- Implementation commits: none. Keep commits local until explicit push approval.
- Handoff: record what the next phase may rely on and any remaining independent work.

## New additions

None yet. Record date, request, rationale, acceptance impact and affected phases/gates.

## Deviations from the original plan

None yet. Record original expectation, replacement, reason, authorization where needed,
and verification. Update downstream documents before starting affected work.

## Learning notes

None yet. Record discoveries, failed assumptions, device findings and follow-up
experiments without private data or transient operational logs.
