# Objective 1.3 completion checklist

**Objective status: ACCEPTED.** Core 2 Objective 1.3 passed independent review
fixes, generated-output verification, and manual Anki smoke testing for Basic
and Cloze imports. Image and media smoke-test checks are not applicable because
this objective has no Image cards.

Official context:

```text
Domain 1.0 Operating Systems, Objective 1.3: Compare and contrast basic
features of Microsoft Windows editions.
```

Official scope categories reviewed: Windows 10 editions, Windows 11 editions,
N versions, feature differences, upgrade paths, and hardware requirements.

Official bullet scope reviewed:

- Windows 10 editions: Home, Pro, Pro for Workstations, and Enterprise.
- Windows 11 editions: Home, Pro, and Enterprise.
- N versions.
- Feature differences: domain vs. workgroup, desktop styles/user interface,
  availability of Remote Desktop Protocol (RDP), RAM support limitations,
  BitLocker, and `gpedit.msc`.
- Upgrade paths: in-place upgrade and clean install.
- Hardware requirements: Trusted Platform Module (TPM) and Unified Extensible
  Firmware Interface (UEFI).

## Coverage map

This map was created during card authoring and should be rechecked during
independent review.

| Concept | Source | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- |
| Windows 10 and Windows 11 edition scope | CompTIA Objective 1.3; Professor Messer 220-1202 v1.40 pp. 5-6 | Windows 10 and Windows 11 Editions | None | None | Study-guide context; individual edition differences are carded | Self-reviewed |
| Windows Home editions | Professor Messer 220-1202 v1.40 pp. 5-6 | Windows 10 and Windows 11 Editions | 1.3-B001 | Basic | N/A | Self-reviewed |
| Windows Pro editions | Professor Messer 220-1202 v1.40 pp. 5-6 | Windows 10 and Windows 11 Editions | 1.3-B001 | Basic | N/A | Self-reviewed |
| Windows 10 Pro for Workstations | Professor Messer 220-1202 v1.40 p. 5 | Windows 10 and Windows 11 Editions | 1.3-B002 | Basic | N/A | Self-reviewed |
| Windows Enterprise editions | Professor Messer 220-1202 v1.40 pp. 5-6 | Windows 10 and Windows 11 Editions | 1.3-B003 | Basic | N/A | Self-reviewed |
| Windows N editions | Professor Messer 220-1202 v1.40 p. 6 | N Editions | 1.3-B004 | Basic | N/A | Self-reviewed |
| Workgroup versus domain | Professor Messer 220-1202 v1.40 p. 6 | Feature Differences | 1.3-B005, 1.3-B006, 1.3-C003 | Basic, Cloze | N/A; comparison, edition selection, and compact distinction are distinct | Self-reviewed |
| Desktop styles/user interface | Professor Messer 220-1202 v1.40 p. 6 | Feature Differences | 1.3-B007 | Basic | N/A | Self-reviewed |
| RDP host availability | Professor Messer 220-1202 v1.40 p. 6 | Feature Differences | 1.3-B008 | Basic | N/A | Self-reviewed |
| RAM support limitations | Professor Messer 220-1202 v1.40 pp. 5-6 | Feature Differences | 1.3-B015 | Basic | N/A | Self-reviewed |
| BitLocker | CompTIA Objective 1.3; Professor Messer 220-1202 v1.40 pp. 5-6 | Feature Differences | 1.3-B009 | Basic | N/A | Self-reviewed |
| Device Encryption in Windows 11 Home | Professor Messer 220-1202 v1.40 p. 6 | Windows 10 and Windows 11 Editions | 1.3-B014 | Basic | N/A | Self-reviewed |
| Group Policy Editor `gpedit.msc` | Professor Messer 220-1202 v1.40 p. 6 | Feature Differences | 1.3-B010, 1.3-C005 | Basic, Cloze | N/A; purpose and command recall are distinct | Self-reviewed |
| In-place upgrade versus clean install | Professor Messer 220-1202 v1.40 p. 4 | Upgrade Paths and Hardware Requirements | 1.3-B012 | Basic | N/A | Self-reviewed |
| TPM hardware requirement | CompTIA Objective 1.3; Professor Messer 220-1202 v1.40 p. 5 | Upgrade Paths and Hardware Requirements | 1.3-B011, 1.3-C006 | Basic, Cloze | N/A; scenario check and acronym recall are distinct | Self-reviewed |
| UEFI hardware requirement | CompTIA Objective 1.3; Professor Messer 220-1202 v1.40 p. 5 | Upgrade Paths and Hardware Requirements | 1.3-B011, 1.3-C007 | Basic, Cloze | N/A; scenario check and acronym recall are distinct | Self-reviewed |
| Windows 11 32-bit CPU limitation | Professor Messer 220-1202 v1.40 p. 6 | Upgrade Paths and Hardware Requirements | 1.3-B013 | Basic | N/A | Self-reviewed |
| Exact Windows release dates, number of Windows 10 releases, and support end dates | Professor Messer 220-1202 v1.40 p. 5 | Windows 10 and Windows 11 Editions | None | None | Volatile/version-specific context; not needed for the official compare-and-contrast task | Self-reviewed |
| Specific Enterprise examples such as AppLocker, BranchCache, MDM/MAM, and UX control | Professor Messer 220-1202 v1.40 pp. 5-6 | Windows 10 and Windows 11 Editions | None | None | Study-guide examples; Enterprise selection is the active-recall target | Self-reviewed |
| Specific Windows 11 interface features such as Snap layouts, Teams integration, touch integration, and Copilot | Professor Messer 220-1202 v1.40 p. 6 | Windows 10 and Windows 11 Editions | None | None | Study-guide context only; feature list is volatile and not necessary for the official edition-comparison target | Self-reviewed |

## HighYield review

| Card ID | Rubric justification | Review status |
| --- | --- | --- |
| 1.3-B001 | Home vs. Pro is a core edition-selection decision | Accepted |
| 1.3-B003 | Enterprise selection is common for large managed deployments | Accepted |
| 1.3-B005 | Domain vs. workgroup is a foundational Windows support distinction | Accepted |
| 1.3-B006 | Home vs. Pro domain joining is a common edition trap | Accepted |
| 1.3-B008 | RDP host availability is a common Windows edition difference | Accepted |
| 1.3-B009 | BitLocker is an explicit security feature difference | Accepted |
| 1.3-B011 | TPM/UEFI checks are required for Windows 11 deployment planning | Accepted |
| 1.3-B012 | In-place upgrade vs. clean install is a common upgrade-path decision | Accepted |

## Research and extraction

- [x] The matching exam version and objective scope are confirmed.
- [x] Official CompTIA objective PDF scope was confirmed as the primary scope
      authority.
- [x] Professor Messer PDF validation/page references were confirmed as the
      approved secondary source after official scope was established.
- [x] Professor Messer practice exam PDF was used only as a private secondary
      gap-check source after official scope was established.
- [x] A practice-exam gap check was completed before draft acceptance review;
      it reinforced BitLocker, domain/workgroup, RDP, Windows N editions, and
      upgrade/hardware-requirement coverage without being cited in card or
      study-guide source fields.
- [x] No new secondary source was used.
- [x] Sources were reviewed according to their defined scope and authoring roles.
- [x] Concepts were extracted without copying source language.
- [x] No unresolved source ambiguity was identified in this draft.
- [x] No ambiguity currently requires changelog escalation.

## Authoring

- [x] `study-guide.md` is written, sourced, and internally consistent.
- [x] Basic cards cover justified comparison, selection, and upgrade-path
      decisions.
- [x] Cloze cards cover justified compact recall without excessive deletions.
- [x] Image cards were considered and not created because visual recognition
      does not materially improve this objective.
- [x] `checklist.md` reflects the objective's actual concepts and coverage.
- [x] Instructor Notes add concise value rather than repeat answers.
- [x] Practice-test-relevant concepts were converted to cards when
      official-scope, source-supported, stable, and useful for recall or
      application.
- [x] Every HighYield card has reviewer agreement or a documented approval.
- [x] Custom tags and stable IDs follow repository rules.
- [x] `changelog.md` records the objective's authoring changes.

## Review and build

- [x] Every factual claim and card has been independently reviewed against a
      reviewable source.
- [x] Cards were peer reviewed for accuracy, atomicity, wording, and ambiguity.
- [x] Original diagrams are not applicable; no image cards were created.
- [x] `.venv/bin/python scripts/validate.py` passes without unexplained warnings.
- [x] `.venv/bin/python scripts/build.py` passes and removes no expected output.
- [x] Generated TSV changes are ready to commit with their Markdown sources.
- [x] `pytest` and Ruff pass. Docusaurus checks are not applicable because no
      website files changed.
- [x] Manual Anki smoke testing passed.
  - Test deck/profile: `OpenAPlus Import Test`.
  - Basic and Cloze imports verified.
  - Image import/media rendering: Not applicable; no Image cards.
  - Expected note count: 20; actual note count: 20.
  - Basic note count: 16; Cloze note count: 4.
  - Headers were not imported as notes.
  - Card ID was first field and used for duplicate/update behavior.
  - HTML rendered correctly.
  - Cloze cards generated correctly.
  - Custom OpenAPlus Basic and Cloze note types worked.
  - Instructor Notes displayed correctly after answer reveal.
  - Tags imported correctly as Anki metadata, not learner-facing fields.
  - Re-import updated existing notes instead of duplicating them.

## Peer review record

| Reviewer | Date | Result | Required Changes | Approval Status |
| --- | --- | --- | --- | --- |
| Self-review | 2026-07-12 | Draft authored from official Objective 1.3 and Messer pp. 4-6; practice gap check completed privately | Independent review, generated-output review, and manual Anki acceptance still required | Complete |
| Independent content review | 2026-07-12 | Required duplicate Basic/Cloze fixes | Remove duplicate Cloze cards `1.3-C001`, `1.3-C002`, and `1.3-C004` | Complete |
| Manual Anki smoke test | 2026-07-12 | Passed | `OpenAPlus Import Test`; 20 expected notes and 20 actual notes; Basic and Cloze imports; custom note types; tags metadata; re-import update behavior | Complete |
