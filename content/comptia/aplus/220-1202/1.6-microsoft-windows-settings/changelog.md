# Changelog

## 2026-07-13 - Acceptance

- Recorded passing manual Anki smoke testing for Objective 1.6 Basic TSV
  import, including headers, rendered HTML, metadata tags, and Card ID update
  behavior.
- Verified the independent-review fixes and completed the bloat review with no
  delete or merge candidates.
- Accepted the final Objective 1.6 card set: 30 Basic cards.
- Verified generated output expectations: `Basic.tsv` contains 30 data rows;
  no Cloze, Command, Image, or media output is expected.

## 2026-07-13 - Independent and bloat review fixes

- Removed an unsupported claim that lid-close behavior can differ by power
  source while preserving the source-backed docking-station scenario.
- Narrowed the Fast Startup card and study-guide wording to the approved source
  boundary: Fast Startup uses hibernation and can be enabled or disabled during
  startup troubleshooting.
- Recorded that the official objective PDF says `Program and Features`, while
  Professor Messer page 11 validates the Windows applet name `Programs and
  Features`; learner-facing content uses the validated applet name without
  changing objective scope.
- Recorded the bloat-review result: all 30 cards should remain, with no delete
  or merge candidates.

## 2026-07-13 - Objective 1.6 draft authoring

- Added the Core 2 Objective 1.6 study guide for Microsoft Windows settings.
- Added Basic cards for scenario-based selection of Control Panel applets,
  File Explorer settings, power settings, accessibility options, and Windows
  Settings categories.
- Used CompTIA A+ 220-1202 Exam Objectives v4.0 Objective 1.6 as the primary
  scope authority.
- Used Professor Messer 220-1202 v1.40 pages 11-13 as the approved secondary
  validation and page-reference source.
- Completed a private Professor Messer Core 2 practice-exam gap check; it
  reinforced lid-close behavior, hidden and protected files, Fast Startup,
  remote settings through System, and optional Windows features without being
  cited in card or study-guide source fields.
- Considered Cloze, Command, and Image cards and omitted them because this
  objective tests configuration-destination selection rather than compact
  fact recall, exact command entry, or visual identification.

### Scope and source decisions

- Practice-exam content was used only as a private gap check and did not define
  scope or supply card wording.
- Control Panel and Windows Settings layouts vary by Windows release, so the
  content emphasizes stable setting purposes rather than click-by-click paths.
- Administrative Tools, General options, and broad View options remain
  study-guide context because their useful subtools or specific view decisions
  are covered elsewhere and a generic recall card would be too broad.
- No new secondary sources were used.
