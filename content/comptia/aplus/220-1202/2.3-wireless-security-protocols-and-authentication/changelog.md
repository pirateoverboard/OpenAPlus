# Changelog

## 2026-07-22 - Acceptance

- Recorded the user-reported passing manual Anki smoke test for the Objective
  2.3 Basic and Cloze imports, including headers, rendered HTML and Cloze
  content, Instructor Notes, metadata tags, the 14-note total, and Card ID
  re-import/update behavior without duplicates. The Anki version and
  disposable profile name were not provided.
- Accepted the final Objective 2.3 card set: 10 Basic and four Cloze cards,
  including 11 HighYield cards.
- Verified generated output expectations: `Basic.tsv` contains 10 data rows
  and `Cloze.tsv` contains four; no Command, Image, or media output is expected.
- Confirmed that no Objective 2.4 content was created.

## 2026-07-22 - Independent-review fixes

- Removed 2.3-B006 and the related frequency, range, and power-consumption
  claims because the approved notes did not independently validate the private
  practice-gap distinction.
- Recorded that radio-characteristics claims remain omitted unless an approved
  source supports them; the practice exam was not used as card content or a
  citation.
- Reworded 2.3-B004 and 2.3-B009 to identify the Objective 2.3 answer boundary.
- Recorded the independent-review NO-GO and blocker-verification GO; official
  coverage, card roles, copyright safety, omissions, and HighYield choices
  passed review.
- Regenerated and verified `Basic.tsv` with 10 data rows and `Cloze.tsv` with
  four against an isolated regeneration.
- Passed validation, build, the 95-test pytest suite, Ruff lint, and Ruff format
  checks after the fixes.
- Objective 2.3 is ready for the manual Anki smoke test.

## 2026-07-22 - Objective 2.3 draft authoring

- Added the Core 2 Objective 2.3 study guide comparing WPA2, WPA3, TKIP, AES,
  RADIUS, TACACS+, Kerberos, and multifactor authentication.
- Added 11 Basic comparison/application cards and four Cloze acronym cards
  aligned to the official `Compare and contrast` wording.
- Used the official CompTIA 220-1202 Objective 2.3 as the scope authority and
  Professor Messer v1.40 pp. 30–32 as the approved secondary validation source.
- Completed a private Core 2 practice-exam gap check without using it for card
  wording, scenarios, or citations.
- Recorded why historical dates, message-integrity acronym recall, and variable
  authentication-cost examples remain study-guide-only.
- Added generated Domain 2 Security and Messer v1.40 source-validation tag
  support for Objective 2.3.
- Generated and verified `Basic.tsv` with 11 data rows and `Cloze.tsv` with
  four; no Command, Image, or media output is expected.
- Passed validation, build, the 95-test pytest suite, Ruff lint, and Ruff format
  checks.
- Independent review and manual Anki smoke testing remain before acceptance.
