# Objective 2.7 completion checklist

**Objective status: ACCEPTED.** Core 2 Objective 2.7 has passed independent
content review, generated-output verification, and manual Anki smoke testing.

Official context:

```text
Domain 2.0 Security, Objective 2.7: Given a scenario, apply workstation
security options and hardening techniques.
```

Official bullet scope reviewed:

1. Data-at-rest encryption.
2. Password considerations: length, character types, uniqueness, complexity,
   and expiration.
3. BIOS/UEFI passwords.
4. End-user best practices: screensaver locks, logging off when not in use,
   securing critical hardware, securing PII and passwords, and using password
   managers.
5. Account management: restricting user permissions and log-in times,
   disabling the guest account, failed-attempt lockout, timeout/screen lock,
   and account expiration dates.
6. Change the default administrator user account and password.
7. Disable AutoRun.
8. Disable unused services.

Source-scope decisions:

- The official objective defines the workstation-hardening scope and the
  scenario-based learner task. Professor Messer p. 43 validates the control
  purposes, distinctions, and page reference.
- The cards ask the learner to select or distinguish a control in a short
  situation rather than reproduce the official bullet list.
- Password expiration and account expiration remain separate because the first
  changes a credential and the second ends use of an account.
- Screensaver/timeout locks and logging off remain separate because a lock
  preserves a session for return while logoff ends it.
- The private Core 2 practice-exam gap check reinforced data-at-rest
  encryption, least privilege, log-in time restrictions, screensaver locks,
  guest-account disabling, and password complexity. No published wording,
  scenario, explanation, or citation was taken from it.
- No new secondary source was used, and no source ambiguity remains unresolved.

## Coverage map

| Concept | Source | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- |
| Data-at-rest encryption | CompTIA 2.7; Messer p. 43 | Protect Data at Rest | 2.7-B001 | Basic | N/A | Self-reviewed |
| Encryption recovery-key backup | Messer p. 43; supports CompTIA 2.7 | Protect Data at Rest | None | None | Important implementation context, but not a distinct official retrieval target | Self-reviewed |
| Password length | CompTIA 2.7; Messer p. 43 | Build a Deliberate Password Policy | 2.7-B002 | Basic | N/A | Self-reviewed |
| Password character types and complexity | CompTIA 2.7; Messer p. 43 | Build a Deliberate Password Policy | 2.7-B003 | Basic | N/A; one scenario tests their related role without duplicating it | Self-reviewed |
| Password uniqueness | CompTIA 2.7; Messer p. 43 | Build a Deliberate Password Policy | 2.7-B004 | Basic | N/A | Self-reviewed |
| Password expiration | CompTIA 2.7; Messer p. 43 | Build a Deliberate Password Policy | 2.7-B005 | Basic | N/A | Self-reviewed |
| BIOS/UEFI supervisor or administrator password | CompTIA 2.7; Messer p. 43 | Protect Firmware Settings and Startup | 2.7-B006 | Basic | N/A | Self-reviewed |
| BIOS/UEFI user password | CompTIA 2.7; Messer p. 43 | Protect Firmware Settings and Startup | 2.7-B007 | Basic | N/A | Self-reviewed |
| Screensaver and timeout/screen locks | CompTIA 2.7; Messer p. 43 | Use Safe End-User Practices; Manage Accounts Around Their Purpose | 2.7-B008 | Basic | N/A; both bullets share the same unattended-session decision | Self-reviewed |
| Log off when not in use | CompTIA 2.7; Messer p. 43 | Use Safe End-User Practices | 2.7-B009 | Basic | N/A | Self-reviewed |
| Secure critical hardware | CompTIA 2.7; Messer p. 43 | Use Safe End-User Practices | 2.7-B010 | Basic | N/A | Self-reviewed |
| Secure PII and passwords | CompTIA 2.7; Messer p. 43 | Use Safe End-User Practices | 2.7-B011, 2.7-C001 | Basic, Cloze | N/A; cards test protection selection and acronym recall | Self-reviewed |
| Password managers | CompTIA 2.7; Messer p. 43 | Build a Deliberate Password Policy | 2.7-B012 | Basic | N/A | Self-reviewed |
| Restrict user permissions | CompTIA 2.7; Messer p. 43 | Manage Accounts Around Their Purpose | 2.7-B013 | Basic | N/A | Self-reviewed |
| Restrict log-in times | CompTIA 2.7; Messer p. 43 | Manage Accounts Around Their Purpose | 2.7-B014 | Basic | N/A | Self-reviewed |
| Disable guest account | CompTIA 2.7; Messer p. 43 | Manage Accounts Around Their Purpose | 2.7-B015 | Basic | N/A | Self-reviewed |
| Failed-attempt lockout | CompTIA 2.7; Messer p. 43 | Manage Accounts Around Their Purpose | 2.7-B016 | Basic | N/A | Self-reviewed |
| Account expiration dates | CompTIA 2.7; Messer p. 43 | Manage Accounts Around Their Purpose | 2.7-B017 | Basic | N/A | Self-reviewed |
| Change default administrator account and password | CompTIA 2.7; Messer p. 43 | Remove Defaults and Unneeded Paths | 2.7-B018 | Basic | N/A | Self-reviewed |
| Disable AutoRun | CompTIA 2.7; Messer p. 43 | Remove Defaults and Unneeded Paths | 2.7-B019 | Basic | N/A | Self-reviewed |
| Disable unused services | CompTIA 2.7; Messer p. 43 | Remove Defaults and Unneeded Paths | 2.7-B020 | Basic | N/A | Self-reviewed |
| Exact password lengths and rotation intervals | Messer p. 43; supports CompTIA 2.7 | Build a Deliberate Password Policy | None | None | Policies vary; the stable learning target is the purpose of each consideration | Self-reviewed |
| Product-specific encryption tools and firmware UI paths | Messer p. 43; supports CompTIA 2.7 | Protect Data at Rest; Protect Firmware Settings and Startup | None | None | Implementation-specific details are not required by the official objective | Self-reviewed |
| Individual service names to disable | CompTIA 2.7; Messer p. 43 | Remove Defaults and Unneeded Paths | None | None | A service is disabled only after confirming it is unused; no universal list is source-supported | Self-reviewed |

## Objective-specific cautions

- Do not treat a login or firmware password as data-at-rest encryption.
- Do not merge password expiration with account expiration.
- Do not merge a temporary screen lock with logging off a completed session.
- Do not prescribe universal password lengths, rotation schedules, login hours,
  lockout thresholds, or timeout values when the sources do not establish them.
- Do not disable an unidentified service until its workstation purpose and
  dependencies are understood.
- Do not pull mobile-device controls from Objective 2.8 into this workstation
  objective.

## HighYield review

| Card IDs | Rubric justification | Review status |
| --- | --- | --- |
| 2.7-B001–B004 | Central data-protection and password-policy decisions | Author justification recorded; independent review pending |
| 2.7-B008, 2.7-B012–B013, 2.7-B015–B016, 2.7-B018–B020 | Common workstation exposure, account-control, default, and attack-surface decisions | Author justification recorded; independent review pending |
| 2.7-C001 | PII is a foundational security acronym used throughout the exam | Author justification recorded; independent review pending |

## Research and extraction

- [x] The matching 220-1202 exam version and Objective 2.7 scope are confirmed.
- [x] The official CompTIA objective PDF was used as the primary scope authority.
- [x] Professor Messer v1.40 printed page 43 was used only for approved
      secondary validation and page references.
- [x] The Professor Messer Core 2 practice exam was used only as a private
      secondary gap check after official scope was established.
- [x] Practice-gap concepts useful for active recall are carded.
- [x] No new secondary source was used.
- [x] Concepts were extracted and expressed without copying source language.
- [x] No unresolved source ambiguity was found.

## Authoring

- [x] `study-guide.md` is written, sourced, and internally consistent.
- [x] Basic cards emphasize short control-selection and distinction scenarios
      in line with the official `Given a scenario` wording.
- [x] The Cloze card is limited to compact acronym expansion and does not
      duplicate a Basic-card target.
- [x] Command cards were considered and are not applicable.
- [x] Image cards were considered; visual recognition does not improve this
      policy-and-control objective.
- [x] Instructor Notes add a control boundary, purpose, or distinction.
- [x] Custom tags and stable IDs follow repository rules.
- [x] Study-guide-only concepts have specific no-card reasons.
- [x] `changelog.md` records the draft.

## Review and build

- [x] Independent review confirms accuracy, scope, atomicity, wording,
      redundancy, omissions, and HighYield classifications.
- [x] Original diagrams are not applicable; no image cards were created.
- [x] `.venv/bin/python scripts/validate.py` passes without unexplained warnings.
- [x] `.venv/bin/python scripts/build.py` passes and removes no expected output.
- [x] Generated TSV changes match the Markdown sources: `Basic.tsv` contains 20
      data rows and `Cloze.tsv` contains one; no Command, Image, or media output
      is expected.
- [x] The 99-test pytest suite and Ruff lint and format checks pass.
- [x] Manual Anki smoke testing passes for generated Basic and Cloze files.

## Acceptance record

- Date accepted: 2026-07-22.
- Final card count: 20 Basic cards and one Cloze card, including 13 HighYield
  cards.
- Generated TSV output: `Basic.tsv` contains 20 verified data rows and
  `Cloze.tsv` contains one; no Command, Image, or media output is expected.
- Manual Anki smoke test: User-reported pass on 2026-07-22 for the Basic and
  Cloze imports; headers were not imported as notes, HTML and Cloze content
  rendered correctly, Instructor Notes displayed after reveal, tags imported
  as Anki metadata, Card ID supported update behavior, re-import created no
  duplicates, and observed counts matched 20 Basic and one Cloze note. The
  Anki version and disposable profile name were not provided.
- Media verification: Not applicable; Objective 2.7 has no Image cards.
- Acceptance decision: Accepted.

## Peer review record

| Reviewer | Date | Result | Required Changes | Approval Status |
| --- | --- | --- | --- | --- |
| Self-review | 2026-07-22 | Draft authored from official Objective 2.7 and Messer p. 43; private practice gap check completed | Independent content review and manual Anki smoke test remain | Needs independent review |
| Independent content review | 2026-07-22 | GO; scope, source fidelity, coverage, omissions, card roles, redundancy, difficulty, HighYield classifications, and generated output passed | None | Approved; ready for manual Anki smoke test |
| Manual Anki smoke test | 2026-07-22 | User-reported Basic and Cloze import, rendering, metadata tags, 21-note total, and Card ID re-import/update behavior passed; Anki version/profile not provided | None | Accepted |
