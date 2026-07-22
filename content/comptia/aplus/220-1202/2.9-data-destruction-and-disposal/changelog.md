# Changelog

## 2026-07-22 - Acceptance

- Recorded the blocker-fix verification GO with all four independent-review
  findings resolved and no new issues.
- Recorded the user-reported passing manual Anki smoke test for the Objective
  2.9 Basic import, including headers, rendered HTML, Instructor Notes,
  metadata tags, the 13-note total, and Card ID re-import/update behavior
  without duplicates. The Anki version and disposable profile name were not
  provided.
- Accepted the final Objective 2.9 card set: 13 Basic cards, including nine
  HighYield cards.
- Verified generated output expectations: `Basic.tsv` contains 13 data rows;
  no Cloze, Command, Image, or media output is expected.
- Confirmed that no Objective 2.10 content was created.

## 2026-07-22 - Independent-review fixes

- Replaced the overbroad physical-method comparison and SSD shredding example
  with the source-supported requirement to use a method compatible with
  nonmagnetic storage.
- Removed `full format` as an unsupported alias and consistently retained the
  approved source's `regular format` wording.
- Removed unsupported claims that regulatory or environmental requirements
  determine vendor eligibility, records retention, or documentation; retained
  the supported local-rule and legal-destruction boundary.
- Changed direct-recall card 2.9-B013 from Medium to Easy.
- Added explicit no-card entries for version-specific formatting defaults and
  anecdotal used-drive recovery statistics.
- Updated the review record; blocker-fix verification and the manual Anki smoke
  test remain.

## 2026-07-22 - Objective 2.9 draft authoring

- Added the Core 2 Objective 2.9 study guide covering physical drive
  destruction, erasing and wiping, formatting distinctions, reuse and
  recycling, third-party documentation, and compliance requirements.
- Added concise comparison and selection Basic cards aligned to the official
  `Compare and contrast` wording.
- Used the official CompTIA 220-1202 Objective 2.9 as the scope authority and
  Professor Messer v1.40 p. 45 as the approved secondary validation source.
- Completed a private Core 2 practice-exam gap check without using it for card
  wording, scenarios, explanations, or citations.
- Documented that quick and regular standard formatting have different
  overwrite outcomes instead of treating `standard formatting` as one result.
- Kept named wiping utilities, vendor interfaces, jurisdiction-specific rules,
  and retention periods out of the flashcards.
- Added generated Domain 2 Security and Messer v1.40 source-validation tag
  support for Objective 2.9.
- Generated and verified `Basic.tsv` with 13 data rows; no Cloze, Command,
  Image, or media output is expected.
- Passed validation, build, the 101-test pytest suite, Ruff lint, and Ruff
  format checks.
- Independent content review and manual Anki smoke testing remain before
  acceptance.
