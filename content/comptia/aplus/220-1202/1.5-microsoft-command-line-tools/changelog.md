# Changelog

## 2026-07-12 - Acceptance

- Recorded passing manual Anki smoke testing for Objective 1.5, including
  Basic and Command TSV import.
- Accepted the final Objective 1.5 card set: 15 Basic cards and 25 Command
  cards.
- Verified generated TSV output expectations: `Basic.tsv` and `Command.tsv`
  are expected; `Cloze.tsv` and `Image.tsv` are not expected for this
  objective.

## 2026-07-12 - Independent-review fixes

- Removed Basic cards that duplicated typed Command recall for `dir`, `cd`,
  `md`, `rmdir`, command help syntax, `hostname`, `winver`, `ipconfig`,
  `ping`, and `nslookup`.
- Rewrote the remaining Basic cards to test scenario decisions, command
  distinctions, or safety reasoning instead of exact typed command recall.
- Tightened `net user` citations to Professor Messer 220-1202 v1.40 page 10.
- Regenerated Objective 1.5 TSV output after the card-set changes.

## 2026-07-12 - Objective 1.5 draft authoring

- Added the Core 2 Objective 1.5 study guide for Microsoft command-line tools.
- Added Basic cards for scenario-based command selection, distinctions, and
  safety decisions across file management, disk management, informational, OS
  management, and network commands.
- Added Command cards for exact command and common command-form recall where
  typed entry is a useful skill.
- Removed Basic cards that only duplicated typed command recall for simple
  navigation, informational, and network command names.
- Used CompTIA A+ 220-1202 Exam Objectives v4.0 Objective 1.5 as the primary
  scope authority.
- Used Professor Messer 220-1202 v1.40 pages 9-10 as the approved secondary
  validation/page-reference source.
- Completed a private Professor Messer Core 2 practice-exam gap check; it
  reinforced SFC, net use, diskpart, gpupdate, gpresult, tracert, chkdsk,
  robocopy, nslookup, netstat, and format coverage without being cited in card
  or study-guide source fields.
- Image cards were considered and omitted because this objective tests command
  selection and typed command recall rather than visual recognition.

### Scope and source decisions

- Practice-exam content was used only as a private gap check and did not define
  scope or supply card wording.
- `copy`, `xcopy`, and switches outside the official Objective 1.5 list were
  not expanded into separate coverage targets unless needed to explain an
  official-scope command distinction.
- Exact command-name recall was carded as typed Command notes, while tool
  selection, contrast, and safety distinctions were carded as Basic notes.
- Tightened `net user` source references to Professor Messer 220-1202 v1.40
  page 10.
- No new secondary sources were used.
