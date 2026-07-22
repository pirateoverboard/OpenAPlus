# Objective 2.8 completion checklist

**Objective status: ACCEPTED.** Core 2 Objective 2.8 has passed independent
content review, blocker-fix verification, generated-output verification, and
manual Anki smoke testing.

Official context:

```text
Domain 2.0 Security, Objective 2.8: Given a scenario, apply common methods for
securing mobile devices.
```

Official bullet scope reviewed:

1. Hardening techniques: device encryption and screen locks using facial
   recognition, PIN codes, fingerprints, patterns, or swipe.
2. Configuration profiles.
3. Patch management: OS updates and application updates.
4. Endpoint security software: antivirus, anti-malware, and content filtering.
5. Locator applications.
6. Remote wipes.
7. Remote backup applications.
8. Failed log-in attempt restrictions.
9. Policies and procedures: MDM, BYOD vs. corporate-owned devices, and profile
   security requirements.

Source-scope decisions:

- The official objective defines the mobile-security scope and the `Given a
  scenario` learner task. Professor Messer p. 44 validates the control
  purposes, distinctions, and page reference.
- The cards use short selection or distinction scenarios rather than asking
  learners to reproduce the official bullet list.
- The private Core 2 practice-exam gap check reinforced remote backup, remote
  wipe, and group-based configuration profiles. No published wording,
  scenario, explanation, or citation was taken from it.
- The official objective lists `Pattern` and `Swipe` separately. Professor
  Messer p. 44 describes swipe as choosing a pattern and does not establish a
  reliable distinction. Both terms remain in the study guide as official
  screen-lock options, but no card asserts an unsupported difference.
- No new secondary source was used. The pattern/swipe wording difference is
  documented and does not block the supported card set.

## Coverage map

| Concept | Source | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- |
| Full-device encryption | CompTIA 2.8; Messer p. 44 | Harden the Device | 2.8-B001 | Basic | N/A | Self-reviewed |
| Screen locks | CompTIA 2.8; Messer p. 44 | Harden the Device | 2.8-B002 | Basic | N/A | Self-reviewed |
| Facial recognition and fingerprint biometrics | CompTIA 2.8; Messer p. 44 | Harden the Device | 2.8-B003 | Basic | N/A | Self-reviewed |
| PIN codes | CompTIA 2.8; Messer p. 44 | Harden the Device | None | None | Covered as a screen-lock option; separate direct recall would add no decision skill | Self-reviewed |
| Pattern and swipe | CompTIA 2.8; Messer p. 44 | Harden the Device | None | None | Official terms are covered, but the secondary source does not support a stable distinction | Self-reviewed |
| Configuration profiles | CompTIA 2.8; Messer p. 44 | Apply Configuration Profiles and MDM | 2.8-B004 | Basic | N/A | Self-reviewed |
| Mobile device management (MDM) | CompTIA 2.8; Messer p. 44 | Apply Configuration Profiles and MDM | 2.8-B005, 2.8-C001 | Basic, Cloze | N/A; cards test centralized purpose and acronym recall | Self-reviewed |
| OS updates | CompTIA 2.8; Messer p. 44 | Keep the OS and Applications Patched | 2.8-B006 | Basic | N/A | Self-reviewed |
| Application updates | CompTIA 2.8; Messer p. 44 | Keep the OS and Applications Patched | 2.8-B007 | Basic | N/A | Self-reviewed |
| Antivirus and anti-malware | CompTIA 2.8; Messer p. 44 | Use Endpoint Security Software | 2.8-B008 | Basic | N/A; combined because both address malicious software at this source depth | Self-reviewed |
| Content filtering | CompTIA 2.8; Messer p. 44 | Use Endpoint Security Software | 2.8-B009 | Basic | N/A | Self-reviewed |
| Locator applications | CompTIA 2.8; Messer p. 44 | Respond to Loss and Preserve Data | 2.8-B010 | Basic | N/A | Self-reviewed |
| Remote wipe | CompTIA 2.8; Messer p. 44 | Respond to Loss and Preserve Data | 2.8-B011 | Basic | N/A | Self-reviewed |
| Remote backup applications | CompTIA 2.8; Messer p. 44 | Respond to Loss and Preserve Data | 2.8-B012 | Basic | N/A | Self-reviewed |
| Failed log-in attempt restrictions | CompTIA 2.8; Messer p. 44 | Respond to Loss and Preserve Data | 2.8-B013 | Basic | N/A | Self-reviewed |
| BYOD vs. corporate-owned policy | CompTIA 2.8; Messer p. 44 | Set Policies for Ownership and Profiles | 2.8-B014 | Basic | N/A | Self-reviewed |
| Profile security requirements | CompTIA 2.8; Messer p. 44 | Set Policies for Ownership and Profiles | 2.8-B015 | Basic | N/A | Self-reviewed |
| Exact failed-attempt thresholds and vendor responses | Messer p. 44; supports CompTIA 2.8 | Respond to Loss and Preserve Data | None | None | Platform and policy specific; the stable target is the control purpose | Self-reviewed |
| Product-specific MDM tools, UI paths, and mobile-firewall behavior | Messer p. 44; supports CompTIA 2.8 | Apply Configuration Profiles and MDM; Use Endpoint Security Software | None | None | Implementation-specific and not required by the official objective | Self-reviewed |

## Objective-specific cautions

- Do not treat encryption, a screen lock, a locator, remote wipe, and remote
  backup as interchangeable controls.
- Do not prescribe a universal failed-attempt threshold or wipe behavior.
- Do not invent a pattern-versus-swipe distinction that the approved secondary
  source does not establish.
- Do not over-card product names, operating-system versions, management UI
  paths, or vendor-specific behavior.
- Do not pull mobile security symptoms and troubleshooting from Objective 3.3
  into this control-application objective.

## HighYield review

| Card IDs | Rubric justification | Review status |
| --- | --- | --- |
| 2.8-B001–B002, 2.8-B004–B009 | Central device-hardening, fleet-management, patching, and endpoint-control decisions | Independent review approved |
| 2.8-B011–B015 | Common loss-response, recovery, access-control, ownership, and policy decisions | Independent review approved |
| 2.8-C001 | MDM is a foundational acronym for centralized mobile administration | Independent review approved |

## Research and extraction

- [x] The matching 220-1202 exam version and Objective 2.8 scope are confirmed.
- [x] The official CompTIA objective PDF was used as the primary scope authority.
- [x] Professor Messer v1.40 printed page 44 was used only for approved
      secondary validation and page references.
- [x] The Professor Messer Core 2 practice exam was used only as a private
      secondary gap check after official scope was established.
- [x] Practice-gap concepts useful for active recall are carded.
- [x] No new secondary source was used.
- [x] Concepts were extracted and expressed without copying source language.
- [x] The pattern/swipe source ambiguity is documented without guessing.

## Authoring

- [x] `study-guide.md` is written, sourced, and internally consistent.
- [x] Basic cards emphasize short control-selection and distinction scenarios
      in line with the official `Given a scenario` wording.
- [x] The Cloze card is limited to acronym expansion and does not duplicate the
      MDM application target.
- [x] Command cards were considered and are not applicable.
- [x] Image cards were considered; visual recognition does not improve this
      policy-and-control objective.
- [x] Interview material was considered and is not justified by this atomic
      control-selection objective.
- [x] Instructor Notes add a control boundary, purpose, or distinction.
- [x] Custom tags and stable IDs follow repository rules.
- [x] Study-guide-only concepts have specific no-card reasons.
- [x] `changelog.md` records the draft.

## Review and build

- [x] Independent review confirms accuracy, scope, atomicity, wording,
      redundancy, omissions, and HighYield classifications.
- [x] Original diagrams are not applicable; no image cards were created.
- [x] `.venv/bin/python scripts/validate.py` passes without unexplained warnings.
- [x] `.venv/bin/python scripts/build.py` passes and removes no expected output.
- [x] Generated TSV changes match the Markdown sources: `Basic.tsv` contains 15
      data rows and `Cloze.tsv` contains one; no Command, Image, or media output
      is expected.
- [x] The 100-test pytest suite and Ruff lint and format checks pass.
- [x] Manual Anki smoke testing passes for generated Basic and Cloze files.

## Acceptance record

- Date accepted: 2026-07-22.
- Final card count: 15 Basic cards and one Cloze card, including 14 HighYield
  cards.
- Generated TSV output: `Basic.tsv` contains 15 verified data rows and
  `Cloze.tsv` contains one; no Command, Image, or media output is expected.
- Manual Anki smoke test: User-reported pass on 2026-07-22 for the Basic and
  Cloze imports; headers were not imported as notes, HTML and Cloze content
  rendered correctly, Instructor Notes displayed after reveal, tags imported
  as Anki metadata, Card ID supported update behavior, re-import created no
  duplicates, and observed counts matched 15 Basic and one Cloze note. The
  Anki version and disposable profile name were not provided.
- Media verification: Not applicable; Objective 2.8 has no Image cards.
- Acceptance decision: Accepted.

## Peer review record

| Reviewer | Date | Result | Required Changes | Approval Status |
| --- | --- | --- | --- | --- |
| Self-review | 2026-07-22 | Draft authored from official Objective 2.8 and Messer p. 44; private practice gap check completed | Independent content review and manual Anki smoke test remain | Needs independent review |
| Independent content review | 2026-07-22 | NO-GO; found one unsupported Instructor Notes claim, one answer-leading/overlapping profile card, and one difficulty mismatch | Revise 2.8-B004 and 2.8-B015; change 2.8-B008 to Easy | Changes required |
| Author fix pass | 2026-07-22 | Removed the unsupported claim, separated B015's profile-security-requirements target from B004, and corrected B008 difficulty | Blocker-fix verification and manual Anki smoke test remain | Needs blocker-fix verification |
| Blocker-fix verification | 2026-07-22 | GO; all three blockers resolved with no new source, redundancy, scope, metadata, or generated-output issues | None | Approved; ready for manual Anki smoke test |
| Manual Anki smoke test | 2026-07-22 | User-reported Basic and Cloze import, rendering, metadata tags, 16-note total, and Card ID re-import/update behavior passed; Anki version/profile not provided | None | Accepted |
