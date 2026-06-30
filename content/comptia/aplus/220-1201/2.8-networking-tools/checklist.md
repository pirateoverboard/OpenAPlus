# Objective 2.8 completion checklist

**Objective status: ACCEPTED.** Objective 2.8 passed manual Anki smoke testing
and is accepted.

## Domain mapping

| Folder | Domain | Required domain tag |
| --- | --- | --- |
| `2.8-networking-tools` | Networking | `A+::220-1201::Domain2-Networking` |

## Scope decision

The official Objective 2.8 scope contains eight networking tools. Each tool has
one primary active-recall target. Three physical tools also have a separate
visual-identification card because recognizing their form tests a materially
different skill from choosing them in a scenario.

## Coverage map with Messer validation

| Concept | Source | Messer Validation | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Crimper | Messer v1.70 p.20; CompTIA 2.8 | Present, p.20 | Cable preparation and termination | 2.8-B001, 2.8-I001 | Basic, Image | N/A; scenario selection and visual recognition are distinct | Self-reviewed |
| Cable stripper | Messer v1.70 p.20; CompTIA 2.8 | Present as wire stripper, p.20 | Cable preparation and termination | 2.8-C001 | Cloze | N/A | Self-reviewed |
| Wi-Fi analyzer | Messer v1.70 p.20; CompTIA 2.8 | Present, p.20 | Wireless analysis | 2.8-B002 | Basic | N/A | Self-reviewed |
| Toner probe | Messer v1.70 p.20; CompTIA 2.8 | Present as tone generator and inductive probe, p.20 | Finding and checking cables | 2.8-B003, 2.8-I003 | Basic, Image | N/A; cable-tracing decision and visual recognition are distinct | Self-reviewed |
| Punchdown tool | Messer v1.70 p.20; CompTIA 2.8 | Present, p.20 | Cable preparation and termination | 2.8-B004, 2.8-I002 | Basic, Image | N/A; termination decision and visual recognition are distinct | Self-reviewed |
| Cable tester | Messer v1.70 p.20; CompTIA 2.8 | Present, p.20 | Finding and checking cables | 2.8-B005 | Basic | N/A | Self-reviewed |
| Loopback plug | Messer v1.70 p.20; CompTIA 2.8 | Present, p.20 | Port and traffic testing | 2.8-C002 | Cloze | N/A | Self-reviewed |
| Network tap | Messer v1.70 p.20; CompTIA 2.8 | Present, p.20 | Port and traffic testing | 2.8-B006 | Basic | N/A | Self-reviewed |
| Brand-specific tool shapes, models, and tester menus | Not explicit in CompTIA 2.8 | Product examples are not required | Intentionally limited detail | None | None | Intentionally omitted; volatile and vendor-specific | Self-reviewed |
| Exact termination sequences and pinout procedures | Not explicit in CompTIA 2.8 | Supporting workflow only | Intentionally limited detail | None | None | Intentionally omitted entirely; procedural depth exceeds tool-purpose scope | Self-reviewed |
| Advanced cable certification measurements | Messer v1.70 p.20 | Distinguished from basic testing | Finding and checking cables | None | None | Study-guide only; clarifies the limit of a basic cable tester | Self-reviewed |
| Wi-Fi channel tables and analyzer UI details | Not explicit in CompTIA 2.8 | General analyzer purpose only | Intentionally limited detail | None | None | Intentionally omitted; regional and product-specific | Self-reviewed |
| Packet decoding and capture-analysis workflow | Messer v1.70 p.20 | Tap purpose present | Intentionally limited detail | None | None | Intentionally omitted; tap selection is the objective-level target | Self-reviewed |
| Networking commands and software utilities | Not listed in CompTIA 2.8 | Not part of the eight-tool list | None | None | None | Intentionally omitted; outside Objective 2.8 scope | Self-reviewed |

## HighYield review

| Card ID | Rubric justification | Review status |
| --- | --- | --- |
| 2.8-B001 | Crimper selection is foundational cable-termination knowledge | Self-review; needs independent agreement |
| 2.8-B002 | Wi-Fi analyzer selection is a common wireless troubleshooting decision | Self-review; needs independent agreement |
| 2.8-B003 | Toner/probe selection is a common physical-layer cable-tracing decision | Self-review; needs independent agreement |
| 2.8-B004 | Punchdown selection is foundational structured-cabling knowledge | Self-review; needs independent agreement |
| 2.8-B005 | Cable tester selection is a common physical-layer troubleshooting decision | Self-review; needs independent agreement |
| 2.8-C002 | Downgraded to non-HighYield during independent-review polish; explicit in scope but less foundational than core tool-selection decisions | Self-review; accepted as non-HighYield for smoke-test draft |

## Research and extraction

- [x] Official CompTIA 220-1201 Objective 2.8 title and bullet scope confirmed.
- [x] Professor Messer 220-1201 v1.70 page 20 reviewed privately.
- [x] Concepts extracted without copying source wording, diagrams, or layout.
- [x] Card, image, study-guide-only, and omitted decisions recorded.
- [x] No unresolved source conflict was guessed into content.

## Authoring

- [x] Study guide written with a References section.
- [x] Basic cards cover justified tool-selection scenarios.
- [x] Cloze cards cover compact tool-purpose recall without duplicating Basic cards.
- [x] Image cards use original simplified SVGs for useful visual recognition.
- [x] Instructor Notes add value on every card.
- [x] HighYield decisions follow the rubric and are documented for review.
- [x] No intentionally redundant learning targets retained.
- [x] Current draft card counts: 6 Basic, 2 Cloze, 3 Image.

## Review and build

- [x] Omitted-concepts review completed.
- [x] Independent content review completed.
- [x] Original diagrams independently reviewed for clarity and licensing.
- [x] `python scripts/validate.py` passes.
- [x] `python scripts/build.py` passes and TSV/media output is regenerated.
- [x] `pytest` and Ruff checks pass.
- [x] Manual Anki smoke test passed.
- [x] Objective accepted by maintainer.

## Manual Anki smoke test

| Item | Result |
| --- | --- |
| Test deck/profile | OpenAPlus Import Test |
| Expected note count | 11 |
| Actual note count | 11 |
| Basic.tsv import | Passed |
| Cloze.tsv import | Passed |
| Image.tsv import | Passed |
| Headers imported as notes | No |
| Card ID first field and update key | Passed |
| HTML rendering | Passed |
| Cloze generation | Passed |
| Custom OpenAPlus Basic, Cloze, and Image note types | Passed |
| Instructor Notes after answer reveal | Passed |
| Tags as Anki metadata, not learner-facing fields | Passed |
| Image media rendering | Passed |
| Question-side SVG visible text and accessibility metadata answer-leak check | Passed |
| Answer-side SVG labels after reveal | Passed |
| Re-import/update behavior | Passed; existing notes updated without duplicates |
| Final result | Pass |

## Peer review record

| Reviewer | Date | Result | Required Changes | Approval Status |
| --- | --- | --- | --- | --- |
| Self-review | 2026-06-29 | Initial draft and coverage decisions completed | Omitted-concepts review, independent review, and Anki smoke test | Needs independent review |
| Independent content review | 2026-06-29 | Required fixes applied before Anki smoke test | SVG metadata answer leaks fixed; Wi-Fi analyzer wording tightened; punchdown wording tightened; difficulty polish applied to 2.8-B003, 2.8-B006, and 2.8-I003; 2.8-C002 downgraded from HighYield; exact termination procedures clarified as omitted entirely; no cards added; no cards deleted; Objective 2.9 was not created | Ready for manual Anki smoke test after automated checks |
| Maintainer manual Anki smoke test | 2026-06-30 | Basic, Cloze, and Image imports passed; media rendered; SVG answer-leak checks passed; re-import updated existing notes | None | Approved; Objective 2.8 accepted |
