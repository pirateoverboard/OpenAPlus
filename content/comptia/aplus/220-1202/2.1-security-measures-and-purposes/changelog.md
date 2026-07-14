# Changelog

## 2026-07-14 - Acceptance

- Recorded the user-reported passing manual Anki smoke test for the Objective
  2.1 Basic and Cloze imports, including headers, rendered HTML and Cloze
  content, Instructor Notes, metadata tags, the 37-note total, and Card ID
  re-import/update behavior without duplicates. The Anki version and disposable
  profile name were not provided.
- Recorded the blocker-verification GO with no remaining blockers or new
  issues and approval of the HighYield and omitted-concept decisions.
- Accepted the final Objective 2.1 card set: 35 Basic and two Cloze cards,
  including 17 HighYield cards.
- Verified generated output expectations: `Basic.tsv` contains 35 data rows and
  `Cloze.tsv` contains two; no Command, Image, or media output is expected.
- Confirmed that no Objective 2.2 content was created.

## 2026-07-14 - Independent-review fixes

- Removed the unsupported claim that the ACL rules tested by card 2.1-B022 are
  ordered; the card now tests only the cited permit/deny function.
- Documented the official-objective and Messer wording differences for SAML and
  IAM, recorded the resolution in the checklist, and added Source Notes to
  cards 2.1-B028 and 2.1-B034.
- Recorded the independent-review NO-GO and its required fixes; blocker
  verification and manual Anki smoke testing remain.

## 2026-07-14 - Objective 2.1 draft authoring

- Added the Core 2 Objective 2.1 study guide for physical controls, physical
  access, authentication, privileged access, data protection, and identity
  controls.
- Added 35 Basic cards and two Cloze cards aligned to the official `Summarize`
  wording and focused on each measure's purpose or a useful distinction.
- Used the official CompTIA 220-1202 Objective 2.1 as the scope authority and
  Professor Messer v1.40 pp. 24–27 as the approved secondary validation source.
- Completed a private Core 2 practice-exam gap check without using it for card
  wording, scenarios, or citations.
- Recorded why separate fingerprint and palm-print cards would be low-value and
  redundant with the broader biometric coverage.
- Added generated Domain 2 Security and Messer v1.40 source-validation tag
  support for the objective.
- Generated and verified `Basic.tsv` with 35 data rows and `Cloze.tsv` with two
  data rows; no Command, Image, or media output is expected.
- Passed validation, build, the 93-test pytest suite, Ruff lint, and Ruff format
  checks.
- Independent review and manual Anki smoke testing remain before acceptance.
