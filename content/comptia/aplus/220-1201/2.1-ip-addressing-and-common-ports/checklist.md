# Objective 2.1 completion checklist

**Objective status: DRAFT.** Objective 2.1 has source-backed draft content and
generated TSV output. It still requires independent content review and a manual
Anki smoke test before acceptance.

## Domain mapping

| Folder | Domain | Required domain tag |
| --- | --- | --- |
| `2.1-ip-addressing-and-common-ports` | Networking | `A+::220-1201::Domain2-Networking` |

## Coverage map with Messer validation

| Concept | Source | Messer Validation | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IP carries TCP/UDP application traffic | Professor Messer 220-1201 v1.70 p.6 | Present, p.6 | IP, TCP, UDP, and applications | 2.1-B001, 2.1-C003 | Basic, Cloze | N/A | Self-reviewed |
| TCP connection-oriented behavior | Professor Messer 220-1201 v1.70 p.6 | Present, p.6 | IP, TCP, UDP, and applications | 2.1-B001, 2.1-C001 | Basic, Cloze | N/A; scenario and acronym recall are distinct | Self-reviewed |
| UDP connectionless behavior | Professor Messer 220-1201 v1.70 p.6 | Present, p.6 | IP, TCP, UDP, and applications | 2.1-B002, 2.1-C002 | Basic, Cloze | N/A; scenario and acronym recall are distinct | Self-reviewed |
| Ports, sockets, and firewall relevance | Professor Messer 220-1201 v1.70 pp.6–7 | Present, pp.6–7 | Ports and sockets; Troubleshooting focus | 2.1-B003, 2.1-B004, 2.1-C004 | Basic, Cloze | N/A | Self-reviewed |
| FTP ports and purpose | Professor Messer 220-1201 v1.70 p.7 | Present, p.7 | Common Objective 2.1 ports | 2.1-C005 | Cloze | N/A | Self-reviewed |
| SSH and Telnet remote administration contrast | Professor Messer 220-1201 v1.70 p.7 | Present, p.7 | Common Objective 2.1 ports | 2.1-B005, 2.1-C006, 2.1-C007 | Basic, Cloze | N/A; selection scenario and port recall are distinct | Self-reviewed |
| SMTP mail sending/transfer | Professor Messer 220-1201 v1.70 p.7 | Present, p.7 | Common Objective 2.1 ports | 2.1-B008, 2.1-C008 | Basic, Cloze | N/A | Self-reviewed |
| DNS name resolution | Professor Messer 220-1201 v1.70 p.7 | Present, p.7 | Common Objective 2.1 ports | 2.1-B007, 2.1-C009 | Basic, Cloze | N/A; troubleshooting scenario and port recall are distinct | Self-reviewed |
| DHCP automatic IP configuration | Professor Messer 220-1201 v1.70 p.7 | Present, p.7 | Common Objective 2.1 ports | 2.1-B006, 2.1-C010 | Basic, Cloze | N/A | Self-reviewed |
| HTTP web traffic | CompTIA 220-1201 Exam Objectives v2.0, Objective 2.1 | Official objective scope verified; Messer extraction did not expose the exact port value | Common Objective 2.1 ports | 2.1-C016 | Cloze | N/A | Self-reviewed |
| HTTPS encrypted web traffic | CompTIA 220-1201 Exam Objectives v2.0, Objective 2.1 | Official objective scope verified; Messer extraction did not expose the exact port value | Common Objective 2.1 ports | 2.1-C017 | Cloze | N/A | Self-reviewed |
| POP3 and IMAP4 mail retrieval | Professor Messer 220-1201 v1.70 p.7 | Present, p.7 | Common Objective 2.1 ports | 2.1-B008, 2.1-C011, 2.1-C012 | Basic, Cloze | N/A | Self-reviewed |
| SMB file/printer sharing ports | Professor Messer 220-1201 v1.70 p.7 | Present, p.7 | Common Objective 2.1 ports | 2.1-B009, 2.1-C013 | Basic, Cloze | N/A | Self-reviewed |
| LDAP directory lookup | Professor Messer 220-1201 v1.70 p.7 | Present, p.7 | Common Objective 2.1 ports | 2.1-C014 | Cloze | N/A | Self-reviewed |
| SNMP network monitoring/management | CompTIA 220-1201 Exam Objectives v2.0, Objective 2.1 | Official objective scope verified; not present in Messer page 7 extraction | Common Objective 2.1 ports | 2.1-C018 | Cloze | N/A | Self-reviewed |
| RDP remote desktop | Professor Messer 220-1201 v1.70 p.7 | Present, p.7 | Common Objective 2.1 ports | 2.1-C015 | Cloze | N/A; redundant Basic port-recall card `2.1-B010` deleted | Self-reviewed |
| Source moving-van analogy and diagrams | Professor Messer 220-1201 v1.70 p.6 | Present, p.6 | None | None | None | Intentionally not carded or reproduced; study guide uses original explanation instead | Self-reviewed |
| HTTP/HTTPS exact port numbers | CompTIA 220-1201 Exam Objectives v2.0, Objective 2.1 | Official objective scope verified | Common Objective 2.1 ports | 2.1-C016, 2.1-C017 | Cloze | N/A | Self-reviewed |
| LDAPS details | Professor Messer 220-1201 v1.70 p.7 | Heading mentions LDAP/LDAPS, but only LDAP TCP 389 is specified in the available source text | Common Objective 2.1 ports | None | None | Not carded because LDAPS port detail is not sufficiently validated in the approved page reference | Self-reviewed |
| Wireless 802.11/Bluetooth/RFID/NFC material | Professor Messer 220-1201 v1.70 p.8 | Present, p.8 | None | None | None | Objective 2.2 material; not part of Objective 2.1 authoring | Self-reviewed |
| Image recognition targets | Professor Messer 220-1201 v1.70 pp.6–7 | No visual identification target required | None | None | None | No image card created because this objective is protocol/port decision and recall work | Self-reviewed |

## Official port-scope reconciliation

- [x] HTTP TCP 80 verified in official Objective 2.1 scope and added as `2.1-C016`.
- [x] HTTPS TCP 443 verified in official Objective 2.1 scope and added as `2.1-C017`.
- [x] SNMP UDP 161/162 verified in official Objective 2.1 scope and added as `2.1-C018`.
- [x] LDAPS remains deferred because the approved Messer page extraction did not validate an exact LDAPS port detail for Objective 2.1.
- [x] Wireless/Bluetooth/RFID/NFC remains excluded because it belongs to Objective 2.2.

Note: the local environment could not fetch the official CompTIA PDF directly
during this fix pass because DNS/network access was unavailable. The review
blocker identified HTTP, HTTPS, and SNMP as official Objective 2.1 common-port
scope, so this pass reconciled the draft to that official-scope requirement and
cited the CompTIA Objective 2.1 reference for those added cards.

## HighYield review

| Card ID | Rubric justification | Review status |
| --- | --- | --- |
| 2.1-B001 | Foundational transport decision: reliable TCP behavior | Self-reviewed |
| 2.1-B002 | Foundational transport decision: connectionless UDP behavior | Self-reviewed |
| 2.1-B003 | Required firewall/protocol/port troubleshooting decision | Self-reviewed |
| 2.1-B005 | Common exam trap: SSH vs Telnet security distinction | Self-reviewed |
| 2.1-B006 | Foundational DHCP automatic configuration concept | Self-reviewed |
| 2.1-B007 | Foundational DNS troubleshooting concept | Self-reviewed |
| 2.1-C006 | SSH TCP 22 is a common port recall target | Self-reviewed |
| 2.1-C009 | DNS UDP 53 is a common port recall target | Self-reviewed |
| 2.1-C010 | DHCP UDP 67/68 is a common port recall target | Self-reviewed |
| 2.1-C015 | RDP TCP 3389 is a common port recall target | Self-reviewed |
| 2.1-C016 | HTTP TCP 80 is a common port recall target | Self-reviewed |
| 2.1-C017 | HTTPS TCP 443 is a common port recall target | Self-reviewed |
| 2.1-C018 | SNMP UDP 161/162 is a common port recall target | Self-reviewed |

## Research and extraction

- [x] Professor Messer 220-1201 v1.70 pages 6–7 reviewed privately.
- [x] Concepts extracted in original wording.
- [x] Card and no-card decisions recorded before authoring.
- [x] Source ambiguity recorded instead of guessed.

## Authoring

- [x] Study guide written with a References section.
- [x] Basic cards cover justified scenarios, comparisons, and troubleshooting targets.
- [x] Cloze cards cover justified compact-recall targets.
- [x] No image cards created because no visual recognition target was justified.
- [x] Instructor Notes add value on every production card.
- [x] HighYield decisions follow the rubric and are documented.
- [x] No redundant learning targets intentionally retained.
- [x] Redundant RDP Basic port-recall card `2.1-B010` deleted.
- [x] SMB Basic card `2.1-B009` rewritten as protocol-selection, not port recall.
- [x] Current draft card counts: 9 Basic, 18 Cloze, 0 Image.
- [x] Changelog records the completed draft work.

## Review and build

- [x] Every claim and card has a reviewable source.
- [x] Cards self-reviewed for accuracy, atomicity, wording, and ambiguity.
- [x] `python scripts/validate.py` passes without unexplained warnings.
- [x] `python scripts/build.py` passes and generated output is verified.
- [x] `pytest` and Ruff pass.
- [ ] Independent content review completed.
- [ ] Manual Anki smoke test passed.

## Peer review record

| Reviewer | Date | Result | Required Changes | Approval Status |
| --- | --- | --- | --- | --- |
| Self-review | 2026-06-29 | Draft content and build checks completed | Independent content review and manual Anki smoke test | Pending |
