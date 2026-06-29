# Objective 2.4 completion checklist

**Objective status: ACCEPTED.** Objective 2.4 passed omitted-concepts review,
independent content review, review fixes, automated verification, and manual
Anki smoke testing.

## Domain mapping

| Folder | Domain | Required domain tag |
| --- | --- | --- |
| `2.4-common-network-configuration-concepts` | Networking | `A+::220-1201::Domain2-Networking` |

## Coverage map with Messer validation

No-card dispositions use two explicit categories:

- **Included in study guide; not carded** means the concept remains useful
  explanatory context but does not justify a separate active-recall target.
- **Intentionally omitted entirely** means the detail is outside the objective's
  required depth, environment-specific, vendor-specific, or volatile.

| Concept | Source | Messer Validation | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DNS A record | Messer v1.70 p.11; CompTIA 2.4 | Present, p.11 | DNS record selection | 2.4-C001 | Cloze | N/A | Self-reviewed |
| DNS AAAA record | Messer v1.70 p.11; CompTIA 2.4 | Present, p.11 | DNS record selection | 2.4-C002 | Cloze | N/A | Self-reviewed |
| DNS CNAME record | Messer v1.70 p.11; CompTIA 2.4 | Present, p.11 | DNS record selection | 2.4-C003 | Cloze | N/A | Self-reviewed |
| DNS MX record | Messer v1.70 p.12; CompTIA 2.4 | Present, p.12 | DNS record selection | 2.4-C004 | Cloze | N/A | Self-reviewed |
| DNS TXT record | Messer v1.70 p.12; CompTIA 2.4 | Present, p.12 | DNS record selection | 2.4-C005 | Cloze | N/A | Self-reviewed |
| SPF | Messer v1.70 p.12; CompTIA 2.4 | Present, p.12 | DNS-based email protection | 2.4-B001 | Basic | N/A | Self-reviewed |
| DKIM | Messer v1.70 p.12; CompTIA 2.4 | Present, p.12 | DNS-based email protection | 2.4-B002 | Basic | N/A | Self-reviewed |
| DMARC | Messer v1.70 p.12; CompTIA 2.4 | Present, p.12 | DNS-based email protection | 2.4-B003 | Basic | N/A | Self-reviewed |
| DHCP reservation | Messer v1.70 p.13; CompTIA 2.4 | Present, p.13 | DHCP configuration | 2.4-B004 | Basic | N/A | Self-reviewed |
| DHCP exclusion | Messer v1.70 p.13; CompTIA 2.4 | Present, p.13 | DHCP configuration | 2.4-B005 | Basic | N/A | Self-reviewed |
| DHCP scope | Messer v1.70 p.13; CompTIA 2.4 | Present, p.13 | DHCP configuration | 2.4-B006 | Basic | N/A | Self-reviewed |
| DHCP lease | Messer v1.70 p.13; CompTIA 2.4 | Present, p.13 | DHCP configuration | 2.4-B007 | Basic | N/A | Self-reviewed |
| VLAN | Messer v1.70 p.14; CompTIA 2.4 | Present, p.14 | VLANs | 2.4-B008 | Basic | N/A | Self-reviewed |
| Client-to-site VPN | Messer v1.70 p.15; CompTIA 2.4 | Present, p.15 | VPNs | 2.4-B009 | Basic | N/A | Self-reviewed |
| Site-to-site VPN | Messer v1.70 p.15; CompTIA 2.4 | Present, p.15 | VPNs | 2.4-B010 | Basic | N/A | Self-reviewed |
| DORA sequence | Messer v1.70 p.13 | Present as supporting detail, p.13 | Intentionally limited details | None | None | Intentionally omitted entirely; the official bullet names leases, and a message-sequence drill exceeds the required configuration depth | Self-reviewed |
| Exact DHCP lease durations, pool sizes, and option values | Messer v1.70 p.13 | Concepts present; no universal values | DHCP configuration; Intentionally limited details | None | None | Included in study guide; not carded because values are environment-specific | Self-reviewed |
| DNS command output and record-file syntax | Messer v1.70 pp.11–12 | Present as examples, pp.11–12 | Intentionally limited details | None | None | Intentionally omitted entirely; syntax and output are outside the Objective 2.4 learning target | Self-reviewed |
| MX priority-number rules | Messer v1.70 p.12 | Present as supporting detail, p.12 | Intentionally limited details | None | None | Included in study guide; not carded because basic MX purpose has higher active-recall value | Self-reviewed |
| VLAN IDs, tags, trunks, and vendor commands | Messer v1.70 p.14 | VLAN concept present; implementation detail limited | Intentionally limited details | None | None | Intentionally omitted entirely; the objective requires VLAN recognition, not vendor-specific configuration | Self-reviewed |
| VPN products, UI paths, and cryptographic suites | Messer v1.70 p.15 | General deployment concepts present | Intentionally limited details | None | None | Intentionally omitted entirely; these details are volatile or beyond the stated objective depth | Self-reviewed |

## HighYield review

| Card ID | Rubric justification | Review status |
| --- | --- | --- |
| 2.4-B001 | SPF is a foundational email-authentication distinction and common exam trap | Independently reviewed |
| 2.4-B002 | DKIM is a foundational email-authentication distinction and common exam trap | Independently reviewed |
| 2.4-B003 | DMARC policy selection is an explicit, commonly confused objective concept | Independently reviewed |
| 2.4-B004 | DHCP reservations are a common configuration and help-desk decision | Independently reviewed |
| 2.4-B006 | Scope exhaustion is a practical DHCP troubleshooting symptom | Independently reviewed |
| 2.4-B008 | VLAN segmentation is foundational to later networking and security work | Independently reviewed |
| 2.4-C001 | A records are foundational DNS configuration recall | Independently reviewed |
| 2.4-C002 | AAAA records are foundational DNS configuration recall | Independently reviewed |
| 2.4-C004 | MX record purpose is required compact DNS recall | Independently reviewed |

## Research and extraction

- [x] Official CompTIA 220-1201 Objective 2.4 title and scope confirmed.
- [x] Professor Messer 220-1201 v1.70 pages 11–15 reviewed privately.
- [x] Concepts extracted without copying source wording or organization.
- [x] Card and no-card decisions recorded before card authoring.
- [x] No unresolved source conflicts were found.

## Authoring

- [x] Study guide written with a References section.
- [x] Basic cards cover justified configuration and troubleshooting decisions.
- [x] Cloze cards cover atomic DNS record recall.
- [x] No Image cards created because no visual-recognition target was justified.
- [x] Instructor Notes add value on every card.
- [x] HighYield decisions follow the rubric and are documented.
- [x] No intentionally redundant learning targets retained.
- [x] Current draft card counts: 10 Basic, 5 Cloze, 0 Image.
- [x] Independent-review blocker fixed: `2.4-B001` identifies SPF as a
      policy published in a DNS TXT record.
- [x] Independent-review polish applied: `2.4-B009` is not HighYield because
      the client-to-site subtype is supporting detail rather than an explicit
      Objective 2.4 bullet.

## Review and build

- [x] Every claim and card has a reviewable source.
- [x] Cards self-reviewed for accuracy, atomicity, wording, and ambiguity.
- [x] Omitted-concepts review completed; no additional cards required.
- [x] Independent content review completed; required blocker and polish applied.
- [x] `python scripts/validate.py` passes.
- [x] `python scripts/build.py` passes and TSV output is regenerated.
- [x] `pytest` and Ruff checks pass.
- [x] Manual Anki smoke test passed.
- [x] Objective accepted by maintainer.

## Manual Anki smoke test

| Item | Result |
| --- | --- |
| Test deck/profile | OpenAPlus Import Test |
| Basic.tsv import | Passed |
| Cloze.tsv import | Passed |
| Image.tsv import | Not applicable; Objective 2.4 has no Image cards |
| Headers imported as notes | No |
| Card ID first field and duplicate/update key | Passed |
| HTML rendering | Passed |
| Cloze generation | Passed |
| Custom OpenAPlus note types | Basic and Cloze passed |
| Instructor Notes after answer reveal | Passed |
| Tags imported as Anki metadata | Passed |
| Re-import/update behavior | Existing notes updated without duplication |
| Result | Pass |

Objective 2.4 accepted. No Objective 2.5 content was created.

## Peer review record

| Reviewer | Date | Result | Required Changes | Approval Status |
| --- | --- | --- | --- | --- |
| Self-review | 2026-06-29 | Initial draft and coverage decisions completed | Omitted-concepts review, independent review, and Anki smoke test | Needs independent review |
| Independent content review | 2026-06-29 | SPF terminology blocker and classification polish identified | Applied before smoke testing | Ready for Anki smoke test |
| Maintainer | 2026-06-29 | Manual Anki smoke test passed | None | Accepted |
