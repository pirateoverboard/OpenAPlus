# Changelog

## 2026-07-22 - Acceptance

- Recorded the blocker-fix verification GO with all four independent-review
  findings resolved and no new issues.
- Recorded the user-reported passing manual Anki smoke test for the Objective
  2.11 Basic import, including headers, rendered HTML, Instructor Notes,
  metadata tags, the 17-note total, and Card ID re-import/update behavior
  without duplicates. The Anki version and disposable profile name were not
  provided.
- Accepted the final Objective 2.11 card set: 17 Basic cards, including 10
  HighYield cards.
- Verified generated output expectations: `Basic.tsv` contains 17 data rows;
  no Cloze, Command, Image, or media output is expected.
- Confirmed that no Objective 3.1 or other future-objective changes were made.

## 2026-07-22 - Independent-review fixes

- Rewrote 2.11-B008 as an original wrong-clock configuration scenario while
  retaining the approved certificate-validity learning target.
- Rewrote 2.11-B016 around a policy requiring DNS lookups over encrypted HTTPS
  transport, removing the practice-adjacent packet-capture scenario.
- Limited 2.11-B005 to the source-supported browser feature-management action
  of disabling an untrusted extension.
- Removed unsupported ad-tracking and site-compatibility claims from 2.11-B014
  and the study guide while retaining the approved ad-blocking behavior,
  recognition limit, availability caveat, and security-level control.
- Rewrapped the 2.11-B001 answer for source readability.
- Regenerated the 17-row `Basic.tsv` and passed validation, build, all 103
  tests, Ruff lint, and Ruff format checks after the fixes.
- Recorded the independent-review NO-GO and author fix pass; blocker-fix
  verification remains before the objective can proceed to manual Anki smoke
  testing.

## 2026-07-22 - Objective 2.11 draft authoring

- Added the Core 2 Objective 2.11 study guide covering browser software trust,
  integrity checks, patching, add-ons, password management, certificates,
  privacy settings, proxies, secure DNS, and feature management.
- Added 17 concise applied Basic cards aligned to the official
  `Given a scenario` wording.
- Used the official CompTIA 220-1202 Objective 2.11 as the scope authority and
  Professor Messer v1.40 pp. 47–48 as the approved secondary validation source.
- Completed a private Core 2 practice-exam gap check without using it for card
  wording, scenarios, explanations, or citations.
- Kept malware-removal procedures, enterprise proxy architecture,
  vendor-specific interface paths, and volatile product details outside the
  card set.
- Added generated Domain 2 Security and Messer v1.40 source-validation tag
  support for Objective 2.11.
- Generated and verified `Basic.tsv` with 17 data rows; no Cloze, Command,
  Image, or media output is expected.
- Passed validation, build, the 103-test pytest suite, Ruff lint, and Ruff
  format checks.
- Independent content review and any required manual Anki smoke testing remain
  before acceptance.
