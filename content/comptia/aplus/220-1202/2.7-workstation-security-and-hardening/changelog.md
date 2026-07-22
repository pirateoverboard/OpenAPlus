# Changelog

## 2026-07-22 - Acceptance

- Recorded the independent-review GO with no required fixes or recommended
  improvements.
- Recorded the user-reported passing manual Anki smoke test for the Objective
  2.7 Basic and Cloze imports, including headers, rendered HTML and Cloze
  content, Instructor Notes, metadata tags, the 21-note total, and Card ID
  re-import/update behavior without duplicates. The Anki version and
  disposable profile name were not provided.
- Accepted the final Objective 2.7 card set: 20 Basic cards and one Cloze card,
  including 13 HighYield cards.
- Verified generated output expectations: `Basic.tsv` contains 20 data rows and
  `Cloze.tsv` contains one; no Command, Image, or media output is expected.
- Confirmed that no Objective 2.8 content was created.

## 2026-07-22 - Objective 2.7 draft authoring

- Added the Core 2 Objective 2.7 study guide covering workstation security
  options and hardening techniques.
- Added concise scenario-driven Basic cards aligned to the official `Given a
  scenario` wording, plus one Cloze card for the PII acronym.
- Used the official CompTIA 220-1202 Objective 2.7 as the scope authority and
  Professor Messer v1.40 p. 43 as the approved secondary validation source.
- Completed a private Core 2 practice-exam gap check without using it for card
  wording, scenarios, explanations, or citations.
- Kept exact password lengths and rotation intervals, product-specific
  encryption tools, firmware-navigation steps, and service names out of the
  flashcards because the objective does not establish universal values.
- Added generated Domain 2 Security and Messer v1.40 source-validation tag
  support for Objective 2.7.
- Generated and verified `Basic.tsv` with 20 data rows and `Cloze.tsv` with one;
  no Command, Image, or media output is expected.
- Passed validation, build, the 99-test pytest suite, Ruff lint, and Ruff format
  checks.
- Independent content review and manual Anki smoke testing remain before
  acceptance.
