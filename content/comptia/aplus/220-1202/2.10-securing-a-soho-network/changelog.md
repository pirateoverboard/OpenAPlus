# Changelog

## 2026-07-22 - Acceptance

- Recorded the blocker-fix verification GO with both independent-review
  findings resolved and no new issues.
- Recorded the user-reported passing manual Anki smoke test for the Objective
  2.10 Basic import, including headers, rendered HTML, Instructor Notes,
  metadata tags, the 14-note total, and Card ID re-import/update behavior
  without duplicates. The Anki version and disposable profile name were not
  provided.
- Accepted the final Objective 2.10 card set: 14 Basic cards, including 10
  HighYield cards.
- Verified generated output expectations: `Basic.tsv` contains 14 data rows;
  no Cloze, Command, Image, or media output is expected.
- Confirmed that no Objective 2.11 changes were made.

## 2026-07-22 - Independent-review fixes

- Removed unsupported `first` priority wording from 2.10-B001 so the prompt
  tests the sourced security-setting decision without implying an order the
  approved sources do not establish.
- Changed applied scenario card 2.10-B009 from Easy to Medium under the
  repository difficulty rubric.
- Regenerated `Basic.tsv` and passed validation, build, all 102 tests, Ruff
  lint, and Ruff format checks after the fixes.
- Recorded the independent-review NO-GO and author fix pass; blocker-fix
  verification remains.

## 2026-07-22 - Objective 2.10 draft authoring

- Added the Core 2 Objective 2.10 study guide covering router management,
  filtering, firmware, physical security, automatic exposure, wireless
  settings, unused ports, and port forwarding.
- Added 14 concise applied Basic cards aligned to the official
  `Given a scenario` wording.
- Used the official CompTIA 220-1202 Objective 2.10 as the scope authority and
  Professor Messer v1.40 pp. 46–47 as the approved secondary validation source.
- Completed a private Core 2 practice-exam gap check without using it for card
  wording, scenarios, explanations, or citations.
- Kept wireless-protocol history, detailed enterprise authentication,
  vendor-specific interfaces, and volatile procedures out of the card set.
- Added generated Domain 2 Security and Messer v1.40 source-validation tag
  support for Objective 2.10.
- Generated and verified `Basic.tsv` with 14 data rows; no Cloze, Command,
  Image, or media output is expected.
- Passed validation, build, the 102-test pytest suite, Ruff lint, and Ruff
  format checks.
- Independent content review and any required manual Anki smoke testing remain
  before acceptance.
