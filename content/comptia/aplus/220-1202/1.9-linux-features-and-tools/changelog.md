# Changelog

## 2026-07-13 - Acceptance

- Recorded GO decisions from blocker-fix verification and bloat review; no
  remaining blockers, delete candidates, rewrite candidates, or merge
  candidates were found.
- Recorded the user-reported passing manual Anki smoke test for Objective 1.9
  Basic, Cloze, and Command imports, including headers, rendered HTML and Cloze
  content, typed-answer comparison, Instructor Notes, metadata tags, the
  42-note total, and Card ID re-import/update behavior without duplicates. The
  Anki version and disposable profile name were not provided.
- Accepted the final Objective 1.9 card set: 10 Basic cards, five Cloze cards,
  and 27 Command cards, including 18 HighYield cards.
- Verified generated output expectations: `Basic.tsv` contains 10 data rows,
  `Cloze.tsv` contains five, and `Command.tsv` contains 27; no Image or media
  output is expected.
- Confirmed that no Objective 1.10 content was created.

## 2026-07-13 - Independent-review fixes

- Removed unsupported learner-facing characterizations of option-specific
  `ping` examples and limited recall to the official base command.
- Removed unsupported access-policy guidance from the study guide and
  source-narrowed the `/etc/shadow` Instructor Note.
- Deleted `1.9-B004` because it duplicated the `dnf`, RPM, and `yum`
  association already tested by `1.9-T015`.
- Rewrote `1.9-T014` so `apt` is uniquely identified by its sourced expansion.
- Tightened `1.9-T018` and `1.9-T019` to identify the `curl` and `dig` commands
  named by Objective 1.9.
- Reduced the expected final card set to 10 Basic, five Cloze, and 27 Command
  cards while preserving all remaining stable IDs.
- Regenerated and verified the three TSV files at those counts, then passed
  validation, the 90-test pytest suite, Ruff lint, and Ruff format checks.

## 2026-07-13 - Objective 1.9 draft authoring

- Added the Core 2 Objective 1.9 study guide for Linux client and desktop
  features and tools.
- Added 11 Basic cards for command distinctions, configuration-file selection,
  OS components, and root access.
- Added five Cloze cards for common Linux configuration-file associations.
- Added 27 Command cards covering every base command named in the official
  objective.
- Used CompTIA A+ 220-1202 Exam Objectives v4.0 Objective 1.9 as the primary
  scope authority.
- Used Professor Messer 220-1202 v1.40 pages 18-21 as the approved secondary
  validation and page-reference source.
- Completed a private Professor Messer Core 2 practice-exam gap check; it
  reinforced permission, filesystem, package, text-search, editor, DNS, and
  route-discovery tools without supplying card wording or citations.
- Added generated domain and `Source::Messer-v140` tag support for the
  Objective 1.9 directory, with documentation and a pipeline test.
- Generated and verified `Basic.tsv` with 11 data rows, `Cloze.tsv` with five,
  and `Command.tsv` with 27; no Image or media output is expected.
- Passed validation, build, the 90-test pytest suite, Ruff lint, and Ruff format
  checks.

### Scope and source decisions

- Excluded option-specific `ping` examples from recall. Cards test only the
  official `ping` base command and its stable reachability purpose.
- Command cards test exact base-command identification. Basic cards are
  retained only when they add a materially different comparison, selection, or
  OS-component task.
- Cloze cards are limited to compact configuration-file associations and do not
  duplicate Command cards.
- No command options beyond the sourced `-h` study-guide context are required
  for recall.
- Image cards were considered and omitted because no visual identification task
  is present.
- No new secondary sources were used.
