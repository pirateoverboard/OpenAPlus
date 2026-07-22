# Objective 2.5 completion checklist

**Objective status: ACCEPTED.** Core 2 Objective 2.5 has passed independent
content review, blocker-fix verification, generated-output verification, and
manual Anki smoke testing.

Official context:

```text
Domain 2.0 Security, Objective 2.5: Compare and contrast common social
engineering attacks, threats, and vulnerabilities.
```

Official bullet scope reviewed:

- Social engineering: phishing, including vishing, smishing, QR code phishing,
  spear phishing, and whaling; shoulder surfing; tailgating; impersonation; and
  dumpster diving.
- Threats: denial of service (DoS), distributed denial of service (DDoS), evil
  twin, zero-day attack, spoofing, on-path attack, brute-force attack,
  dictionary attack, insider threat, Structured Query Language (SQL) injection,
  cross-site scripting (XSS), business email compromise (BEC), and supply
  chain/pipeline attack.
- Vulnerabilities: non-compliant systems, unpatched systems, unprotected systems
  with missing antivirus or firewall, end of life (EOL), and bring your own
  device (BYOD).

Source-scope decisions:

- The official objective defines the complete concept set and its `Compare and
  contrast` learner task. Professor Messer pp. 35–41 validates the identifying
  characteristics and page references.
- Piggybacking is supporting contrast for the official tailgating term, not an
  additional flashcard target.
- Reflected and stored XSS are study-guide context under the official XSS term;
  the principal comparison target is XSS versus SQL injection.
- The official EOL term is retained while the approved notes' more precise
  distinction is documented: end of sales may precede end of service life, and
  loss of security updates is the critical vulnerability.
- The private Core 2 practice-exam gap check reinforced phishing and spear
  phishing recognition; shoulder surfing and tailgating; DoS/DDoS; evil twins;
  spoofing and on-path attacks; and distinctions among insider, BEC, and supply
  chain threats. It supplied no card wording, scenarios, or citations.
- No new secondary source was used, and no source ambiguity remains unresolved.

## Coverage map

| Concept | Source | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- |
| Phishing | CompTIA 2.5; Messer p. 35 | Phishing and Its Variants | 2.5-B001 | Basic | N/A | Self-reviewed |
| Vishing | CompTIA 2.5; Messer p. 35 | Phishing and Its Variants | 2.5-B002 | Basic | N/A | Self-reviewed |
| Smishing | CompTIA 2.5; Messer p. 35 | Phishing and Its Variants | 2.5-B003 | Basic | N/A | Self-reviewed |
| QR code phishing | CompTIA 2.5; Messer p. 35 | Phishing and Its Variants | 2.5-B004 | Basic | N/A | Self-reviewed |
| Spear phishing and whaling | CompTIA 2.5; Messer p. 35 | Phishing and Its Variants | 2.5-B005 | Basic | N/A | Self-reviewed |
| Shoulder surfing | CompTIA 2.5; Messer pp. 35–36 | Physical and Human-Focused Attacks | 2.5-B006 | Basic | N/A | Self-reviewed |
| Tailgating | CompTIA 2.5; Messer p. 36 | Physical and Human-Focused Attacks | 2.5-B007 | Basic | N/A | Self-reviewed |
| Impersonation | CompTIA 2.5; Messer p. 36 | Physical and Human-Focused Attacks | 2.5-B008 | Basic | N/A | Self-reviewed |
| Dumpster diving | CompTIA 2.5; Messer p. 36 | Physical and Human-Focused Attacks | 2.5-B009 | Basic | N/A | Self-reviewed |
| DoS and DDoS distinction/expansion | CompTIA 2.5; Messer p. 36 | Availability and Wireless Threats | 2.5-B010, 2.5-C001 | Basic, Cloze | N/A; Basic tests mechanism while Cloze tests acronym expansion | Self-reviewed |
| Evil twin | CompTIA 2.5; Messer p. 37 | Availability and Wireless Threats | 2.5-B011 | Basic | N/A | Self-reviewed |
| Zero-day attack | CompTIA 2.5; Messer p. 38 | Spoofing, On-Path, and Zero-Day Attacks | 2.5-B012 | Basic | N/A | Self-reviewed |
| Spoofing and on-path distinction | CompTIA 2.5; Messer p. 37 | Spoofing, On-Path, and Zero-Day Attacks | 2.5-B013 | Basic | N/A | Self-reviewed |
| Brute-force and dictionary attacks | CompTIA 2.5; Messer p. 38 | Password Attacks | 2.5-B014 | Basic | N/A | Self-reviewed |
| Insider threat | CompTIA 2.5; Messer p. 38 | Insider and Application Threats | 2.5-B015 | Basic | N/A | Self-reviewed |
| SQL injection and SQL expansion | CompTIA 2.5; Messer p. 39 | Insider and Application Threats | 2.5-B016, 2.5-C002 | Basic, Cloze | N/A; Basic tests attack recognition while Cloze tests acronym expansion | Self-reviewed |
| XSS and XSS expansion | CompTIA 2.5; Messer p. 39 | Insider and Application Threats | 2.5-B017, 2.5-C003 | Basic, Cloze | N/A; Basic tests attack recognition while Cloze tests acronym expansion | Self-reviewed |
| BEC and BEC expansion | CompTIA 2.5; Messer p. 40 | Business Email and Supply Chain Attacks | 2.5-B018, 2.5-C004 | Basic, Cloze | N/A; Basic tests scenario recognition while Cloze tests acronym expansion | Self-reviewed |
| Supply chain/pipeline attack | CompTIA 2.5; Messer pp. 40–41 | Business Email and Supply Chain Attacks | 2.5-B019 | Basic | N/A | Self-reviewed |
| Non-compliant systems | CompTIA 2.5; Messer p. 41 | Conditions That Create Vulnerability | 2.5-B020 | Basic | N/A | Self-reviewed |
| Unpatched systems | CompTIA 2.5; Messer p. 41 | Conditions That Create Vulnerability | 2.5-B021 | Basic | N/A | Self-reviewed |
| Unprotected systems | CompTIA 2.5; Messer p. 41 | Conditions That Create Vulnerability | 2.5-B022 | Basic | N/A | Self-reviewed |
| EOL and EOL expansion | CompTIA 2.5; Messer p. 41 | Conditions That Create Vulnerability | 2.5-B023, 2.5-C005 | Basic, Cloze | N/A; Basic tests lifecycle risk while Cloze tests acronym expansion | Self-reviewed |
| BYOD and BYOD expansion | CompTIA 2.5; Messer p. 41 | Conditions That Create Vulnerability | 2.5-B024, 2.5-C006 | Basic, Cloze | N/A; Basic tests security implications while Cloze tests acronym expansion | Self-reviewed |
| Piggybacking | Messer p. 36; supports CompTIA 2.5 tailgating | Physical and Human-Focused Attacks | None | None | Supporting contrast in B007; not a separately named official objective item | Self-reviewed |
| Reflected and stored XSS variants | Messer p. 39; supports CompTIA 2.5 | Insider and Application Threats | None | None | Study-guide context; separate cards would add detail beyond the official comparison target | Self-reviewed |
| Historical incidents and vendor examples | Messer pp. 38, 40–41; supports CompTIA 2.5 | Relevant threat sections | None | None | Volatile or trivia-like examples do not improve the stable attack distinctions | Self-reviewed |
| Exact patch schedules and product lifecycle dates | Messer p. 41; supports CompTIA 2.5 | Conditions That Create Vulnerability | None | None | Vendor- and time-specific detail is less stable than patching and support-lifecycle principles | Self-reviewed |

## Objective-specific cautions

- Keep the official three groups distinct: human-focused social engineering,
  technical threats, and conditions that create vulnerability.
- Do not reduce every phishing variant to email; the delivery channel and target
  distinguish the variants.
- Do not conflate spoofing's false identity with an on-path attack's intercepted
  and relayed communication.
- Do not conflate SQL injection, which changes a database query, with XSS, which
  runs attacker-supplied script in a victim's browser.
- Do not over-card historical incidents, product names, exact patch schedules,
  or vendor-specific lifecycle dates.

## HighYield review

| Card IDs | Rubric justification | Review status |
| --- | --- | --- |
| 2.5-B001–B003, B005–B007 | Central social-engineering distinctions and common recognition traps | Author justification recorded; independent review pending |
| 2.5-B010–B019 | Central threat comparisons, common attack recognition, and practice-gap distinctions | Author justification recorded; independent review pending |
| 2.5-B021–B024 | Common real-world vulnerability and lifecycle decisions | Author justification recorded; independent review pending |
| 2.5-C001, C003–C004 | Frequently used threat acronyms useful for quick recognition | Author justification recorded; independent review pending |

## Research and extraction

- [x] The matching 220-1202 exam version and Objective 2.5 scope are confirmed.
- [x] The official CompTIA objective PDF was used as the primary scope authority.
- [x] Professor Messer v1.40 printed pages 35–41 were used only for approved
      secondary validation and page references.
- [x] The Professor Messer Core 2 practice exam was used only as a private
      secondary gap check after official scope was established.
- [x] Practice-gap concepts useful for active recall are carded.
- [x] No new secondary source was used.
- [x] Concepts were extracted and expressed without copying source language.
- [x] Source terminology distinctions were documented without guessing.

## Authoring

- [x] `study-guide.md` is written, sourced, and internally consistent.
- [x] Basic cards emphasize comparison and recognition in line with the
      official `Compare and contrast` wording.
- [x] Cloze cards are limited to compact acronym expansion and do not duplicate
      applied Basic-card targets.
- [x] Command cards were considered and are not applicable.
- [x] Image cards were considered; visual recognition does not improve these
      attack and vulnerability distinctions.
- [x] Instructor Notes add a distinction, consequence, or decision boundary.
- [x] Custom tags and stable IDs follow repository rules.
- [x] Study-guide-only concepts have specific no-card reasons.
- [x] `changelog.md` records the draft.

## Review and build

- [x] Independent review confirms accuracy, scope, atomicity, wording,
      redundancy, omissions, and HighYield classifications.
- [x] Original diagrams are not applicable; no image cards were created.
- [x] `.venv/bin/python scripts/validate.py` passes without unexplained warnings.
- [x] `.venv/bin/python scripts/build.py` passes and removes no expected output.
- [x] Generated TSV changes match the Markdown sources: `Basic.tsv` contains 24
      data rows and `Cloze.tsv` contains six; no Command, Image, or media output
      is expected.
- [x] The 97-test pytest suite and Ruff lint and format checks pass.
- [x] Manual Anki smoke testing passes for generated Basic and Cloze files.

## Acceptance record

- Date accepted: 2026-07-22.
- Final card count: 24 Basic cards and six Cloze cards, including 23 HighYield
  cards.
- Generated TSV output: `Basic.tsv` contains 24 verified data rows and
  `Cloze.tsv` contains six; no Command, Image, or media output is expected.
- Manual Anki smoke test: User-reported pass on 2026-07-22 for the Basic and
  Cloze imports; headers were not imported as notes, HTML and Cloze content
  rendered correctly, Instructor Notes displayed after reveal, tags imported
  as Anki metadata, Card ID supported update behavior, re-import created no
  duplicates, and observed counts matched 24 Basic and six Cloze notes. The
  Anki version and disposable profile name were not provided.
- Media verification: Not applicable; Objective 2.5 has no Image cards.
- Acceptance decision: Accepted.

## Peer review record

| Reviewer | Date | Result | Required Changes | Approval Status |
| --- | --- | --- | --- | --- |
| Self-review | 2026-07-22 | Draft authored from official Objective 2.5 and Messer pp. 35–41; private practice gap check completed | Independent content review and manual Anki smoke test remain | Needs independent review |
| Independent content review | 2026-07-22 | NO-GO; scope, coverage, omissions, card roles, and generated output passed | Tighten zero-day wording and remove unsupported mitigation detail; remove unsupported rate-limit reference; recommended B002/B003 difficulty calibration | Changes Required |
| Blocker-fix verification | 2026-07-22 | GO; all source-fidelity and difficulty fixes passed, generated output matched, and no new issues were introduced | None | Approved; ready for manual Anki smoke test |
| Manual Anki smoke test | 2026-07-22 | User-reported Basic and Cloze import, rendering, metadata tags, 30-note total, and Card ID re-import/update behavior passed; Anki version/profile not provided | None | Accepted |
