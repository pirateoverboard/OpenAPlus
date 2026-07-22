# Objective 2.3 completion checklist

**Objective status: ACCEPTED.** Core 2 Objective 2.3 has passed independent
content review, blocker-fix verification, generated-output verification, and
manual Anki smoke testing.

Official context:

```text
Domain 2.0 Security, Objective 2.3: Compare and contrast wireless security
protocols and authentication methods.
```

Official bullet scope reviewed:

- Protocols and encryption: Wi-Fi Protected Access 2 (WPA2), WPA3, Temporal
  Key Integrity Protocol (TKIP), and Advanced Encryption Standard (AES).
- Authentication: Remote Authentication Dial-in User Service (RADIUS),
  Terminal Access Controller Access-Control System Plus (TACACS+), Kerberos,
  and multifactor authentication.

Source-scope decisions:

- The official objective defines the comparison scope. Professor Messer pp.
  30–32 validates the protocol relationships, authentication roles, and useful
  distinctions.
- Personal/PSK and Enterprise/802.1X modes are included only as supporting
  context for comparing shared wireless access with RADIUS-backed individual
  authentication.
- The private Core 2 practice-exam gap check reinforced encryption versus
  authentication, WPA3 security improvements, centralized RADIUS
  authentication, and MFA as an additional factor. It supplied no card wording
  or citations. A radio-characteristics distinction surfaced by the gap check
  was not retained because the approved notes did not independently support
  that detail.
- No new secondary source was used, and no source ambiguity remains unresolved.

## Coverage map

| Concept | Source | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- |
| Wireless encryption versus authentication | CompTIA 2.3; Messer p. 30 | Encryption and Authentication | 2.3-B001 | Basic | N/A | Self-reviewed |
| WPA2 and AES | CompTIA 2.3; Messer p. 31 | WPA2, WPA3, TKIP, and AES | 2.3-B002 | Basic | N/A | Self-reviewed |
| WPA3 versus WPA2 | CompTIA 2.3; Messer p. 31 | WPA2, WPA3, TKIP, and AES | 2.3-B003 | Basic | N/A | Self-reviewed |
| WPA3 encryption on open networks | CompTIA 2.3; Messer p. 31 | WPA2, WPA3, TKIP, and AES | 2.3-B004 | Basic | N/A | Self-reviewed |
| TKIP versus AES | CompTIA 2.3; Messer p. 31 | WPA2, WPA3, TKIP, and AES | 2.3-B005, 2.3-C001, 2.3-C002 | Basic, Cloze | N/A; Basic tests selection while Cloze cards test acronym expansion | Self-reviewed |
| Personal/PSK versus Enterprise/802.1X | Messer p. 31; supports CompTIA 2.3 | Personal and Enterprise Modes | 2.3-B007 | Basic | N/A | Self-reviewed |
| RADIUS role and expansion | CompTIA 2.3; Messer p. 31 | RADIUS | 2.3-B008, 2.3-C003 | Basic, Cloze | N/A; Basic tests application while Cloze tests acronym expansion | Self-reviewed |
| TACACS+ role and expansion | CompTIA 2.3; Messer pp. 31–32 | TACACS+ | 2.3-B009, 2.3-C004 | Basic, Cloze | N/A; Basic tests selection while Cloze tests acronym expansion | Self-reviewed |
| Kerberos tickets, mutual authentication, and SSO | CompTIA 2.3; Messer p. 31 | Kerberos | 2.3-B010 | Basic | N/A | Self-reviewed |
| Multifactor authentication | CompTIA 2.3; Messer p. 32 | Multifactor Authentication | 2.3-B011 | Basic | N/A | Self-reviewed |
| Message integrity check | Messer p. 30; supports CompTIA 2.3 | Encryption and Authentication | None | None | Context for why wireless protection checks integrity; a standalone acronym card would not improve the required protocol comparison | Self-reviewed |
| Radio frequency, range, and power effects | Private practice gap context; not independently validated by approved notes | None | None | None | Omitted because the approved sources do not support these negative claims for Objective 2.3; the practice exam cannot supply card content or citations | Independently reviewed |
| Historical dates and original protocol development | Messer pp. 31–32; supports CompTIA 2.3 | WPA2, WPA3, TKIP, and AES; TACACS+; Kerberos | None | None | Version dates and development history are low-value trivia for the official comparison task | Self-reviewed |
| Authentication implementation cost examples | Messer p. 32; supports CompTIA 2.3 | Multifactor Authentication | None | None | Context only; cost varies by implementation and is not a stable selection rule | Self-reviewed |

## Objective-specific cautions

- Keep wireless protection separate from the authentication service used to
  validate a user.
- Do not add port numbers, packet fields, or vendor-specific configuration
  steps that the approved sources and official scope do not require.
- Keep legacy protocol history in the study guide rather than turning dates
  into recall cards.

## HighYield review

| Card IDs | Rubric justification | Review status |
| --- | --- | --- |
| 2.3-B001–B003, B005, B007–B011 | Central protocol, encryption, and authentication distinctions | Approved by independent review |
| 2.3-C001–C002 | Frequently tested encryption acronym expansions | Approved by independent review |

## Research and extraction

- [x] The matching 220-1202 exam version and Objective 2.3 scope are confirmed.
- [x] The official CompTIA objective PDF was used as the primary scope authority.
- [x] Professor Messer v1.40 printed pages 30–32 were used only for approved
      secondary validation and page references.
- [x] The Professor Messer Core 2 practice exam was used only as a private
      secondary gap check after official scope was established.
- [x] Practice-gap concepts useful for active recall are carded.
- [x] No new secondary source was used.
- [x] Concepts were extracted and expressed without copying source language.
- [x] No source ambiguity remains unresolved.

## Authoring

- [x] `study-guide.md` is written, sourced, and internally consistent.
- [x] Basic cards emphasize comparison, selection, and common-confusion
      handling in line with the official objective wording.
- [x] Cloze cards are limited to compact acronym expansion and do not duplicate
      the applied Basic-card targets.
- [x] Command cards were considered and are not applicable.
- [x] Image cards were considered; visual recognition does not improve these
      protocol and authentication comparisons.
- [x] Instructor Notes add a distinction, consequence, or decision boundary.
- [x] Custom tags and stable IDs follow repository rules.
- [x] Study-guide-only concepts have specific no-card reasons.
- [x] `changelog.md` records the draft.

## Review and build

- [x] Independent review and blocker-fix verification confirm accuracy, scope,
      atomicity, wording, redundancy, omissions, and HighYield classifications.
- [x] Original diagrams are not applicable; no image cards were created.
- [x] `.venv/bin/python scripts/validate.py` passes without unexplained warnings.
- [x] `.venv/bin/python scripts/build.py` passes and removes no expected output.
- [x] Generated TSV changes match the Markdown sources: `Basic.tsv` contains 10
      data rows and `Cloze.tsv` contains four; no Command, Image, or media
      output is expected.
- [x] The 95-test pytest suite and Ruff lint and format checks pass.
- [x] Manual Anki smoke testing passes for generated Basic and Cloze files.

## Acceptance record

- Date accepted: 2026-07-22.
- Final card count: 10 Basic cards and four Cloze cards, including 11
  HighYield cards.
- Generated TSV output: `Basic.tsv` contains 10 verified data rows and
  `Cloze.tsv` contains four; no Command, Image, or media output is expected.
- Manual Anki smoke test: User-reported pass on 2026-07-22 for the Basic and
  Cloze imports; headers were not imported as notes, HTML and Cloze content
  rendered correctly, Instructor Notes displayed after reveal, tags imported
  as Anki metadata, Card ID supported update behavior, re-import created no
  duplicates, and observed counts matched 10 Basic and four Cloze notes. The
  Anki version and disposable profile name were not provided.
- Media verification: Not applicable; Objective 2.3 has no Image cards.
- Acceptance decision: Accepted.

## Peer review record

| Reviewer | Date | Result | Required Changes | Approval Status |
| --- | --- | --- | --- | --- |
| Self-review | 2026-07-22 | Draft authored from official Objective 2.3 and Messer pp. 30–32; private practice gap check completed | Independent content review and manual Anki smoke test remain | Needs independent review |
| Independent content review | 2026-07-22 | NO-GO; official coverage, card roles, copyright safety, omissions, generated output, and HighYield choices passed | Remove unsupported radio frequency/range/power claims and 2.3-B006; clarify B004 and B009 wording | Changes required; blocker verification remains |
| Blocker-fix verification | 2026-07-22 | GO; unsupported claims and B006 were removed, recommendation wording was applied, generated TSVs matched isolated regeneration, and no new issues were found | None | Approved; ready for manual Anki smoke test |
| Manual Anki smoke test | 2026-07-22 | User-reported Basic and Cloze import, rendering, metadata tags, 14-note total, and Card ID re-import/update behavior passed; Anki version/profile not provided | None | Accepted |
