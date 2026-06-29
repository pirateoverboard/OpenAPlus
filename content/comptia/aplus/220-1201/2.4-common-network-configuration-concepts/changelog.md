# Objective 2.4 changelog

## 2026-06-29 — Initial Objective 2.4 draft

- Determined the official title and slug: `Common Network Configuration
  Concepts`, `2.4-common-network-configuration-concepts`.
- Created an original study guide covering DNS records, DNS-based email
  protection, DHCP configuration, VLANs, and VPNs.
- Created the coverage map and no-card decisions before card authoring.
- Added 10 Basic cards and 5 Cloze cards; no Image card has a justified visual
  recognition target.
- Added the Objective 2.4 generated domain/source-validation tag mapping:
  `A+::220-1201::Domain2-Networking` and `Source::Messer-v170`.
- Used Professor Messer pages 11–15 only for concept validation and concise page
  references. No content, structure, tables, diagrams, or command output was
  copied from the private source.
- Kept Objective 2.1 port recall and Objective 2.3 service recognition out of
  this objective.
- Intentionally did not card DORA ordering, exact DHCP values, DNS syntax and
  command output, MX priority details, VLAN implementation minutiae, or
  product-specific VPN settings.
- No Objective 2.5 content was created.
- Omitted-concepts review, independent review, and manual Anki smoke testing
  remain pending.

## 2026-06-29 — Independent review fixes before Anki smoke test

- Reworded `2.4-B001` to identify SPF as a policy published in a DNS TXT
  record, avoiding any implication that SPF is a separate DNS record type.
- Changed `2.4-B009` from HighYield to non-HighYield because client-to-site VPN
  is useful supporting detail rather than an explicit Objective 2.4 bullet.
- Clarified checklist no-card dispositions so study-guide-only context is
  distinct from details intentionally omitted entirely.
- Regenerated Objective 2.4 TSV output.
- Automated validation, build, pytest, Ruff lint, and Ruff formatting checks
  completed successfully.
- Added no new cards and deleted no cards.
- Did not create Objective 2.5 content.

## 2026-06-29 — Final acceptance

- Objective 2.4 accepted.
- Manual Anki smoke test passed in the `OpenAPlus Import Test` deck/profile.
- Basic.tsv and Cloze.tsv imported successfully.
- Image.tsv was not applicable because Objective 2.4 has no Image cards.
- Headers were not imported as notes.
- Card ID was the first field and supported duplicate/update behavior.
- HTML rendered correctly, and Cloze cards generated correctly.
- Custom OpenAPlus Basic and Cloze note types worked.
- Instructor Notes displayed correctly after answer reveal.
- Tags imported correctly as Anki metadata rather than learner-facing fields.
- Re-import updated existing notes without creating duplicates.
- No Objective 2.5 content was created.
