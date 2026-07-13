# Changelog

## 2026-07-13 - Acceptance

- Recorded the user-reported passing manual Anki smoke test for the Objective
  1.11 Basic import, including headers, rendered HTML, Instructor Notes,
  metadata tags, the ten-note total, and Card ID re-import/update behavior
  without duplicates. The Anki version and disposable profile name were not
  provided.
- Recorded the independent-review GO with no required fixes and approval of the
  five HighYield classifications and omitted-concept decisions.
- Accepted the final Objective 1.11 card set: ten Basic cards, including five
  HighYield cards.
- Verified generated output expectations: `Basic.tsv` contains ten data rows;
  no Cloze, Command, Image, or media output is expected.
- Removed the obsolete cards-directory placeholder.
- Confirmed that no Objective 2.1 content was created.

## 2026-07-13 - Objective 1.11 draft authoring

- Added the Core 2 Objective 1.11 study guide for cloud email, storage and
  folder synchronization, collaboration tools, identity synchronization, and
  licensing assignment.
- Added ten Basic cards using short installation, configuration, and
  tool-selection scenarios aligned to the official `Given a scenario` wording.
- Used the official CompTIA 220-1202 Objective 1.11 as the scope authority and
  Professor Messer v1.40 p. 23 as the approved secondary validation source.
- Completed a private Core 2 practice-exam gap check; it found no additional
  official-scope, independently supported Objective 1.11 card target and did
  not supply card wording or citations.
- Recorded why general cloud scaling context and vendor-specific examples were
  not carded.
- Added generated domain and Messer-source tag support for the new objective.
- Generated and verified `Basic.tsv` with ten data rows; no Cloze, Command,
  Image, or media output is expected.
- Passed validation, build, the 92-test pytest suite, Ruff lint, and Ruff format
  checks.
- Independent review and manual Anki smoke testing remain before acceptance.
