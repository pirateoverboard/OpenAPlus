# Changelog

## 2026-07-12 - Objective 1.3 accepted

- Objective 1.3 accepted after independent-review fixes and manual Anki smoke
  testing.
- Manual Anki smoke test: Passed in the `OpenAPlus Import Test` profile/deck.
- Basic and Cloze TSV imports verified with custom OpenAPlus Basic and Cloze
  note types.
- Expected note count: 20; actual note count: 20.
- Basic note count: 16; Cloze note count: 4.
- Image import and media rendering were not applicable because this objective
  has no Image cards.
- Import headers were not imported as notes.
- Card ID was first field and used for duplicate/update behavior.
- HTML rendered correctly.
- Cloze cards generated correctly.
- Instructor Notes displayed correctly after answer reveal.
- Tags imported correctly as Anki metadata, not learner-facing fields.
- Re-import updated existing notes instead of duplicating them.
- No Objective 1.4 content was created.

## 2026-07-12 - Independent-review fixes

- Removed duplicate Cloze cards `1.3-C001`, `1.3-C002`, and `1.3-C004`; the
  corresponding Basic cards remain as the reviewed learning targets for Windows
  N editions, RDP host availability, and BitLocker.
- Updated `checklist.md` coverage rows to reflect the removed duplicate Cloze
  cards.
- Revised the Objective 1.3 draft count to 16 Basic cards and 4 Cloze cards.

## 2026-07-12 - Objective 1.3 draft authoring

- Added the Core 2 Objective 1.3 study guide for Windows editions, N editions,
  feature differences, upgrade paths, and Windows 11 hardware requirements.
- Added 16 Basic cards and 4 Cloze cards after independent-review duplicate
  removal.
- Used CompTIA A+ 220-1202 Exam Objectives v4.0 Objective 1.3 as the primary
  scope authority.
- Used Professor Messer 220-1202 v1.40 pages 4-6 as the approved secondary
  validation/page-reference source.
- Completed a private Professor Messer Core 2 practice-exam gap check; it
  reinforced BitLocker, domain/workgroup, RDP, Windows N editions, and
  upgrade/hardware-requirement coverage without being cited in card or
  study-guide source fields.
- Image cards were considered and omitted because this objective does not need
  visual recognition.

### Scope and source decisions

- Exact Windows release dates, release counts, and support end dates were left
  study-guide-only or omitted from cards because they are volatile and not
  necessary for the official compare-and-contrast task.
- Specific Enterprise feature examples and Windows 11 interface examples remain
  study-guide context because the stable active-recall target is the edition or
  feature-category selection.
- No new secondary sources were used.
