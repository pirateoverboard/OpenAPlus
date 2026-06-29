# Objective 2.7 completion checklist

**Objective status: ACCEPTED.** Objective 2.7 passed omitted-concepts review,
independent content review, review fixes, automated verification, and manual
Anki smoke testing.

## Domain mapping

| Folder | Domain | Required domain tag |
| --- | --- | --- |
| `2.7-internet-connection-and-network-types` | Networking | `A+::220-1201::Domain2-Networking` |

## Scope decision

The official Objective 2.7 scope contains six internet connection types and six
network types. This draft covers every explicit item. It excludes provider
plans, exact performance figures, implementation versions, and troubleshooting
tools because those details are volatile, environment-specific, or assigned to
Objective 2.8.

## Coverage map with Messer validation

| Concept | Source | Messer Validation | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Satellite internet | Messer v1.70 p.18; CompTIA 2.7 | Present, p.18 | Satellite | 2.7-B001 | Basic | N/A | Self-reviewed |
| Fiber internet | Messer v1.70 p.18; CompTIA 2.7 | Present, p.18 | Fiber | 2.7-B002 | Basic | N/A | Self-reviewed |
| Cable internet and DOCSIS | Messer v1.70 p.18; CompTIA 2.7 | Present, p.18 | Cable | 2.7-B003, 2.7-C003 | Basic, Cloze | N/A; service recognition and acronym expansion are distinct | Self-reviewed |
| DSL | Messer v1.70 p.18; CompTIA 2.7 | Present, p.18 | DSL | 2.7-B004, 2.7-C001 | Basic, Cloze | N/A; connection selection and acronym expansion are distinct | Self-reviewed |
| Cellular internet | Messer v1.70 p.19; CompTIA 2.7 | Present, p.19 | Cellular | 2.7-B005 | Basic | N/A | Self-reviewed |
| WISP | Messer v1.70 p.19; CompTIA 2.7 | Present, p.19 | WISP | 2.7-B006, 2.7-C002 | Basic, Cloze | N/A; service selection and acronym expansion are distinct | Self-reviewed |
| LAN | Messer v1.70 p.19; CompTIA 2.7 | Present, p.19 | LAN and WLAN | 2.7-B007, 2.7-C004 | Basic, Cloze | N/A; scope classification and acronym expansion are distinct | Self-reviewed |
| WAN | Messer v1.70 p.19; CompTIA 2.7 | Present, p.19 | WAN and MAN | 2.7-B007, 2.7-C005 | Basic, Cloze | N/A; scope classification and acronym expansion are distinct | Self-reviewed |
| PAN | Messer v1.70 p.19; CompTIA 2.7 | Present, p.19 | PAN | 2.7-B008, 2.7-C006 | Basic, Cloze | N/A; use-case recognition and acronym expansion are distinct | Self-reviewed |
| MAN | Messer v1.70 p.19; CompTIA 2.7 | Present, p.19 | WAN and MAN | 2.7-B009, 2.7-C007 | Basic, Cloze | N/A; scope recognition and acronym expansion are distinct | Self-reviewed |
| SAN | Messer v1.70 p.19; CompTIA 2.7 | Present, p.19 | SAN | 2.7-B010, 2.7-C008 | Basic, Cloze | N/A; storage-network recognition and acronym expansion are distinct | Self-reviewed |
| WLAN | Messer v1.70 p.19; CompTIA 2.7 | Present, p.19 | LAN and WLAN | 2.7-B011, 2.7-C009 | Basic, Cloze | N/A; network selection and acronym expansion are distinct | Self-reviewed |
| Exact provider speeds, prices, caps, and availability | Not explicit in CompTIA 2.7 | Variable examples only | Intentionally limited details | None | None | Intentionally omitted; volatile and provider-specific | Self-reviewed |
| Exact satellite latency and branded constellation details | Messer v1.70 p.18 | Supporting examples present | Intentionally limited details | None | None | Study-guide boundary only; precise figures and brands change | Self-reviewed |
| DSL variants and exact distance/speed limits | Messer v1.70 p.18 | Supporting examples present | Intentionally limited details | None | None | Study-guide only; deployment-specific detail has low recall value | Self-reviewed |
| DOCSIS versions, modulation, and channels | Messer v1.70 p.18 | DOCSIS concept present | Intentionally limited details | None | None | Intentionally omitted; beyond the explicit objective depth | Self-reviewed |
| Cellular generations, bands, and carrier behavior | Messer v1.70 p.19 | General cellular concept present | Intentionally limited details | None | None | Intentionally omitted; volatile and provider-specific | Self-reviewed |
| WISP proprietary technologies, alignment values, and ranges | Messer v1.70 p.19 | General deployment examples present | Intentionally limited details | None | None | Intentionally omitted; implementation-specific | Self-reviewed |
| Vendor-specific WAN, MAN, SAN, and WLAN architectures | Not explicit in CompTIA 2.7 | General characteristics only | Intentionally limited details | None | None | Intentionally omitted; beyond compare-and-contrast depth | Self-reviewed |
| Networking tools | CompTIA Objective 2.8 | Deferred | None | None | None | Deferred to Objective 2.8 | Self-reviewed |

## HighYield review

| Card ID | Rubric justification | Review status |
| --- | --- | --- |
| 2.7-B001 | Satellite latency and remote-coverage tradeoffs are common connection-selection distinctions | Independently reviewed |
| 2.7-B002 | Fiber selection is foundational to comparing connection media | Independently reviewed |
| 2.7-B003 | Cable/DOCSIS recognition is a common internet-service distinction | Independently reviewed |
| 2.7-B004 | DSL telephone-line and distance characteristics are common exam distinctions | Independently reviewed |
| 2.7-B006 | WISP recognition distinguishes terrestrial wireless service from satellite and cellular | Independently reviewed |
| 2.7-B007 | LAN versus WAN scope is foundational networking knowledge | Independently reviewed |
| 2.7-B008 | PAN recognition is foundational to classifying short-range personal networks | Independently reviewed |
| 2.7-B010 | SAN block-storage recognition prevents confusion with ordinary LAN file sharing | Independently reviewed |
| 2.7-B011 | WLAN versus upstream internet service is a common conceptual distinction | Independently reviewed |

## Research and extraction

- [x] Official CompTIA 220-1201 Objective 2.7 title and bullet scope confirmed.
- [x] Professor Messer 220-1201 v1.70 pages 18–19 reviewed privately.
- [x] Concepts extracted without copying source wording or organization.
- [x] Card and no-card decisions recorded before card authoring.
- [x] No unresolved source conflict was guessed into content.

## Authoring

- [x] Study guide written with a References section.
- [x] Basic cards cover justified comparison, selection, and classification skills.
- [x] Cloze cards cover compact acronym expansion only.
- [x] No Image cards created because physical appearance varies and topology art would not improve the explicit learning targets.
- [x] Instructor Notes add value on every card.
- [x] HighYield decisions follow the rubric and are documented for review.
- [x] No intentionally redundant learning targets retained.
- [x] Current draft card counts: 11 Basic, 9 Cloze, 0 Image.
- [x] Cellular wording limited to cellular networking, tethering, and mobile hotspots.
- [x] `2.7-B005` distinguishes the local device-to-phone connection from the cellular upstream without naming unsupported tethering media.
- [x] Fiber wording now separates supported installation/equipment cost from repair difficulty.
- [x] DSL wording retains supported distance sensitivity without adding line-condition claims.
- [x] WISP wording is limited to terrestrial wireless service and outdoor customer equipment.
- [x] Review fixes added no cards and deleted no cards.
- [x] Objective 2.8 was not created.

## Review and build

- [x] Every claim and card independently reviewed against its cited source.
- [x] Omitted-concepts review completed; no additional cards required.
- [x] Independent content review completed.
- [x] Review blockers resolved.
- [x] `python scripts/validate.py` passes.
- [x] `python scripts/build.py` passes and TSV output is regenerated.
- [x] `pytest` and Ruff checks pass.
- [x] Manual Anki smoke test passed.
- [x] Objective accepted by maintainer.

## Manual Anki smoke test

| Item | Result |
| --- | --- |
| Test deck/profile | OpenAPlus Import Test |
| Expected note count | 20 |
| Actual note count | 20 |
| Basic.tsv import | Passed |
| Cloze.tsv import | Passed |
| Image.tsv import | Not applicable; Objective 2.7 has no Image cards |
| Headers imported as notes | No |
| Card ID first field and duplicate/update key | Passed |
| HTML rendering | Passed |
| Cloze generation | Passed |
| Custom OpenAPlus note types | Basic and Cloze passed |
| Instructor Notes after answer reveal | Passed |
| Tags imported as Anki metadata | Passed |
| Re-import/update behavior | Existing notes updated without duplication |
| Result | Pass |

Objective 2.7 accepted. No Objective 2.8 content was created.

## Peer review record

| Reviewer | Date | Result | Required Changes | Approval Status |
| --- | --- | --- | --- | --- |
| Self-review | 2026-06-29 | Initial draft and coverage decisions completed | Omitted-concepts review, independent review, and Anki smoke test | Needs independent review |
| Independent content review | 2026-06-29 | Source-support wording blockers identified | Cellular, tethering, fiber, DSL, and WISP wording tightened | Ready for Anki smoke test |
| Maintainer | 2026-06-29 | Manual Anki smoke test passed with 20 expected and actual notes | None | Accepted |
