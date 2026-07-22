# Changelog

## 2026-07-22 - Acceptance

- Recorded the user-reported passing manual Anki smoke test for the Objective
  2.5 Basic and Cloze imports, including headers, rendered HTML and Cloze
  content, Instructor Notes, metadata tags, the 30-note total, and Card ID
  re-import/update behavior without duplicates. The Anki version and
  disposable profile name were not provided.
- Accepted the final Objective 2.5 card set: 24 Basic and six Cloze cards,
  including 23 HighYield cards.
- Verified generated output expectations: `Basic.tsv` contains 24 data rows and
  `Cloze.tsv` contains six; no Command, Image, or media output is expected.
- Recorded the blocker-fix verification GO for the source-fidelity and
  difficulty changes.
- Confirmed that no Objective 2.6 content was created.

## 2026-07-22 - Independent-review fixes

- Reworded zero-day coverage in the study guide and 2.5-B012 to match the
  approved source's unknown/unpublished vulnerability boundary and removed the
  unsupported behavior-monitoring recommendation.
- Removed the unsupported online rate-limit reference while retaining the
  source-backed account-lockout distinction.
- Changed 2.5-B002 and 2.5-B003 from Easy to Medium because they apply phishing
  channel recognition in short scenarios.
- Blocker-fix verification and manual Anki smoke testing remain before
  acceptance.

## 2026-07-22 - Objective 2.5 draft authoring

- Added the Core 2 Objective 2.5 study guide covering the official social
  engineering attacks, threats, and vulnerability conditions.
- Added comparison and recognition cards aligned to the official `Compare and
  contrast` wording, with separate Cloze cards only for useful acronym
  expansion.
- Used the official CompTIA 220-1202 Objective 2.5 as the scope authority and
  Professor Messer v1.40 pp. 35–41 as the approved secondary validation source.
- Completed a private Core 2 practice-exam gap check without using it for card
  wording, scenarios, explanations, or citations.
- Kept product names, historical incidents, exact vendor schedules, and
  implementation-specific examples out of the flashcards.
- Added generated Domain 2 Security and Messer v1.40 source-validation tag
  support for Objective 2.5.
- Generated and verified `Basic.tsv` with 24 data rows and `Cloze.tsv` with six;
  no Command, Image, or media output is expected.
- Passed validation, build, the 97-test pytest suite, Ruff lint, and Ruff format
  checks.
- Independent content review and manual Anki smoke testing remain before
  acceptance.
