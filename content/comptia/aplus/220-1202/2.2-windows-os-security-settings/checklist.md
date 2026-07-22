# Objective 2.2 completion checklist

**Objective status: ACCEPTED.** Core 2 Objective 2.2 has passed independent
content review, blocker-fix verification, generated-output verification, and
manual Anki smoke testing.

Official context:

```text
Domain 2.0 Security, Objective 2.2: Given a scenario, configure and apply basic
Microsoft Windows OS security settings.
```

Official bullet scope reviewed:

- Defender Antivirus: activate/deactivate and update definitions.
- Firewall: activate/deactivate, port security, and application security.
- Users and groups: local versus Microsoft accounts, standard, administrator,
  Guest, and Power User.
- Log-in OS options: username/password, PIN, fingerprint, facial recognition,
  SSO, and passwordless/Windows Hello.
- NTFS versus share permissions, file and folder attributes, and inheritance.
- Run as administrator versus standard user and User Account Control (UAC).
- BitLocker, BitLocker To Go, and Encrypting File System (EFS).
- Active Directory: joining a domain, log-in scripts, moving objects within
  OUs, home folders, Group Policy, security groups, and folder redirection.

Source-scope decisions:

- The official objective defines the Windows configuration scope and requires
  applied selection. Professor Messer pp. 28–30 validates the settings,
  distinctions, and scenario decisions.
- The private Core 2 practice-exam gap check reinforced UAC, account privilege,
  Guest use, effective NTFS/share access, Group Policy, permissions, and the
  BitLocker/EFS distinction. It supplied no card wording or citations.
- No new secondary source was used.
- The official objective lists “file and folder attributes,” but the approved
  2.2 notes do not define a specific attribute list. The study guide preserves
  the boundary between object properties and access permissions; no attribute
  list card was created pending clearer approved-source support.
- No other source ambiguity remains unresolved.

## Coverage map

| Concept | Source | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- |
| Defender activation/deactivation | CompTIA 2.2; Messer p. 28 | Microsoft Defender Antivirus | 2.2-B001 | Basic | N/A | Self-reviewed |
| Defender definition updates | CompTIA 2.2; Messer p. 28 | Microsoft Defender Antivirus | 2.2-B002 | Basic | N/A | Self-reviewed |
| Firewall activation/deactivation and profiles | CompTIA 2.2; Messer p. 28 | Windows Firewall | 2.2-B003 | Basic | N/A | Self-reviewed |
| Firewall port security | CompTIA 2.2; Messer p. 28 | Windows Firewall | 2.2-B004 | Basic | N/A | Self-reviewed |
| Firewall application security | CompTIA 2.2; Messer p. 28 | Windows Firewall | 2.2-B005 | Basic | N/A | Self-reviewed |
| Local versus Microsoft account | CompTIA 2.2; Messer p. 28 | Users, Groups, and Sign-In | 2.2-B006 | Basic | N/A | Self-reviewed |
| Standard account | CompTIA 2.2; Messer p. 28 | Users, Groups, and Sign-In | 2.2-B007 | Basic | N/A | Self-reviewed |
| Administrator account | CompTIA 2.2; Messer p. 28 | Users, Groups, and Sign-In | 2.2-B008 | Basic | N/A | Self-reviewed |
| Guest account | CompTIA 2.2; Messer p. 28 | Users, Groups, and Sign-In | 2.2-B009 | Basic | N/A | Self-reviewed |
| Power User | CompTIA 2.2; Messer p. 28 | Users, Groups, and Sign-In | 2.2-B010 | Basic | N/A | Self-reviewed |
| Username/password and PIN | CompTIA 2.2; Messer p. 28 | Users, Groups, and Sign-In | 2.2-B011 | Basic | N/A | Self-reviewed |
| Fingerprint and facial recognition | CompTIA 2.2; Messer p. 28 | Users, Groups, and Sign-In | 2.2-B012 | Basic | N/A | Self-reviewed |
| SSO | CompTIA 2.2; Messer p. 28 | Users, Groups, and Sign-In | 2.2-B013 | Basic | N/A | Self-reviewed |
| Passwordless and Windows Hello | CompTIA 2.2; Messer p. 28 | Users, Groups, and Sign-In | 2.2-B014 | Basic | N/A | Self-reviewed |
| NTFS versus share permissions | CompTIA 2.2; Messer p. 29 | NTFS and Share Permissions | 2.2-B015 | Basic | N/A | Self-reviewed |
| Effective permissions and deny | CompTIA 2.2; Messer p. 29 | NTFS and Share Permissions | 2.2-B016 | Basic | N/A | Self-reviewed |
| Permission inheritance | CompTIA 2.2; Messer p. 29 | NTFS and Share Permissions | 2.2-B017 | Basic | N/A | Self-reviewed |
| File and folder attributes | CompTIA 2.2 | NTFS and Share Permissions | None | None | Approved notes do not define an objective-specific attribute list; avoid guessing or trivia until approved support clarifies the intended depth | Self-reviewed |
| Run as administrator versus standard user | CompTIA 2.2; Messer p. 29 | Elevation and User Account Control | 2.2-B018 | Basic | N/A | Self-reviewed |
| UAC | CompTIA 2.2; Messer p. 29 | Elevation and User Account Control | 2.2-B019 | Basic | N/A | Self-reviewed |
| BitLocker | CompTIA 2.2; Messer p. 29 | BitLocker, BitLocker To Go, and EFS | 2.2-B020 | Basic | N/A | Self-reviewed |
| BitLocker To Go | CompTIA 2.2; Messer p. 29 | BitLocker, BitLocker To Go, and EFS | 2.2-B021 | Basic | N/A | Self-reviewed |
| EFS | CompTIA 2.2; Messer p. 29 | BitLocker, BitLocker To Go, and EFS | 2.2-B022 | Basic | N/A | Self-reviewed |
| Active Directory and joining a domain | CompTIA 2.2; Messer p. 29 | Active Directory Administration | 2.2-B023 | Basic | N/A | Self-reviewed |
| Assigning a log-in script | CompTIA 2.2; Messer p. 30 | Active Directory Administration | 2.2-B024 | Basic | N/A | Self-reviewed |
| Organizational units | CompTIA 2.2; Messer p. 30 | Active Directory Administration | 2.2-B025 | Basic | N/A | Self-reviewed |
| Moving objects within OUs | CompTIA 2.2; Messer p. 30 | Active Directory Administration | 2.2-B026 | Basic | N/A | Self-reviewed |
| Assigning home folders | CompTIA 2.2; Messer p. 30 | Active Directory Administration | 2.2-B027 | Basic | N/A | Self-reviewed |
| Applying Group Policy | CompTIA 2.2; Messer p. 30 | Active Directory Administration | 2.2-B028 | Basic | N/A | Self-reviewed |
| Selecting security groups | CompTIA 2.2; Messer p. 30 | Active Directory Administration | 2.2-B029 | Basic | N/A | Self-reviewed |
| Configuring folder redirection | CompTIA 2.2; Messer p. 30 | Active Directory Administration | 2.2-B030 | Basic | N/A | Self-reviewed |

## Objective-specific cautions

- Keep general security-control purposes in Objective 2.1 and workstation
  hardening techniques in Objective 2.7; this objective selects Windows
  security settings.
- Do not turn menu paths into volatile memorization targets.
- Do not imply that disabling Defender or Windows Firewall is a lasting fix;
  temporary isolation must be followed by restoring protection.
- Keep file/share permission layers distinct from Active Directory group and
  OU organization.
- Do not invent a file/folder attribute list without clearer approved-source
  support.

## HighYield review

| Card IDs | Rubric justification | Review status |
| --- | --- | --- |
| 2.2-B001–B005 | Foundational endpoint and network protection configuration | Approved by independent review |
| 2.2-B007–B008, B013–B019 | Common privilege, sign-in, permission, and elevation decisions | Approved by independent review |
| 2.2-B020–B023, B028–B030 | Frequently tested encryption and centralized-management choices | Approved by independent review |

## Research and extraction

- [x] The matching 220-1202 exam version and Objective 2.2 scope are confirmed.
- [x] The official CompTIA objective PDF was used as the primary scope authority.
- [x] Professor Messer v1.40 printed pages 28–30 were used only for approved
      secondary validation and page references.
- [x] The Professor Messer Core 2 practice exam was used only as a private
      secondary gap check after official scope was established.
- [x] Practice-gap concepts useful for active recall are carded.
- [x] No new secondary source was used.
- [x] Concepts were extracted and expressed without copying source language.
- [x] The file/folder-attributes source limitation is documented without
      guessing; no other ambiguity remains unresolved.

## Authoring

- [x] `study-guide.md` is written, sourced, and internally consistent.
- [x] Basic cards use short scenarios and configuration choices aligned to the
      official “Given a scenario” wording.
- [x] Cloze cards were considered; compact recall would duplicate the applied
      Basic targets.
- [x] Command cards were considered; exact command recall belongs to Objective
      1.5 and is not required for these setting choices.
- [x] Image cards were considered; visual recognition is not required to choose
      the listed Windows settings.
- [x] Instructor Notes add a distinction, consequence, or decision boundary.
- [x] Custom tags and stable IDs follow repository rules.
- [x] The one study-guide-only concept has a specific source-support reason.
- [x] `changelog.md` records the draft.

## Review and build

- [x] Independent review and blocker-fix verification confirm accuracy, scope,
      atomicity, wording, redundancy, omissions, and HighYield classifications.
- [x] Original diagrams are not applicable; no image cards were created.
- [x] `.venv/bin/python scripts/validate.py` passes without unexplained warnings.
- [x] `.venv/bin/python scripts/build.py` passes and removes no expected output.
- [x] Generated TSV changes match the Markdown sources: `Basic.tsv` contains 30
      data rows; no Cloze, Command, Image, or media output is expected.
- [x] The 94-test pytest suite and Ruff lint and format checks pass.
- [x] Manual Anki smoke testing passes for the generated Basic file.

## Acceptance record

- Date accepted: 2026-07-22.
- Final card count: 30 Basic cards, including 21 HighYield cards.
- Generated TSV output: `Basic.tsv` contains 30 verified data rows; no Cloze,
  Command, Image, or media output is expected.
- Manual Anki smoke test: User-reported pass on 2026-07-22 for the Basic
  import; headers were not imported as notes, HTML rendered correctly,
  Instructor Notes displayed after reveal, tags imported as Anki metadata,
  Card ID supported update behavior, re-import created no duplicates, and the
  observed count matched 30 Basic notes. The Anki version and disposable
  profile name were not provided.
- Media verification: Not applicable; Objective 2.2 has no Image cards.
- Acceptance decision: Accepted.

## Peer review record

| Reviewer | Date | Result | Required Changes | Approval Status |
| --- | --- | --- | --- | --- |
| Self-review | 2026-07-22 | Draft authored from official Objective 2.2 and Messer pp. 28–30; private practice gap check completed | Independent content review and manual Anki smoke test remain | Needs independent review |
| Independent content review | 2026-07-22 | NO-GO; scope, sources, omissions, card roles, redundancy, generated output, and HighYield choices passed | Give 2.2-B012 an explicit two-answer boundary; recommended changing direct-recall 2.2-B019 to Easy | Changes required; blocker verification remains |
| Blocker-fix verification | 2026-07-22 | GO; B012 now states the two-answer boundary, B019 is Easy, generated output matches isolated regeneration, and no new issues were found | None | Approved; ready for manual Anki smoke test |
| Manual Anki smoke test | 2026-07-22 | User-reported Basic import, rendering, metadata tags, 30-note total, and Card ID re-import/update behavior passed; Anki version/profile not provided | None | Accepted |
