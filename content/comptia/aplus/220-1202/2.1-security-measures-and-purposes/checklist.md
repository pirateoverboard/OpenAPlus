# Objective 2.1 completion checklist

**Objective status: ACCEPTED.** Core 2 Objective 2.1 has passed independent
content review, blocker-fix verification, generated-output verification, and
manual Anki smoke testing.

Official context:

```text
Domain 2.0 Security, Objective 2.1: Summarize various security measures and
their purposes.
```

Official bullet scope reviewed:

- Physical security: bollards, access control vestibules, badge readers, video
  surveillance, alarms, motion sensors, door and equipment locks, guards, and
  fences.
- Physical access security: key fobs, smart cards, mobile digital keys,
  mechanical keys, biometrics, lighting, and magnetometers.
- Logical security: least privilege, Zero Trust, ACLs, MFA and its listed
  methods, SAML, SSO, just-in-time access and PAM, MDM, DLP, IAM, and directory
  services.

Source-scope decisions:

- The official objective defines the control-and-purpose scope. Professor
  Messer pp. 24–27 validates the functions and distinctions.
- The private Core 2 practice-exam gap check reinforced physical-access
  distinctions, least privilege versus Zero Trust, MFA methods, TOTP, SSO,
  just-in-time access, and DLP. It supplied no card wording or citations.
- No new secondary source was used.
- The official PDF prints “Security Assertions Markup Language,” while Messer
  p. 27 uses the standard singular expansion, “Security Assertion Markup
  Language.” Card 2.1-B028 follows the approved Messer wording and records the
  official wording in a Source Note.
- The official PDF prints “Identity access management,” while Messer p. 27
  uses “Identity and Access Management.” Card 2.1-B034 follows the approved
  Messer wording and records the official wording in a Source Note.
- Both wording differences are resolved for this draft; no other source
  ambiguity remains unresolved.

## Coverage map

| Concept | Source | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- |
| Bollards | CompTIA 2.1; Messer p. 24 | Physical Security | 2.1-B001 | Basic | N/A | Self-reviewed |
| Access control vestibule | CompTIA 2.1; Messer p. 24 | Physical Security | 2.1-B002 | Basic | N/A | Self-reviewed |
| Badge reader | CompTIA 2.1; Messer p. 24 | Physical Security | 2.1-B003 | Basic | N/A | Self-reviewed |
| Video surveillance | CompTIA 2.1; Messer p. 24 | Physical Security | 2.1-B004 | Basic | N/A | Self-reviewed |
| Alarm systems and motion sensors | CompTIA 2.1; Messer p. 24 | Physical Security | 2.1-B005 | Basic | N/A | Self-reviewed |
| Door locks | CompTIA 2.1; Messer p. 24 | Physical Security | 2.1-B006 | Basic | N/A | Self-reviewed |
| Equipment locks | CompTIA 2.1; Messer p. 24 | Physical Security | 2.1-B007 | Basic | N/A | Self-reviewed |
| Security guards | CompTIA 2.1; Messer p. 24 | Physical Security | 2.1-B008 | Basic | N/A | Self-reviewed |
| Fences | CompTIA 2.1; Messer p. 24 | Physical Security | 2.1-B009 | Basic | N/A | Self-reviewed |
| Key fobs | CompTIA 2.1; Messer p. 25 | Physical Access Security | 2.1-B010 | Basic | N/A | Self-reviewed |
| Smart cards | CompTIA 2.1; Messer p. 25 | Physical Access Security | 2.1-B011 | Basic | N/A | Self-reviewed |
| Mobile digital keys | CompTIA 2.1; Messer p. 25 | Physical Access Security | 2.1-B012 | Basic | N/A | Self-reviewed |
| Mechanical keys and accountability | CompTIA 2.1; Messer p. 25 | Physical Access Security | 2.1-B013 | Basic | N/A | Self-reviewed |
| Biometrics and replacement risk | CompTIA 2.1; Messer p. 25 | Physical Access Security | 2.1-B014 | Basic | N/A | Self-reviewed |
| Retina scanner | CompTIA 2.1; Messer p. 25 | Physical Access Security | 2.1-B015 | Basic | N/A | Self-reviewed |
| Facial recognition technology | CompTIA 2.1; Messer p. 25 | Physical Access Security | 2.1-B016 | Basic | N/A | Self-reviewed |
| Voice recognition technology | CompTIA 2.1; Messer p. 25 | Physical Access Security | 2.1-B017 | Basic | N/A | Self-reviewed |
| Fingerprint and palm-print scanners | CompTIA 2.1; Messer p. 25 | Physical Access Security | None | None | Names directly identify the measured trait; generic biometric purpose and less-obvious types are carded | Self-reviewed |
| Lighting | CompTIA 2.1; Messer p. 25 | Physical Access Security | 2.1-B018 | Basic | N/A | Self-reviewed |
| Magnetometers | CompTIA 2.1; Messer p. 25 | Physical Access Security | 2.1-B019 | Basic | N/A | Self-reviewed |
| Principle of least privilege | CompTIA 2.1; Messer p. 26 | Least Privilege, Zero Trust, and ACLs | 2.1-B020 | Basic | N/A | Self-reviewed |
| Zero Trust model | CompTIA 2.1; Messer p. 26 | Least Privilege, Zero Trust, and ACLs | 2.1-B021 | Basic | N/A | Self-reviewed |
| Access control lists | CompTIA 2.1; Messer p. 26 | Least Privilege, Zero Trust, and ACLs | 2.1-B022 | Basic | N/A | Self-reviewed |
| Multifactor authentication | CompTIA 2.1; Messer p. 26 | Multifactor Authentication and One-Time Codes | 2.1-B023 | Basic | N/A | Self-reviewed |
| Email verification | CompTIA 2.1; Messer p. 26 | Multifactor Authentication and One-Time Codes | 2.1-B024 | Basic | N/A | Self-reviewed |
| Authenticator applications | CompTIA 2.1; Messer p. 26 | Multifactor Authentication and One-Time Codes | 2.1-B025 | Basic | N/A | Self-reviewed |
| Hardware tokens | CompTIA 2.1; Messer p. 26 | Multifactor Authentication and One-Time Codes | 2.1-B026 | Basic | N/A | Self-reviewed |
| SMS and voice-call delivery | CompTIA 2.1; Messer p. 26 | Multifactor Authentication and One-Time Codes | 2.1-B027 | Basic | N/A | Self-reviewed |
| TOTP | CompTIA 2.1; Messer p. 26 | Multifactor Authentication and One-Time Codes | 2.1-C001 | Cloze | N/A | Self-reviewed |
| OTP | CompTIA 2.1; Messer p. 26 | Multifactor Authentication and One-Time Codes | 2.1-C002 | Cloze | N/A | Self-reviewed |
| SAML | CompTIA 2.1; Messer p. 27 | Federated and Simplified Access | 2.1-B028 | Basic | N/A | Self-reviewed |
| SSO | CompTIA 2.1; Messer p. 27 | Federated and Simplified Access | 2.1-B029 | Basic | N/A | Self-reviewed |
| Just-in-time access | CompTIA 2.1; Messer p. 27 | Privileged and Device Access | 2.1-B030 | Basic | N/A | Self-reviewed |
| PAM | CompTIA 2.1; Messer p. 27 | Privileged and Device Access | 2.1-B031 | Basic | N/A | Self-reviewed |
| MDM | CompTIA 2.1; Messer p. 27 | Privileged and Device Access | 2.1-B032 | Basic | N/A | Self-reviewed |
| DLP | CompTIA 2.1; Messer p. 27 | Data and Identity Controls | 2.1-B033 | Basic | N/A | Self-reviewed |
| IAM | CompTIA 2.1; Messer p. 27 | Data and Identity Controls | 2.1-B034 | Basic | N/A | Self-reviewed |
| Directory services | CompTIA 2.1; Messer p. 27 | Data and Identity Controls | 2.1-B035 | Basic | N/A | Self-reviewed |

## Objective-specific cautions

- Keep security-setting configuration in Objective 2.2 and wireless protocols
  in Objective 2.3; this objective summarizes control purposes.
- Do not turn self-descriptive biometric names into filler cards.
- Do not imply that one factor delivery method is universally secure; state
  the relevant dependency or limitation.
- Keep vendor products, implementation-specific thresholds, and UI paths out
  of the cards.

## HighYield review

| Card IDs | Rubric justification | Review status |
| --- | --- | --- |
| 2.1-B002, B014, B020–B023 | Foundational access-control and authentication distinctions | Approved by independent review |
| 2.1-B025, B027, C001, C002 | Frequently tested one-time-code and MFA delivery distinctions | Approved by independent review |
| 2.1-B029–B035 | Central logical-security, privileged-access, data, and identity controls | Approved by independent review |

## Research and extraction

- [x] The matching 220-1202 exam version and Objective 2.1 scope are confirmed.
- [x] The official CompTIA objective PDF was used as the primary scope authority.
- [x] Professor Messer v1.40 printed pages 24–27 were used only for approved
      secondary validation and page references.
- [x] The Professor Messer Core 2 practice exam was used only as a private
      secondary gap check after official scope was established.
- [x] Practice-gap concepts useful for active recall are carded.
- [x] No new secondary source was used.
- [x] Concepts were extracted and expressed without copying source language.
- [x] Source wording differences for SAML and IAM were documented and resolved;
      no ambiguity remains unresolved.

## Authoring

- [x] `study-guide.md` is written, sourced, and internally consistent.
- [x] Basic cards summarize purposes and use short distinctions or applications.
- [x] Cloze cards are limited to the compact TOTP and OTP facts.
- [x] Command cards were considered and are not applicable.
- [x] Image cards were considered; visual recognition is not required to
      understand the listed control purposes.
- [x] Instructor Notes add a distinction, consequence, or decision boundary.
- [x] Custom tags and stable IDs follow repository rules.
- [x] Omitted biometric subtypes have a specific no-card reason.
- [x] `changelog.md` records the draft.

## Review and build

- [x] Independent review and blocker verification confirm accuracy, scope, atomicity, wording,
      redundancy, omissions, and HighYield classifications.
- [x] Original diagrams are not applicable; no image cards were created.
- [x] `.venv/bin/python scripts/validate.py` passes without unexplained warnings.
- [x] `.venv/bin/python scripts/build.py` passes and removes no expected output.
- [x] Generated TSV changes match the Markdown sources: `Basic.tsv` contains 35
      data rows and `Cloze.tsv` contains two; no Command, Image, or media output
      is expected.
- [x] The 93-test pytest suite and Ruff lint and format checks pass.
- [x] Manual Anki smoke testing passes for generated Basic and Cloze files.

## Acceptance record

- Date accepted: 2026-07-14.
- Final card count: 35 Basic cards and two Cloze cards, including 17 HighYield
  cards.
- Generated TSV output: `Basic.tsv` contains 35 verified data rows and
  `Cloze.tsv` contains two; no Command, Image, or media output is expected.
- Manual Anki smoke test: User-reported pass on 2026-07-14 for the Basic and
  Cloze imports; headers were not imported as notes, HTML and Cloze content
  rendered correctly, Instructor Notes displayed after reveal, tags imported
  as Anki metadata, Card ID supported update behavior, re-import created no
  duplicates, and observed counts matched 35 Basic and two Cloze notes. The
  Anki version and disposable profile name were not provided.
- Media verification: Not applicable; Objective 2.1 has no Image cards.
- Acceptance decision: Accepted.

## Peer review record

| Reviewer | Date | Result | Required Changes | Approval Status |
| --- | --- | --- | --- | --- |
| Self-review | 2026-07-14 | Draft authored from official Objective 2.1 and Messer pp. 24–27; private practice gap check completed | Independent content review and manual Anki smoke test remain | Needs independent review |
| Independent content review | 2026-07-14 | NO-GO; scope, coverage, card roles, omissions, generated output, and HighYield choices passed | Remove unsupported ACL ordering; document and resolve SAML and IAM wording differences | Changes required; blocker verification remains |
| Blocker-fix verification | 2026-07-14 | GO; all required fixes passed, generated TSVs matched isolated regeneration, and no new issues or redundancy were found | None | Approved; ready for manual Anki smoke test |
| Manual Anki smoke test | 2026-07-14 | User-reported Basic and Cloze import, rendering, metadata tags, 37-note total, and Card ID re-import/update behavior passed; Anki version/profile not provided | None | Accepted |
