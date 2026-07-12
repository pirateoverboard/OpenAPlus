# Objective 1.1 completion checklist

**Objective status: ACCEPTED.** Core 2 Objective 1.1 passed independent review
fixes, generated-output verification, and manual Anki smoke testing for Basic
and Cloze imports. Image and media smoke-test checks are not applicable because
this objective has no Image cards.

Official context:

```text
Domain 1.0 Operating Systems, Objective 1.1: Explain common operating system
(OS) types and their purposes.
```

Official scope categories reviewed: workstation OSs, mobile OSs, filesystem
types, vendor lifecycle limitations, and compatibility concerns between
operating systems.

Official bullet scope reviewed:

- Workstation OSs: Windows, Linux, macOS, and Chrome OS.
- Mobile OSs: iPadOS, iOS, and Android.
- Filesystem types: NTFS, ReFS, FAT32, ext4, XFS, APFS, and exFAT.
- Vendor lifecycle limitations: EOL and update limitations.
- Compatibility concerns between operating systems.

## Coverage map

This map was created during card authoring and should be rechecked during
independent review.

| Concept | Source | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- |
| OS purpose and resource coordination | Professor Messer 220-1202 v1.40 p. 1 | Operating System Purpose | 1.1-B001 | Basic | N/A | Self-reviewed |
| Standard OS functions | Professor Messer 220-1202 v1.40 p. 1 | Operating System Purpose | None | None | Covered as study-guide context; separate memorization card would duplicate OS-purpose coverage | Self-reviewed |
| Windows workstation role and tradeoffs | Professor Messer 220-1202 v1.40 p. 1 | Workstation Operating Systems | 1.1-B002 | Basic | N/A | Self-reviewed |
| Linux workstation role and tradeoffs | Professor Messer 220-1202 v1.40 p. 1 | Workstation Operating Systems | 1.1-B003 | Basic | N/A | Self-reviewed |
| macOS workstation role and tradeoffs | Professor Messer 220-1202 v1.40 p. 1 | Workstation Operating Systems | 1.1-B004 | Basic | N/A | Self-reviewed |
| Chrome OS browser/cloud-centered role | Professor Messer 220-1202 v1.40 p. 1 | Workstation Operating Systems | 1.1-B005 | Basic | N/A | Self-reviewed |
| iPadOS, iOS, and Android roles | Professor Messer 220-1202 v1.40 pp. 1-2 | Mobile Operating Systems | 1.1-B006, 1.1-C001, 1.1-C002, 1.1-C003 | Basic, Cloze | N/A; B006 compares mobile OS platform scope, while Cloze cards test compact single-platform recall | Self-reviewed |
| Filesystem formatting purpose | Professor Messer 220-1202 v1.40 p. 2 | Filesystem Types | 1.1-B007 | Basic | N/A | Self-reviewed |
| NTFS Windows use and cross-OS limitations | Professor Messer 220-1202 v1.40 p. 2 | Filesystem Types | 1.1-B008, 1.1-C004 | Basic, Cloze | N/A; compatibility application and acronym recall are distinct | Self-reviewed |
| ReFS large Windows storage and integrity role | Professor Messer 220-1202 v1.40 p. 2 | Filesystem Types | 1.1-B009, 1.1-C005 | Basic, Cloze | N/A; selection and acronym recall are distinct | Self-reviewed |
| FAT32 large-file limitation | Professor Messer 220-1202 v1.40 p. 2 | Filesystem Types | 1.1-C006 | Cloze | N/A | Self-reviewed |
| exFAT removable cross-platform storage | Professor Messer 220-1202 v1.40 p. 2 | Filesystem Types | 1.1-B010, 1.1-C007 | Basic, Cloze | N/A; selection and acronym recall are distinct | Self-reviewed |
| ext4 Linux/Android association | Professor Messer 220-1202 v1.40 p. 2 | Filesystem Types | 1.1-B011 | Basic | N/A | Self-reviewed |
| XFS high-performance Linux storage role | Professor Messer 220-1202 v1.40 p. 2 | Filesystem Types | 1.1-B012 | Basic | N/A | Self-reviewed |
| APFS Apple platform and SSD-oriented role | Professor Messer 220-1202 v1.40 p. 2 | Filesystem Types | 1.1-B013, 1.1-C008 | Basic, Cloze | N/A; selection and acronym recall are distinct | Self-reviewed |
| Vendor lifecycle and EOL/update limitations | Professor Messer 220-1202 v1.40 p. 2 | Lifecycle and Compatibility | 1.1-B014 | Basic | N/A | Self-reviewed |
| Compatibility concerns between operating systems | Professor Messer 220-1202 v1.40 p. 2 | Lifecycle and Compatibility | 1.1-B015 | Basic | N/A | Self-reviewed |
| OS vendor-specific app store development details | Professor Messer 220-1202 v1.40 pp. 1-2 | Mobile Operating Systems | None | None | Supporting context; too platform-development-specific for this objective's OS-purpose focus | Self-reviewed |
| Exact update behavior differences by vendor | Professor Messer 220-1202 v1.40 p. 2 | Lifecycle and Compatibility | None | None | Volatile implementation detail; lifecycle risk is the stable learning target | Self-reviewed |

## HighYield review

| Card ID | Rubric justification | Review status |
| --- | --- | --- |
| 1.1-B001 | Foundational concept for all OS objectives | Accepted |
| 1.1-B008 | Common cross-platform NTFS compatibility trap | Accepted |
| 1.1-B009 | Practice-gap and official-scope filesystem selection concept | Accepted |
| 1.1-B010 | Common removable-media and cross-OS file-sharing decision | Accepted |
| 1.1-B013 | Common Apple filesystem selection concept | Accepted |
| 1.1-B014 | EOL/update limitations are a recurring support and security issue | Accepted |
| 1.1-B015 | Foundational OS compatibility concept | Accepted |
| 1.1-C006 | FAT32 4 GB file-size limit requires quick recall | Accepted |

## Research and extraction

- [x] The matching exam version and objective scope are confirmed.
- [x] Official CompTIA objective PDF scope was confirmed as the primary scope
      authority.
- [x] Professor Messer PDF validation/page references were confirmed as the
      approved secondary source after official scope was established.
- [x] Professor Messer practice exam PDF was used only as a private secondary
      gap-check source after official scope was established.
- [x] A practice-exam gap check was completed before draft acceptance review;
      it reinforced filesystem selection and cross-OS compatibility coverage.
- [x] No new secondary source was used.
- [x] Sources were reviewed according to their defined scope and authoring roles.
- [x] Concepts were extracted without copying source language.
- [x] No unresolved source ambiguity was identified in this draft.
- [x] No ambiguity currently requires changelog escalation.

## Authoring

- [x] `study-guide.md` is written, sourced, and internally consistent.
- [x] Basic cards cover justified OS-purpose, selection, compatibility, and
      lifecycle decisions.
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
  - Expected note count: 23; actual note count: 23.
  - Basic note count: 15; Cloze note count: 8.
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
| Self-review | 2026-07-12 | Draft authored from official Objective 1.1 and Messer pp. 1-2; practice gap check completed privately | Independent review, generated-output review, and manual Anki acceptance still required | Complete |
| Independent content review | 2026-07-12 | Required duplicate-card, checklist-scope, and difficulty fixes | Rewrite `1.1-B006`, record official bullet scope, and recalibrate direct-recognition difficulty | Complete |
| Manual Anki smoke test | 2026-07-12 | Passed | `OpenAPlus Import Test`; 23 expected notes and 23 actual notes; Basic and Cloze imports; custom note types; tags metadata; re-import update behavior | Complete |
