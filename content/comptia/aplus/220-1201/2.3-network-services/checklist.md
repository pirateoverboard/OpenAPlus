# Objective 2.3 completion checklist

**Objective status: ACCEPTED.** Objective 2.3 passed omitted-concepts review,
independent content review, review polish, and manual Anki smoke testing. It is
accepted for this pass.

## Domain mapping

| Folder | Domain | Required domain tag |
| --- | --- | --- |
| `2.3-network-services` | Networking | `A+::220-1201::Domain2-Networking` |

## Coverage map with Messer validation

| Concept | Source | Messer Validation | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DNS server | Professor Messer 220-1201 v1.70 p.9 | Present, p.9 | Core infrastructure services | 2.3-B001 | Basic | N/A | Self-reviewed |
| DHCP server | Professor Messer 220-1201 v1.70 p.9 | Present, p.9 | Core infrastructure services | 2.3-B002 | Basic | N/A | Self-reviewed |
| NTP server | Professor Messer 220-1201 v1.70 p.10 | Present, p.10 | Core infrastructure services | 2.3-B003, 2.3-C001 | Basic, Cloze | N/A; scenario and port recall are distinct | Self-reviewed |
| File share | Professor Messer 220-1201 v1.70 p.9 | Present, p.9 | User-facing services | 2.3-B004 | Basic | N/A | Self-reviewed |
| Print server | Professor Messer 220-1201 v1.70 p.9 | Present, p.9 | User-facing services | 2.3-B005 | Basic | N/A | Self-reviewed |
| Mail server | Professor Messer 220-1201 v1.70 p.9 | Present, p.9 | User-facing services | 2.3-B006 | Basic | N/A | Self-reviewed |
| Web server | Professor Messer 220-1201 v1.70 p.9 | Present, p.9 | User-facing services | 2.3-B007 | Basic | N/A | Self-reviewed |
| Authentication server | Professor Messer 220-1201 v1.70 p.9 | Present, p.9 | User-facing services | 2.3-B008 | Basic | N/A | Self-reviewed |
| Database server and SQL | Professor Messer 220-1201 v1.70 p.10 | Present, p.10 | Application and logging services | 2.3-B009, 2.3-C002 | Basic, Cloze | N/A; service recognition and acronym recall are distinct | Self-reviewed |
| Syslog | Professor Messer 220-1201 v1.70 p.9 | Present, p.9 | Application and logging services | 2.3-B010 | Basic | N/A | Self-reviewed |
| Proxy server | Professor Messer 220-1201 v1.70 p.10 | Present, p.10 | Application and logging services | 2.3-B011 | Basic | N/A | Self-reviewed |
| Load balancer | Professor Messer 220-1201 v1.70 p.10 | Present, p.10 | Application and logging services | 2.3-B012 | Basic | N/A | Self-reviewed |
| Spam gateway | Professor Messer 220-1201 v1.70 p.10 | Present, p.10 | Application and logging services | 2.3-B013 | Basic | N/A | Self-reviewed |
| All-in-one security appliance | Professor Messer 220-1201 v1.70 p.10 | Present, p.10 | Application and logging services | 2.3-B014, 2.3-C003 | Basic, Cloze | N/A; scenario and acronym recall are distinct | Self-reviewed |
| SCADA and ICS | Professor Messer 220-1201 v1.70 p.10 | Present, p.10 | Specialized and constrained systems | 2.3-B015, 2.3-C004, 2.3-C005 | Basic, Cloze | N/A; scenario and acronym recall are distinct | Self-reviewed |
| Legacy systems | Professor Messer 220-1201 v1.70 p.10 | Present, p.10 | Specialized and constrained systems | 2.3-B016 | Basic | N/A | Self-reviewed |
| Embedded systems | Professor Messer 220-1201 v1.70 p.10 | Present, p.10 | Specialized and constrained systems | 2.3-B017 | Basic | N/A | Self-reviewed |
| IoT devices | Professor Messer 220-1201 v1.70 p.10 | Present, p.10 | Specialized and constrained systems | 2.3-B018, 2.3-C006 | Basic, Cloze | N/A; segmentation scenario and acronym recall are distinct | Self-reviewed |
| Specific database brands | Professor Messer 220-1201 v1.70 p.10 | Present as examples, p.10 | Intentionally limited details | None | None | Study-guide only; product examples are not carded to avoid vendor-specific memorization | Self-reviewed |
| Exact security-appliance feature matrix | Professor Messer 220-1201 v1.70 p.10 | Present, p.10 | Intentionally limited details | None | None | Study-guide only; broad function recognition is carded, exhaustive feature recall is not | Self-reviewed |
| Storage/log sizing estimates | Professor Messer 220-1201 v1.70 p.9 | Present as qualitative warning, p.9 | Intentionally limited details | None | None | Study-guide only; exact sizing is implementation-specific | Self-reviewed |
| Cloud/on-site spam gateway deployment details | Professor Messer 220-1201 v1.70 p.10 | Present, p.10 | Intentionally limited details | None | None | Study-guide only; card focuses on gateway purpose rather than deployment model | Self-reviewed |
| Objective 2.1 common-port recall | Professor Messer 220-1201 v1.70 p.7 | Covered in Objective 2.1 | None | None | None | Excluded to avoid duplicate port-recall cards, except NTP UDP 123 which appears in Objective 2.3 source scope | Self-reviewed |

## HighYield review

| Card ID | Rubric justification | Review status |
| --- | --- | --- |
| 2.3-B001 | Foundational DNS service symptom recognition | Self-reviewed |
| 2.3-B002 | Foundational DHCP service symptom recognition | Self-reviewed |
| 2.3-B003 | Time synchronization is foundational for logs/authentication/troubleshooting | Self-reviewed |
| 2.3-B008 | Authentication server is foundational enterprise service recognition | Self-reviewed |
| 2.3-B011 | Proxy behavior is a common exam distinction | Self-reviewed |
| 2.3-B012 | Load balancer purpose is foundational service-availability knowledge | Self-reviewed |
| 2.3-B015 | SCADA/ICS segmentation is a common safety/security trap | Self-reviewed |
| 2.3-B018 | IoT segmentation is a common real-world security issue | Self-reviewed |
| 2.3-C001 | NTP UDP 123 is a compact service/port recall fact in this objective | Self-reviewed |

## Research and extraction

- [x] Professor Messer 220-1201 v1.70 pages 9–10 reviewed privately.
- [x] Concepts extracted in original wording.
- [x] Card and no-card decisions recorded before authoring.
- [x] Source ambiguity recorded instead of guessed.

## Authoring

- [x] Study guide written with a References section.
- [x] Basic cards cover justified scenarios and service recognition.
- [x] Cloze cards cover justified compact-recall targets.
- [x] No image cards created because no visual recognition target was justified.
- [x] Instructor Notes add value on every production card.
- [x] HighYield decisions follow the rubric and are documented.
- [x] No redundant learning targets intentionally retained.
- [x] Changelog records the completed draft work.
- [x] Review polish applied: `2.3-B001`, `2.3-B002`, `2.3-B008`,
  `2.3-B010`, `2.3-B011`, `2.3-B012`, and `2.3-B014` changed from medium
  to easy because they are straightforward service-recognition cards.
- [x] Review polish applied: `2.3-B010` remains useful but is no longer
  HighYield because Syslog is less foundational than DNS, DHCP, NTP,
  authentication, proxy, load balancing, and segmentation concepts.
- [x] Review polish applied: NTP checklist wording now says scenario and port
  recall are distinct.
- [x] Current draft card counts: 18 Basic, 6 Cloze, 0 Image.

## Review and build

- [x] Every claim and card has a reviewable source.
- [x] Cards self-reviewed for accuracy, atomicity, wording, and ambiguity.
- [x] `python scripts/validate.py` passes without unexplained warnings.
- [x] `python scripts/build.py` passes and generated output is verified.
- [x] `pytest` and Ruff pass.
- [x] Omitted-concepts review completed.
- [x] Independent content review completed.
- [x] Manual Anki smoke test passed.

## Manual Anki smoke test

| Item | Result |
| --- | --- |
| Test deck/profile | OpenAPlus Import Test |
| Basic.tsv import | Passed |
| Cloze.tsv import | Passed |
| Image.tsv import | Not applicable; Objective 2.3 has no Image cards |
| Expected note count | 24 |
| Actual note count | 24 |
| Headers imported as notes | No |
| Card ID first field and duplicate/update key | Passed |
| HTML rendering | Passed |
| Cloze generation | Passed |
| Custom OpenAPlus note types | Basic and Cloze passed |
| Instructor Notes after answer reveal | Passed |
| Tags imported as Anki metadata | Passed |
| Re-import/update behavior | Existing notes updated without duplication |
| Result | Pass |

Objective 2.3 accepted. No Objective 2.4 content was created.

## Peer review record

| Reviewer | Date | Result | Required Changes | Approval Status |
| --- | --- | --- | --- | --- |
| Self-review | 2026-06-29 | Draft content and build checks completed | Omitted-concepts review, independent content review, and manual Anki smoke test | Complete |
| Maintainer | 2026-06-29 | Manual Anki smoke test passed | None | Accepted |
