# Objective 2.5 completion checklist

**Objective status: ACCEPTED.** Objective 2.5 passed omitted-concepts review,
independent content review, review fixes, automated verification, and manual
Anki smoke testing.

## Domain mapping

| Folder | Domain | Required domain tag |
| --- | --- | --- |
| `2.5-networking-hardware-devices` | Networking | `A+::220-1201::Domain2-Networking` |

## Coverage map with Messer validation

| Concept | Source | Messer Validation | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Router | Messer v1.70 p.15; CompTIA 2.5 | Present, p.15 | Moving traffic | 2.5-B001 | Basic | N/A | Self-reviewed |
| Switch | Messer v1.70 p.15; CompTIA 2.5 | Present, p.15 | Moving traffic | 2.5-B002 | Basic | N/A | Self-reviewed |
| Managed switch | Messer v1.70 p.16; CompTIA 2.5 | Present, p.16 | Moving traffic | 2.5-B003 | Basic | N/A | Self-reviewed |
| Unmanaged switch | Messer v1.70 p.16; CompTIA 2.5 | Present, p.16 | Moving traffic | 2.5-B003 | Basic | N/A; managed/unmanaged selection is one comparison target | Self-reviewed |
| Access point | Messer v1.70 p.16; CompTIA 2.5 | Present, p.16 | Moving traffic | 2.5-B004 | Basic | N/A | Self-reviewed |
| Patch panel | Messer v1.70 p.16; CompTIA 2.5 | Present, p.16 | Organizing and protecting connections | 2.5-B005 | Basic | N/A | Self-reviewed |
| Firewall | Messer v1.70 p.16; CompTIA 2.5 | Present, p.16 | Organizing and protecting connections | 2.5-B006 | Basic | N/A | Self-reviewed |
| PoE injector | Messer v1.70 p.16; CompTIA 2.5 | Present, p.16 | Power over Ethernet | 2.5-B007 | Basic | N/A | Self-reviewed |
| PoE switch | Messer v1.70 p.16; CompTIA 2.5 | Present, p.16 | Power over Ethernet | 2.5-B008 | Basic | N/A | Self-reviewed |
| PoE standards and compatibility | Messer v1.70 p.16; CompTIA 2.5 | Present, p.16 | Power over Ethernet | 2.5-B009, 2.5-C003 | Basic, Cloze | N/A; compatibility reasoning and acronym recall are distinct | Self-reviewed |
| Cable modem | Messer v1.70 p.16; CompTIA 2.5 | Present, p.16 | Provider connection devices | 2.5-B010 | Basic | N/A | Self-reviewed |
| DSL modem | Messer v1.70 p.16; CompTIA 2.5 | Present, p.16 | Provider connection devices | 2.5-B011, 2.5-C005 | Basic, Cloze | N/A; hardware selection and acronym recall are distinct | Self-reviewed |
| Optical network terminal | Messer v1.70 p.16; CompTIA 2.5 | Present, p.16 | Provider connection devices | 2.5-B012, 2.5-C004 | Basic, Cloze | N/A; hardware selection and acronym recall are distinct | Self-reviewed |
| Network interface card | Messer v1.70 p.16; CompTIA 2.5 | Present, p.16 | NICs and physical MAC addresses | 2.5-B013, 2.5-C001 | Basic, Cloze | N/A; component function and acronym recall are distinct | Self-reviewed |
| Physical MAC address | Messer v1.70 p.16; CompTIA 2.5 | Present, p.16 | NICs and physical MAC addresses | 2.5-B013, 2.5-C002 | Basic, Cloze | N/A; component function and acronym recall are distinct | Self-reviewed |
| Exact PoE wattage/current figures | Messer v1.70 p.16 | Present, p.16 | Power over Ethernet | None | None | Included in the study guide only; standards compatibility has higher card value than electrical-value recall | Independently reviewed |
| DOCSIS versions and provider speed tiers | Messer v1.70 p.16 | DOCSIS present; versions not required | Intentionally limited details | None | None | Study-guide only; vendor/provider details are outside active-recall scope | Self-reviewed |
| DSL distance and speed characteristics | Messer v1.70 p.16 | Present, p.16 | Intentionally limited details | None | None | Deferred to Objective 2.7 connection characteristics to avoid duplication | Self-reviewed |
| Vendor UI, defaults, port counts, and pricing | Not an official 2.5 requirement | Not used | Intentionally limited details | None | None | Intentionally omitted; vendor-specific or volatile | Self-reviewed |
| Switch ASICs, multilayer switching, and detailed STP/SNMP configuration | Messer v1.70 pp.15–16 | Present as supporting detail | Intentionally limited details | None | None | Study-guide boundary only; beyond Objective 2.5 device comparison depth | Self-reviewed |
| Firewall rule syntax, VPN configuration, and proxy details | Messer v1.70 p.16 | Present as supporting capabilities | Intentionally limited details | None | None | Intentionally omitted; configuration depth belongs elsewhere | Self-reviewed |
| Physical device appearance | Not stable across vendors | Not used | Intentionally limited details | None | None | No Image card; appearance is variable and not a reliable learning target | Self-reviewed |
| Wireless standards | CompTIA Objective 2.2 | Validated in Objective 2.2 | None | None | None | Excluded to avoid duplicating accepted Objective 2.2 recall | Self-reviewed |
| Internet connection type comparisons | CompTIA Objective 2.7 | Deferred | None | None | None | Deferred to Objective 2.7 | Self-reviewed |
| Networking tools | CompTIA Objective 2.8 | Deferred | None | None | None | Deferred to Objective 2.8 | Self-reviewed |

## HighYield review

| Card ID | Rubric justification | Review status |
| --- | --- | --- |
| 2.5-B001 | Router selection is foundational network-device knowledge | Independently reviewed |
| 2.5-B002 | Switch selection and MAC-based forwarding are foundational | Independently reviewed |
| 2.5-B003 | Managed/unmanaged selection is a common deployment decision | Independently reviewed |
| 2.5-B004 | Access point function is foundational wired/wireless integration knowledge | Independently reviewed |
| 2.5-B006 | Firewall function is foundational network-security knowledge | Independently reviewed |
| 2.5-B007 | PoE injector selection is a common installation decision | Independently reviewed |
| 2.5-B009 | PoE standards compatibility prevents an incorrect power-source choice | Independently reviewed |
| 2.5-B012 | ONT recognition is foundational for fiber service handoffs | Independently reviewed |
| 2.5-B013 | NIC and physical MAC recognition are foundational device concepts | Independently reviewed |
| 2.5-C002 | MAC expansion supports a required physical-address concept | Independently reviewed |

## Research and extraction

- [x] Official CompTIA 220-1201 Objective 2.5 title and scope confirmed.
- [x] Professor Messer 220-1201 v1.70 pages 15–16 reviewed privately.
- [x] Concepts extracted without copying source wording or organization.
- [x] Card and no-card decisions recorded before card authoring.
- [x] No unresolved source conflict was guessed into content.

## Authoring

- [x] Study guide written with a References section.
- [x] Basic cards cover justified hardware-selection and comparison decisions.
- [x] Cloze cards cover only explicit compact acronym recall.
- [x] No Image cards created because vendor-variable appearance is not a stable visual target.
- [x] Instructor Notes add value on every card.
- [x] HighYield decisions follow the rubric and are documented.
- [x] No intentionally redundant learning targets retained.
- [x] Current draft card counts: 13 Basic, 5 Cloze, 0 Image.
- [x] Exact PoE wattage figures are covered in the study guide and remain
      intentionally not carded.
- [x] `2.5-B009` now asks for one direct action without changing its learning
      target.
- [x] Review fixes added no cards and deleted no cards.
- [x] Objective 2.6 was not created.

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
| Image.tsv import | Not applicable; Objective 2.5 has no Image cards |
| Headers imported as notes | No |
| Card ID first field and duplicate/update key | Passed |
| HTML rendering | Passed |
| Cloze generation | Passed |
| Custom OpenAPlus note types | Basic and Cloze passed |
| Instructor Notes after answer reveal | Passed |
| Tags imported as Anki metadata | Passed |
| Re-import/update behavior | Existing notes updated without duplication |
| Result | Pass |

Objective 2.5 accepted. No Objective 2.6 content was created.

## Peer review record

| Reviewer | Date | Result | Required Changes | Approval Status |
| --- | --- | --- | --- | --- |
| Self-review | 2026-06-29 | Initial draft and coverage decisions completed | Omitted-concepts review, independent review, and Anki smoke test | Needs independent review |
| Independent content review | 2026-06-29 | PoE study-guide coverage blocker and card wording polish identified | Applied before smoke testing | Ready for Anki smoke test |
| Maintainer | 2026-06-29 | Manual Anki smoke test passed | None | Accepted |
