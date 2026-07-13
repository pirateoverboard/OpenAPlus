# Changelog

## 2026-07-13 - Acceptance

- Recorded the user-reported passing manual Anki smoke test for Objective 1.10
  Basic and Cloze imports, including headers, rendered HTML and Cloze content,
  Instructor Notes, metadata tags, the 16-note total, and Card ID
  re-import/update behavior without duplicates. The Anki version and disposable
  profile name were not provided.
- Accepted the final Objective 1.10 card set: 15 Basic cards and one Cloze card,
  including seven HighYield cards.
- Verified generated output expectations: `Basic.tsv` contains 15 data rows and
  `Cloze.tsv` contains one; no Command, Image, or media output is expected.
- Confirmed that no Objective 1.11 content was created.

## 2026-07-13 - Independent-review fixes

- Corrected the study guide to distinguish 2^32 addresses from the
  approximately 4 GiB byte-addressable capacity they represent.
- Reworded the integrated-graphics explanation to state precisely that the CPU
  and GPU are on the same chip and graphics uses system memory.
- Reclassified `1.10-B004` and `1.10-B006` from Medium to Easy because each
  tests one direct requirement fact.
- Recorded the independent-review NO-GO and passing blocker-fix verification;
  no duplicate learning targets, card deletions, or remaining blockers were
  found.
- Regenerated `Basic.tsv` and `Cloze.tsv` and confirmed the final 15 Basic and
  one Cloze data rows.
- Passed validation, build, the 91-test pytest suite, Ruff lint, and Ruff format
  checks after the fixes.
- Objective 1.10 is ready for manual Anki smoke testing but is not yet accepted.

## 2026-07-13 - Objective 1.10 draft authoring

- Added the Core 2 Objective 1.10 study guide for application requirements,
  distribution methods, and device/network/operation/business impacts.
- Added 15 concise Basic scenario and selection cards plus one Cloze card for
  the reinforced 32-bit address-space fact.
- Used CompTIA A+ 220-1202 Exam Objectives v4.0 Objective 1.10 as the primary
  scope authority.
- Used Professor Messer 220-1202 v1.40 pages 22-23 as the approved secondary
  validation and page-reference source.
- Completed a private Professor Messer Core 2 practice-exam gap check; it
  reinforced 32-bit memory limits, application/OS architecture compatibility,
  and destination storage without supplying card wording or citations.
- Considered Command and Image cards and omitted them because neither exact
  command recall nor visual recognition is part of the learner task.
- Added generated Operating Systems domain and `Source::Messer-v140` tag support
  for the Objective 1.10 directory, with documentation and a pipeline test.
- Generated and verified `Basic.tsv` with 15 data rows and `Cloze.tsv` with one;
  no Command, Image, or media output is expected.
- Passed validation, build, the 91-test pytest suite, Ruff lint, and Ruff format
  checks.
- Independent content review and manual Anki smoke testing remain before
  acceptance.

### Scope and source decisions

- The official `Given a scenario` wording drives short compatibility,
  selection, and impact-classification cards.
- Vendor-specific requirements and installer UI paths remain outside card scope.
- The four impact categories are kept distinct from broader change-management
  and troubleshooting procedures.
- The application-rights statement remains study-guide context because a
  separate card would not add an official impact-category learning target.
- No new secondary sources were used, and no unresolved source ambiguity was
  found.
