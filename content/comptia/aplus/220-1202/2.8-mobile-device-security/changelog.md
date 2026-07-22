# Changelog

## 2026-07-22 - Acceptance

- Recorded the blocker-fix verification GO with all three independent-review
  findings resolved and no new issues.
- Recorded the user-reported passing manual Anki smoke test for the Objective
  2.8 Basic and Cloze imports, including headers, rendered HTML and Cloze
  content, Instructor Notes, metadata tags, the 16-note total, and Card ID
  re-import/update behavior without duplicates. The Anki version and
  disposable profile name were not provided.
- Accepted the final Objective 2.8 card set: 15 Basic cards and one Cloze card,
  including 14 HighYield cards.
- Verified generated output expectations: `Basic.tsv` contains 15 data rows
  and `Cloze.tsv` contains one; no Command, Image, or media output is expected.
- Confirmed that no Objective 2.9 content was created.

## 2026-07-22 - Independent-review fixes

- Reworded 2.8-B015 to test profile security requirements without naming the
  configuration-profile answer on the front or duplicating 2.8-B004's
  scalable-deployment target.
- Replaced the unsupported error-rate claim in 2.8-B004 with the
  source-supported benefit of easier, consistent management.
- Changed direct-recall card 2.8-B008 from Medium to Easy under the documented
  difficulty rubric.
- Updated the coverage map and review record; blocker-fix verification and the
  manual Anki smoke test remain.

## 2026-07-22 - Objective 2.8 draft authoring

- Added the Core 2 Objective 2.8 study guide covering mobile-device hardening,
  profiles and MDM, patching, endpoint software, lost-device controls,
  backups, failed-attempt restrictions, and ownership policies.
- Added concise scenario-driven Basic cards aligned to the official `Given a
  scenario` wording, plus one Cloze card for the MDM acronym.
- Used the official CompTIA 220-1202 Objective 2.8 as the scope authority and
  Professor Messer v1.40 p. 44 as the approved secondary validation source.
- Completed a private Core 2 practice-exam gap check without using it for card
  wording, scenarios, explanations, or citations.
- Documented the pattern/swipe wording ambiguity and avoided an unsupported
  comparison card.
- Kept exact failed-attempt thresholds, product names, OS-version details,
  mobile-firewall behavior, and UI paths out of the flashcards.
- Added generated Domain 2 Security and Messer v1.40 source-validation tag
  support for Objective 2.8.
- Generated and verified `Basic.tsv` with 15 data rows and `Cloze.tsv` with one;
  no Command, Image, or media output is expected.
- Passed validation, build, the 100-test pytest suite, Ruff lint, and Ruff
  format checks.
- Independent content review and manual Anki smoke testing remain before
  acceptance.
