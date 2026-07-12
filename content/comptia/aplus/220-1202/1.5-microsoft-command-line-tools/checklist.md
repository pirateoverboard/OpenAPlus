# Objective 1.5 completion checklist

**Objective status: ACCEPTED.** Core 2 Objective 1.5 has passed independent
review, generated-output verification, and manual Anki smoke testing.

Official context:

```text
Domain 1.0 Operating Systems, Objective 1.5: Given a scenario, use the
appropriate Microsoft command-line tools.
```

Official scope categories reviewed: Navigation, Network, Disk management, File
management, Informational, and OS management.

Official bullet scope reviewed:

- Navigation: `cd` and `dir`.
- Network: `ipconfig`, `ping`, `netstat`, `nslookup`, `net use`, `tracert`,
  and `pathping`.
- Disk management: `chkdsk`, `format`, and `diskpart`.
- File management: `md`, `rmdir`, and `robocopy`.
- Informational: `hostname`, `net user`, `winver`, `whoami`, and
  `[command name] /?`.
- OS management: `gpupdate`, `gpresult`, and `sfc`.

## Coverage map

This map was created during card authoring and should be rechecked during
independent review.

| Concept | Source | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- |
| Objective 1.5 command categories | CompTIA Objective 1.5; Professor Messer 220-1202 v1.40 pp. 9-10 | All sections | None | None | Study-guide context; individual command decisions are carded | Self-reviewed |
| `dir` | CompTIA Objective 1.5; Professor Messer 220-1202 v1.40 p. 9 | Navigation and File Management | 1.5-T001 | Command | N/A; exact command recall only, Basic duplicate removed | Self-reviewed |
| `cd` / `chdir` | CompTIA Objective 1.5; Professor Messer 220-1202 v1.40 p. 9 | Navigation and File Management | 1.5-T002 | Command | N/A; exact command recall only, Basic duplicate removed | Self-reviewed |
| `md` / `mkdir` | CompTIA Objective 1.5; Professor Messer 220-1202 v1.40 p. 9 | Navigation and File Management | 1.5-T003 | Command | N/A; exact command recall only, Basic duplicate removed | Self-reviewed |
| `rmdir` / `rd` | CompTIA Objective 1.5; Professor Messer 220-1202 v1.40 p. 9 | Navigation and File Management | 1.5-T004 | Command | N/A; exact command recall only, Basic duplicate removed | Self-reviewed |
| `[command] /?` help syntax | CompTIA Objective 1.5; Professor Messer 220-1202 v1.40 p. 9 | Navigation and File Management | 1.5-T013 | Command | N/A; exact syntax recall only, Basic duplicate removed | Self-reviewed |
| `chkdsk /f` | CompTIA Objective 1.5; Professor Messer 220-1202 v1.40 p. 9 | Disk Management Commands | 1.5-B005, 1.5-T005 | Basic, Command | N/A | Self-reviewed |
| `chkdsk /r` | CompTIA Objective 1.5; Professor Messer 220-1202 v1.40 p. 9 | Disk Management Commands | 1.5-B006, 1.5-T006 | Basic, Command | N/A | Self-reviewed |
| `format` | CompTIA Objective 1.5; Professor Messer 220-1202 v1.40 p. 9 | Disk Management Commands | 1.5-B007, 1.5-T007 | Basic, Command | N/A | Self-reviewed |
| `diskpart` | CompTIA Objective 1.5; Professor Messer 220-1202 v1.40 p. 9 | Disk Management Commands | 1.5-B008, 1.5-T008 | Basic, Command | N/A | Self-reviewed |
| `robocopy` | CompTIA Objective 1.5; Professor Messer 220-1202 v1.40 p. 9 | Navigation and File Management | 1.5-B009, 1.5-T009 | Basic, Command | N/A; Basic tests robust-copy selection, Command tests exact recall | Self-reviewed |
| `hostname` | CompTIA Objective 1.5; Professor Messer 220-1202 v1.40 p. 9 | Informational Commands | 1.5-T010 | Command | N/A; exact command recall only, Basic duplicate removed | Self-reviewed |
| `winver` | CompTIA Objective 1.5; Professor Messer 220-1202 v1.40 p. 9 | Informational Commands | 1.5-T011 | Command | N/A; exact command recall only, Basic duplicate removed | Self-reviewed |
| `whoami /all` | CompTIA Objective 1.5; Professor Messer 220-1202 v1.40 p. 9 | Informational Commands | 1.5-B012, 1.5-T012 | Basic, Command | N/A | Self-reviewed |
| `net user` | CompTIA Objective 1.5; Professor Messer 220-1202 v1.40 p. 10 | Informational Commands | 1.5-B023, 1.5-T023 | Basic, Command | N/A; Basic tests `net use`/`net user` distinction, Command tests exact recall | Self-reviewed |
| `gpupdate` | CompTIA Objective 1.5; Professor Messer 220-1202 v1.40 p. 9 | OS Management Commands | 1.5-B014, 1.5-T014 | Basic, Command | N/A | Self-reviewed |
| `gpresult` | CompTIA Objective 1.5; Professor Messer 220-1202 v1.40 p. 9 | OS Management Commands | 1.5-B015, 1.5-T015 | Basic, Command | N/A | Self-reviewed |
| `sfc /scannow` | CompTIA Objective 1.5; Professor Messer 220-1202 v1.40 p. 9 | OS Management Commands | 1.5-B016, 1.5-T016 | Basic, Command | N/A | Self-reviewed |
| `ipconfig` | CompTIA Objective 1.5; Professor Messer 220-1202 v1.40 p. 10 | Network Commands | 1.5-T017 | Command | N/A; exact command recall only, Basic duplicate removed | Self-reviewed |
| `ipconfig /all` | Professor Messer 220-1202 v1.40 p. 10 | Network Commands | 1.5-B018, 1.5-T018 | Basic, Command | N/A; official `ipconfig` scope with validated detail option | Self-reviewed |
| `ping` | CompTIA Objective 1.5; Professor Messer 220-1202 v1.40 p. 10 | Network Commands | 1.5-T019 | Command | N/A; exact command recall only, Basic duplicate removed | Self-reviewed |
| `netstat` | CompTIA Objective 1.5; Professor Messer 220-1202 v1.40 p. 10 | Network Commands | 1.5-B020, 1.5-T020 | Basic, Command | N/A | Self-reviewed |
| `nslookup` | CompTIA Objective 1.5; Professor Messer 220-1202 v1.40 p. 10 | Network Commands | 1.5-T021 | Command | N/A; exact command recall only, Basic duplicate removed | Self-reviewed |
| `net use` | CompTIA Objective 1.5; Professor Messer 220-1202 v1.40 p. 10 | Network Commands | 1.5-B022, 1.5-T022 | Basic, Command | N/A; Basic tests `net use`/`net user` distinction, Command tests exact recall | Self-reviewed |
| `tracert` | CompTIA Objective 1.5; Professor Messer 220-1202 v1.40 p. 10 | Network Commands | 1.5-B024, 1.5-T024 | Basic, Command | N/A; Basic tests route-path selection, Command tests exact recall | Self-reviewed |
| `pathping` | CompTIA Objective 1.5; Professor Messer 220-1202 v1.40 p. 10 | Network Commands | 1.5-B025, 1.5-T025 | Basic, Command | N/A; Basic tests when route metrics are needed, Command tests exact recall | Self-reviewed |
| `copy` switches `/v` and `/y` | Professor Messer 220-1202 v1.40 p. 9 | Navigation and File Management | None | None | Study-guide omitted; not listed in official Objective 1.5 bullet scope and lower value than official file-management commands | Self-reviewed |
| `xcopy` | Professor Messer 220-1202 v1.40 p. 9 | Navigation and File Management | None | None | Mentioned only as a contrast for `robocopy`; not listed as an official Objective 1.5 bullet | Self-reviewed |

## HighYield review

| Card ID | Rubric justification | Review status |
| --- | --- | --- |
| 1.5-B005 | `chkdsk /f` is a common repair decision for logical file-system errors | Draft |
| 1.5-B006 | `chkdsk /r` is a common distinction from `/f` and includes bad-sector handling | Draft |
| 1.5-B007 | `format` is destructive and frequently confused with repair commands | Draft |
| 1.5-B008 | `diskpart` is a powerful disk configuration tool with data-loss risk | Draft |
| 1.5-B014 | `gpupdate` is a common Group Policy action command | Draft |
| 1.5-B015 | `gpresult` is a common Group Policy verification command | Draft |
| 1.5-B016 | `sfc /scannow` is a core Windows system-file integrity command | Draft |
| 1.5-B022 | `net use` is the Windows share mapping command | Draft |
| 1.5-B024 | `tracert` is the route-path command learners must distinguish from `ping` | Draft |
| 1.5-B025 | `pathping` combines route mapping with packet-loss and round-trip statistics | Draft |

## Research and extraction

- [x] The matching exam version and objective scope are confirmed.
- [x] Official CompTIA objective PDF scope was confirmed as the primary scope
      authority.
- [x] Professor Messer PDF validation/page references were confirmed as the
      approved secondary source after official scope was established.
- [x] Professor Messer practice exam PDF was used only as a private secondary
      gap-check source after official scope was established.
- [x] A practice-exam gap check was completed before draft acceptance review;
      it reinforced SFC, net use, diskpart, gpupdate, gpresult, tracert,
      chkdsk, robocopy, nslookup, netstat, and format coverage without being
      cited in card or study-guide source fields.
- [x] No new secondary source was used.
- [x] Sources were reviewed according to their defined scope and authoring roles.
- [x] Concepts were extracted without copying source language.
- [x] No unresolved source ambiguity was identified in this draft.
- [x] No ambiguity currently requires changelog escalation.

## Authoring

- [x] `study-guide.md` is written, sourced, and internally consistent.
- [x] Basic cards cover justified scenario and command-selection decisions.
- [x] Cloze cards are not used because exact command recall is better tested
      with Command cards for this objective.
- [x] Command cards cover justified exact typed command and command-form recall.
- [x] Image cards were considered and not created because visual recognition
      does not materially improve this objective.
- [x] `checklist.md` reflects the objective's actual concepts and coverage.
- [x] Instructor Notes add concise value rather than repeat answers.
- [x] Practice-test-relevant concepts were converted to cards when
      official-scope, source-supported, stable, and useful for recall or
      application.
- [x] Every HighYield card has reviewer agreement or a documented justification.
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
- [x] `pytest` and Ruff pass. Docusaurus checks are not applicable unless
      website files change.
- [x] Manual Anki smoke testing passed, including Basic and Command TSV import.

## Acceptance record

- Date accepted: 2026-07-12.
- Final card count: 15 Basic cards and 25 Command cards.
- Generated TSV output verified: `Basic.tsv` and `Command.tsv` exist for
      Objective 1.5; no `Cloze.tsv` or `Image.tsv` is expected for this
      objective.
- Manual Anki smoke test passed, including the typed Command note type import.
- Acceptance decision: Accepted.

## Peer review record

| Reviewer | Date | Result | Required Changes | Approval Status |
| --- | --- | --- | --- | --- |
| Self-review | 2026-07-12 | Draft authored from official Objective 1.5 and Messer pp. 9-10; practice gap check completed privately | Independent review, generated-output review, and acceptance still required | Needs independent review |
| Independent content review | 2026-07-12 | Duplicate Basic/Command learning targets fixed; objective ready for smoke testing | Remove duplicate Basic cards; rewrite remaining Basic cards for scenario, distinction, or safety decisions; tighten `net user` citation | Complete |
| Manual Anki smoke test | 2026-07-12 | Basic and Command TSV import passed | None | Accepted |
