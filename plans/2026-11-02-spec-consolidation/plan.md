# Specification consolidation

## Goal and constraints

Consolidate the three historical discussions into ZENDOOH.md as a navigable product and
architecture reference. Preserve current decisions, open questions, source documents and
unrelated work. Avoid freezing illustrative schemas, APIs or dependencies.

## Progress

- [x] Compare all four documents and identify omissions and conflicts.
- [x] Reorganize by data flow and integrate durable behavioral guidance.
- [x] Review source coverage, links, formatting and final changes.

## Decisions

The current specification governs conflicts. Retain Kotlin/Compose, transient message
processing and the distinction between interpretation and independent verification.
Illustrative confidence thresholds are not adopted. Existing open design questions remain
open; this consolidation does not select cryptography, accounting policy or wire formats.

## Acceptance

Linked contents, grouped subsections, preserved product promises, scoped Markdown checks,
and unchanged historical sources. No application build is required for prose-only edits.

## Verification results

Scoped Prettier check and markdownlint passed for both changed documents. All 15 internal
links resolve to headings. Source comparison preserved existing requirements while
replacing the bracketed draft-learning note with explicit saved-correction behavior.
Historical sources were left unchanged. Application tests/builds were not run because this
change is documentation only.

## Subsequent cleanup

At the user’s request, removed the three superseded source documents after consolidation.
Removed the source-links section and historical-threshold reference from ZENDOOH.md so the
specification stands alone. The source-preservation checks above describe the initial
consolidation, before this authorized cleanup.
