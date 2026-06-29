# Objective 2.6 completion checklist

**Objective status: ACCEPTED.** Objective 2.6 passed omitted-concepts review,
independent content review, review fixes, automated verification, and manual
Anki smoke testing.

## Domain mapping

| Folder | Domain | Required domain tag |
| --- | --- | --- |
| `2.6-basic-soho-network-configuration` | Networking | `A+::220-1201::Domain2-Networking` |

## Scope decision

The official title refers to wired/wireless SOHO networks, while its explicit
sub-objectives list only IP-addressing concepts. The approved private reference
also limits its Objective 2.6 pages to IP addressing. This draft follows the
explicit bullet list and does not infer cabling, wireless-security, or tool
content into Objective 2.6.

## Coverage map with Messer validation

| Concept | Source | Messer Validation | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IPv4 | Messer v1.70 p.17; CompTIA 2.6 | Present, p.17 | IPv4 public and private addresses | 2.6-B001, 2.6-C005 | Basic, Cloze | N/A; address classification and bit-length recall are distinct | Self-reviewed |
| Public IPv4 addresses | Messer v1.70 p.17; CompTIA 2.6 | Present, p.17 | IPv4 public and private addresses | 2.6-B001 | Basic | N/A | Self-reviewed |
| Private IPv4 addresses | Messer v1.70 p.17; CompTIA 2.6 | Present, p.17 | IPv4 public and private addresses | 2.6-B001, 2.6-C001, 2.6-C002, 2.6-C003 | Basic, Cloze | N/A; classification and exact range recall are distinct | Self-reviewed |
| NAT supporting context | Messer v1.70 p.17 | Present, p.17 | IPv4 public and private addresses | None | None | Included in the study guide only to explain private-to-public access; no NAT card created | Independently reviewed |
| IPv6 | Messer v1.70 p.17; CompTIA 2.6 | Present, p.17 | IPv6 | 2.6-B002, 2.6-C006 | Basic, Cloze | N/A; format recognition and bit-length recall are distinct | Self-reviewed |
| Static addressing | Messer v1.70 p.18; CompTIA 2.6 | Present, p.18 | Static and dynamic assignment | 2.6-B003 | Basic | N/A | Self-reviewed |
| Dynamic addressing | Messer v1.70 p.18; CompTIA 2.6 | Present, p.18 | Static and dynamic assignment | 2.6-B003 | Basic | N/A; static/dynamic selection is one comparison target | Self-reviewed |
| Subnet mask | Messer v1.70 p.18; CompTIA 2.6 | Present, p.18 | Subnet mask and default gateway | 2.6-B004 | Basic | N/A | Self-reviewed |
| Default gateway | Messer v1.70 p.18; CompTIA 2.6 | Present, p.18 | Subnet mask and default gateway | 2.6-B005 | Basic | N/A | Self-reviewed |
| APIPA purpose and symptom | Messer v1.70 p.18; CompTIA 2.6 | Present, p.18 | APIPA | 2.6-B006 | Basic | N/A | Self-reviewed |
| APIPA address block | Messer v1.70 p.18; CompTIA 2.6 | Present, p.18 | APIPA | 2.6-C004 | Cloze | N/A; range recall and symptom diagnosis are distinct | Self-reviewed |
| APIPA expansion | Messer v1.70 p.18; CompTIA 2.6 | Present, p.18 | APIPA | 2.6-C007 | Cloze | N/A | Self-reviewed |
| Binary conversion and full subnetting math | Not explicit in CompTIA 2.6 | Supporting detail only | Intentionally limited details | None | None | Intentionally omitted; beyond basic configuration depth | Self-reviewed |
| Classful IPv4 addressing | Not explicit in CompTIA 2.6 | Not required | Intentionally limited details | None | None | Intentionally omitted; historical detail is not needed for the objective | Self-reviewed |
| Exact address-count calculations | Messer v1.70 p.17 | Present as supporting scale context | Intentionally limited details | None | None | Study-guide boundary only; trivia-like compared with address recognition | Self-reviewed |
| Detailed IPv6 compression, address types, and prefix rules | Messer v1.70 p.17 | Basic format/prefix context present | Intentionally limited details | None | None | Study-guide only; exhaustive IPv6 rules exceed objective depth | Self-reviewed |
| APIPA ARP duplicate-check procedure | Messer v1.70 p.18 | Present, p.18 | Intentionally limited details | None | None | Study-guide only; implementation sequence has lower active-recall value | Self-reviewed |
| OS/router-specific configuration paths | Not an official requirement | Not used | Intentionally limited details | None | None | Intentionally omitted; vendor-specific and volatile | Self-reviewed |
| DHCP reservations, scopes, and exclusions | CompTIA Objective 2.4 | Covered in Objective 2.4 | None | None | None | Excluded to avoid duplicating accepted Objective 2.4 content | Self-reviewed |
| DNS/NTP and other optional client settings | CompTIA Objectives 2.3–2.4 | Covered earlier | None | None | None | Excluded to avoid duplicate service/configuration targets | Self-reviewed |
| Cabling and connectors | CompTIA Objective 3.2 | Deferred | None | None | None | Deferred to Objective 3.2; not an Objective 2.6 bullet | Self-reviewed |
| Wireless standards | CompTIA Objective 2.2 | Covered in Objective 2.2 | None | None | None | Excluded to avoid duplicating accepted Objective 2.2 content | Self-reviewed |
| Networking tools | CompTIA Objective 2.8 | Deferred | None | None | None | Deferred to Objective 2.8 | Self-reviewed |

## HighYield review

| Card ID | Rubric justification | Review status |
| --- | --- | --- |
| 2.6-B001 | Public/private IPv4 classification is foundational network configuration knowledge | Independently reviewed |
| 2.6-B004 | Subnet-mask symptoms are a common configuration and troubleshooting decision | Independently reviewed |
| 2.6-B005 | Default-gateway symptoms are a common help-desk issue | Independently reviewed |
| 2.6-B006 | APIPA recognition is a common DHCP troubleshooting cue | Independently reviewed |
| 2.6-C001 | The 10.0.0.0/8 private block requires quick recall | Independently reviewed |
| 2.6-C002 | The 172.16.0.0/12 private block is a common exam trap | Independently reviewed |
| 2.6-C003 | The 192.168.0.0/16 private block requires quick recall | Independently reviewed |
| 2.6-C004 | The APIPA block is a high-value troubleshooting fact | Independently reviewed |

## Research and extraction

- [x] Official CompTIA 220-1201 Objective 2.6 title and explicit scope confirmed.
- [x] Professor Messer 220-1201 v1.70 pages 17–18 reviewed privately.
- [x] Broad title versus explicit bullet-list scope decision recorded.
- [x] Concepts extracted without copying source wording or organization.
- [x] Card and no-card decisions recorded before card authoring.
- [x] No unresolved source conflict was guessed into content.

## Authoring

- [x] Study guide written with a References section.
- [x] Basic cards cover justified configuration and troubleshooting decisions.
- [x] Cloze cards cover compact address and acronym recall.
- [x] No Image cards created because no stable visual target adds learning value.
- [x] Instructor Notes add value on every card.
- [x] HighYield decisions follow the rubric and are documented.
- [x] No intentionally redundant learning targets retained.
- [x] Current draft card counts: 6 Basic, 7 Cloze, 0 Image.
- [x] NAT added as study-guide-only context; no NAT card created.
- [x] `2.6-B001` now explains NAT when private IPv4 hosts access public networks.
- [x] `2.6-B006` now asks what an APIPA address indicates without claiming a
      single specific DHCP failure.
- [x] Review fixes added no cards and deleted no cards.
- [x] Objective 2.7 was not created.

## Review and build

- [x] Every claim and card has a reviewable source.
- [x] Cards self-reviewed for accuracy, atomicity, wording, and ambiguity.
- [x] Omitted-concepts review completed; no additional cards required.
- [x] Independent content review completed; required blockers applied.
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
| Image.tsv import | Not applicable; Objective 2.6 has no Image cards |
| Headers imported as notes | No |
| Card ID first field and duplicate/update key | Passed |
| HTML rendering | Passed |
| Cloze generation | Passed |
| Custom OpenAPlus note types | Basic and Cloze passed |
| Instructor Notes after answer reveal | Passed |
| Tags imported as Anki metadata | Passed |
| Re-import/update behavior | Existing notes updated without duplication |
| Result | Pass |

Objective 2.6 accepted. No Objective 2.7 content was created.

## Peer review record

| Reviewer | Date | Result | Required Changes | Approval Status |
| --- | --- | --- | --- | --- |
| Self-review | 2026-06-29 | Initial draft and coverage decisions completed | Omitted-concepts review, independent review, and Anki smoke test | Needs independent review |
| Independent content review | 2026-06-29 | NAT clarity and APIPA prompt blockers identified | Applied before smoke testing | Ready for Anki smoke test |
| Maintainer | 2026-06-29 | Manual Anki smoke test passed | None | Accepted |
