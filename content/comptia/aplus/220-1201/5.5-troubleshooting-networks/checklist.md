# Objective 5.5 completion checklist

**Objective status: ACCEPTED.** Objective 5.5 has source-backed content,
regenerated output, completed review-fix cleanup, interview-practice material,
and a passing manual Anki smoke test.

## Domain mapping

| Folder | Domain | Required domain tag |
| --- | --- | --- |
| `5.5-troubleshooting-networks` | Hardware and Network Troubleshooting | `A+::220-1201::Domain5-Troubleshooting` |

## Scope decision

Objective 5.5 is treated as troubleshooting network symptoms. Because the user
requested interview preparation, active-recall cards emphasize evidence-driven
path isolation: link, local host, local network, gateway, remote network,
wireless environment, performance, authentication, and ISP escalation.

## Coverage map with Messer validation

| Concept | Source | Messer Validation | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| No network connectivity and link light | Messer v1.70 p.55; CompTIA 5.5 | Present, p.55 | No Connectivity and Limited Connectivity | 5.5-B001, 5.5-B002 | Basic | N/A; link indication and physical cabling are separate decisions | Self-reviewed |
| Loopback test | Messer v1.70 p.55; CompTIA 5.5 | Present, p.55 | No Connectivity and Limited Connectivity | 5.5-B003, 5.5-C001 | Basic, Cloze | N/A; test interpretation and address recall are distinct | Self-reviewed |
| Local IP address test | Messer v1.70 p.55; CompTIA 5.5 | Present, p.55 | No Connectivity and Limited Connectivity | 5.5-B004 | Basic | N/A | Self-reviewed |
| Default gateway test | Messer v1.70 p.55; CompTIA 5.5 | Present, p.55 | No Connectivity and Limited Connectivity | 5.5-B005 | Basic | N/A | Self-reviewed |
| Remote IP or beyond-router test | Messer v1.70 p.55; CompTIA 5.5 | Present, p.55 | No Connectivity and Limited Connectivity | 5.5-B006 | Basic | N/A | Self-reviewed |
| Limited/no connectivity and APIPA symptom | Messer v1.70 p.55; CompTIA 5.5 | Present, p.55 | No Connectivity and Limited Connectivity | 5.5-B007, 5.5-B008 | Basic | N/A; local IP check and APIPA interpretation are separate troubleshooting targets | Self-reviewed |
| Intermittent wireless interference | Messer v1.70 p.55; CompTIA 5.5 | Present, p.55 | Wireless Symptoms | 5.5-B009, 5.5-B010, 5.5-B011, 5.5-B012, 5.5-B013 | Basic | N/A; interference, signal strength, channel, multipath, and AP placement are separate clues | Self-reviewed |
| Slow network speeds | Messer v1.70 p.55; CompTIA 5.5 | Present, p.55 | Slow Speeds and Path Isolation | 5.5-B014, 5.5-B015, 5.5-B016, 5.5-B017 | Basic | N/A; end-to-end confirmation, speed test, hop evaluation, and capture are separate decisions | Self-reviewed |
| Jitter | Messer v1.70 p.55; CompTIA 5.5 | Present, p.55 | Voice, Video, Latency, and Jitter | 5.5-B018, 5.5-C002 | Basic, Cloze | N/A; symptom interpretation and term recall are distinct | Self-reviewed |
| Poor VoIP quality | Messer v1.70 p.55; CompTIA 5.5 | Present, p.55 | Voice, Video, Latency, and Jitter | 5.5-B019, 5.5-B020, 5.5-B021 | Basic | N/A; internet link, local equipment, and capture evidence are separate targets | Self-reviewed |
| Port flapping | Messer v1.70 p.55; CompTIA 5.5 | Present, p.55 | Port Flapping, Authentication, and Provider Scope | 5.5-B022, 5.5-B023, 5.5-B024, 5.5-B025 | Basic | N/A; cable test, switch-port move, and result interpretation are separate targets | Self-reviewed |
| High latency | Messer v1.70 p.55; CompTIA 5.5 | Present, p.55 | Voice, Video, Latency, and Jitter | 5.5-B026, 5.5-B027 | Basic | N/A; path response timing and packet-capture detail are separate targets | Self-reviewed |
| Signal-to-noise ratio | Messer v1.70 p.56; CompTIA 5.5 | Present, p.56 | Wireless Symptoms | 5.5-B029, 5.5-C003 | Basic, Cloze | N/A; low-SNR interpretation and acronym recall are distinct | Self-reviewed |
| Authentication issues | Messer v1.70 p.56; CompTIA 5.5 | Present, p.56 | Port Flapping, Authentication, and Provider Scope | 5.5-B030, 5.5-B031 | Basic | N/A; session refresh and hidden-service capture are separate decisions | Self-reviewed |
| Intermittent internet connectivity | Messer v1.70 p.56; CompTIA 5.5 | Present, p.56 | Port Flapping, Authentication, and Provider Scope | 5.5-B032, 5.5-B033, 5.5-B034, 5.5-B035, 5.5-B036, 5.5-C004 | Basic, Cloze | N/A; scope, ping, traceroute, ISP escalation, SLA, and acronym recall are separate targets | Self-reviewed |
| Escalation and documentation | Messer v1.70 p.55-56; CompTIA 5.5 | Supported across Objective 5.5 symptom set | Interview-ready Troubleshooting Language; interview-practice file | 5.5-B037, 5.5-B038 | Basic | N/A; ISP handoff and internal network-team handoff are separate details | Self-reviewed |
| Broad network troubleshooting explanations | Messer v1.70 p.55-56; CompTIA 5.5 | Supported across Objective 5.5 symptom set | Interview-ready Troubleshooting Language; interview-practice file | None | None | Broad spoken answers belong in `interview/`, not TSV cards | Self-reviewed |
| Exact packet capture filter syntax | Messer v1.70 p.55-56 | General packet capture only | Slow Speeds and Path Isolation | None | None | Intentionally omitted; command/filter syntax is tool-specific and not required | Self-reviewed |
| Exhaustive APIPA definitions and ranges | Messer v1.70 p.55; prior Objective 2.6 coverage | APIPA appears as symptom in 5.5 | No Connectivity and Limited Connectivity | None | None | Already covered in Objective 2.6; 5.5 uses APIPA only as troubleshooting evidence | Self-reviewed |
| Exact Wi-Fi channel plans | Messer v1.70 p.55 | General channel/configuration only | Wireless Symptoms | None | None | Study-guide only; exact plans are environment-specific and not required here | Self-reviewed |
| ISP-specific escalation procedures | Messer v1.70 p.56 | General ISP escalation only | Port Flapping, Authentication, and Provider Scope | None | None | Intentionally omitted; provider-specific and volatile | Self-reviewed |
| Numeric SNR thresholds | Messer v1.70 p.56 | General ratio quality only | Wireless Symptoms | None | None | Intentionally omitted; source supports high-level interpretation, not threshold tables | Self-reviewed |

## HighYield review

| Card ID | Rubric justification | Review status |
| --- | --- | --- |
| 5.5-B001 | Link light is a foundational no-connectivity first check | Self-review; needs independent agreement |
| 5.5-B003 | Loopback testing is a common path-isolation decision | Self-review; needs independent agreement |
| 5.5-B005 | Gateway reachability is a key local-network boundary | Self-review; needs independent agreement |
| 5.5-B007 | Local IP/APIPA check is a common limited-connectivity clue | Self-review; needs independent agreement |
| 5.5-B009 | Wireless interference is a frequent help desk symptom cause | Self-review; needs independent agreement |
| 5.5-B014 | Vague slow-network complaints need measurable confirmation | Self-review; needs independent agreement |
| 5.5-B018 | Jitter recognition is useful for voice/video complaints | Self-review; needs independent agreement |
| 5.5-B019 | VoIP quality depends on internet speed and latency | Self-review; needs independent agreement |
| 5.5-B022 | Port flapping cable checks prevent unnecessary hardware replacement | Self-review; needs independent agreement |
| 5.5-B026 | Latency path measurement is a core network troubleshooting decision | Self-review; needs independent agreement |
| 5.5-B029 | SNR interpretation is a high-value wireless troubleshooting clue | Self-review; needs independent agreement |
| 5.5-B032 | Scope evidence is essential for intermittent internet outages | Self-review; needs independent agreement |
| 5.5-B034 | ISP escalation requires evidence and account/contact readiness | Self-review; needs independent agreement |
| 5.5-C001 | Loopback address recall supports network isolation tests | Self-review; needs independent agreement |
| 5.5-C003 | SNR acronym recall supports wireless troubleshooting interpretation | Self-review; needs independent agreement |

## Research and extraction

- [x] Official CompTIA 220-1201 Objective 5.5 title and troubleshooting-networks scope confirmed from available objective references.
- [x] Professor Messer 220-1201 v1.70 pages 55-56 reviewed privately.
- [x] Concepts extracted without copying source wording, diagrams, or layout.
- [x] Card, study-guide-only, interview-only, and omitted decisions recorded.
- [x] Source ambiguity recorded instead of guessed into cards.

## Authoring

- [x] Study guide written with a References section.
- [x] Basic cards emphasize specific troubleshooting decisions rather than broad interview answers.
- [x] Cloze cards cover only compact recall targets.
- [x] Image cards were considered and intentionally omitted because visual recognition did not add enough value for the selected learning targets.
- [x] Instructor Notes add troubleshooting logic on every card.
- [x] HighYield decisions follow the rubric and are documented for review.
- [x] Duplicate learning target cleanup completed; 5.5-B028 was deleted as a duplicate of 5.5-B009.
- [x] Final accepted card counts: 37 Basic, 4 Cloze, 0 Image, 41 total.
- [x] Optional learner-facing hints added to selected troubleshooting Basic cards; hints guide reasoning without revealing answers.
- [x] Interview-practice directory created with longer spoken-answer scenarios.
- [x] Broad interview-style prompts kept out of regular Anki.
- [x] No Objective 5.5 scope was expanded.
- [x] No objectives outside Objective 5.5 were modified for content.
- [x] Objective 5.6 was not created.
- [x] No cards were added during review cleanup.
- [x] No unrelated cards were deleted during review cleanup.

## Review and build

- [x] Omitted-concepts review completed.
- [x] Independent review blockers fixed.
- [x] Independent review fixes completed.
- [x] Duplicate card cleanup completed.
- [x] Hint review passed.
- [x] Original diagrams reviewed for clarity, licensing, and unique names, or not applicable.
- [x] `python scripts/validate.py` passes.
- [x] `python scripts/build.py` passes and TSV output is regenerated.
- [x] `pytest` and Ruff checks pass.
- [x] Manual Anki smoke test passed.
- [x] Interview directory text not exported to TSV.
- [x] Objective accepted by maintainer.

## Build verification

- 2026-07-04: `.venv/bin/python scripts/validate.py` passed with 395 cards checked.
- 2026-07-04: `.venv/bin/python scripts/build.py` passed and regenerated TSV output.
- 2026-07-04: Generated Objective 5.5 TSV counts verified: 38 Basic, 4 Cloze, 0 Image.
- 2026-07-04: `Basic.tsv` uses the stable Hint column:
  `Card ID, Front, Hint, Back, Instructor Notes, Difficulty, Card Type, Objective, Source, Tags`.
- 2026-07-04: Objective 5.5 generated tags include the 5.5 objective tag,
  normalized objective-name tag, Domain 5 troubleshooting tag, card-type tag,
  HighYield where applicable, source-validation tag, and author topic tags.
- 2026-07-04: Interview-practice text was not exported to regular TSV output.
- 2026-07-04: No Image cards or Objective 5.5 media output were generated.
- 2026-07-04: `.venv/bin/python -m pytest` passed with 70 tests.
- 2026-07-04: `.venv/bin/ruff check .` passed.
- 2026-07-04: `.venv/bin/ruff format --check .` passed.
- 2026-07-04: Objective 5.6 was not created.
- 2026-07-04: Omitted-concepts review passed.
- 2026-07-04: Independent review blockers fixed before manual Anki smoke test.
- 2026-07-04: Deleted 5.5-B028 as a duplicate of 5.5-B009.
- 2026-07-04: Rewrote 5.5-B006 to avoid over-specific upstream-cause wording.
- 2026-07-04: Softened the answer-revealing hint in 5.5-B017.
- 2026-07-04: Softened the answer-revealing hint in 5.5-B030.
- 2026-07-04: No cards were added and no unrelated cards were deleted.
- 2026-07-04: Interview-practice text remains separate from TSV output.
- 2026-07-04: TSV regenerated after review fixes.
- 2026-07-04: Final expected card counts after cleanup: 37 Basic, 4 Cloze, 0 Image, 41 total.
- 2026-07-04: Manual Anki smoke test passed using the OpenAPlus Import Test deck/profile.
- 2026-07-04: Basic import passed.
- 2026-07-04: Cloze import passed.
- 2026-07-04: Image import was not applicable because Objective 5.5 has no Image cards.
- 2026-07-04: Final accepted card counts confirmed: 37 Basic, 4 Cloze, 0 Image, 41 total.
- 2026-07-04: `Basic.tsv` stable Hint column imported correctly.
- 2026-07-04: Headers were not imported as notes.
- 2026-07-04: Card ID was first field and used for duplicate/update behavior.
- 2026-07-04: HTML rendered correctly.
- 2026-07-04: Cloze cards generated correctly.
- 2026-07-04: Custom OpenAPlus Basic and Cloze note types worked.
- 2026-07-04: Instructor Notes displayed correctly after answer reveal.
- 2026-07-04: Tags imported as Anki metadata, not learner-facing fields.
- 2026-07-04: Re-import updated existing notes instead of duplicating them.
- 2026-07-04: Objective accepted after cleanup and smoke test.

## Peer review record

| Reviewer | Date | Result | Required Changes | Approval Status |
| --- | --- | --- | --- | --- |
| Self-review | 2026-07-04 | Initial Objective 5.5 draft and coverage decisions completed | Automated verification, omitted-concepts review, independent content review, and manual Anki smoke-test decision | Completed |
| Manual Anki smoke test | 2026-07-04 | Basic and Cloze imports passed; no Image cards applicable; re-import updated existing notes | None | Accepted |
