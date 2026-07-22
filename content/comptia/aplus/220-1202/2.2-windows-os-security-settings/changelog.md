# Changelog

## 2026-07-22 - Acceptance

- Recorded the user-reported passing manual Anki smoke test for the Objective
  2.2 Basic import, including headers, rendered HTML, Instructor Notes,
  metadata tags, the 30-note total, and Card ID re-import/update behavior
  without duplicates. The Anki version and disposable profile name were not
  provided.
- Accepted the final Objective 2.2 card set: 30 Basic cards, including 21
  HighYield cards.
- Verified generated output expectations: `Basic.tsv` contains 30 data rows;
  no Cloze, Command, Image, or media output is expected.
- Confirmed that no Objective 2.3 content was created.

## 2026-07-22 - Independent-review fixes

- Reworded 2.2-B012 to state explicitly that the learner must identify the two
  biometric sign-in options, resolving the independent review's only blocker.
- Changed direct-recall UAC card 2.2-B019 from Medium to Easy as recommended.
- Recorded the independent-review NO-GO and blocker-verification GO; scope,
  sources, omissions, card roles, redundancy, and HighYield classifications
  passed review.
- Regenerated `Basic.tsv` and verified its 30 rows against an isolated
  regeneration.
- Passed validation, build, the 94-test pytest suite, Ruff lint, and Ruff format
  checks after the fixes.
- Objective 2.2 is ready for the manual Anki smoke test.

## 2026-07-22 - Objective 2.2 draft authoring

- Added the Core 2 Objective 2.2 study guide for Defender Antivirus, Windows
  Firewall, accounts and sign-in, permissions, elevation, encryption, and
  Active Directory administration.
- Added 30 Basic cards aligned to the official `Given a scenario` wording and
  focused on choosing or applying one Windows security setting.
- Used the official CompTIA 220-1202 Objective 2.2 as the scope authority and
  Professor Messer v1.40 pp. 28–30 as the approved secondary validation source.
- Completed a private Core 2 practice-exam gap check without using it for card
  wording, scenarios, or citations.
- Documented that the official file-and-folder-attributes bullet lacks a
  specific attribute list in the approved 2.2 notes, so no unsupported list
  card was created.
- Added generated Domain 2 Security and Messer v1.40 source-validation tag
  support for Objective 2.2.
- Generated and verified `Basic.tsv` with 30 data rows; no Cloze, Command,
  Image, or media output is expected.
- Passed validation, build, the 94-test pytest suite, Ruff lint, and Ruff format
  checks.
- Independent review and manual Anki smoke testing remain before acceptance.
