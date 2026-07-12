# Changelog

## 2026-07-12 - Objective 1.1 accepted

- Objective 1.1 accepted after independent-review fixes and manual Anki smoke
  testing.
- Manual Anki smoke test: Passed in the `OpenAPlus Import Test` profile/deck.
- Basic and Cloze TSV imports verified with custom OpenAPlus Basic and Cloze
  note types.
- Expected note count: 23; actual note count: 23.
- Basic note count: 15; Cloze note count: 8.
- Image import and media rendering were not applicable because this objective
  has no Image cards.
- Import headers were not imported as notes.
- Card ID was first field and used for duplicate/update behavior.
- HTML rendered correctly.
- Cloze cards generated correctly.
- Instructor Notes displayed correctly after answer reveal.
- Tags imported correctly as Anki metadata, not learner-facing fields.
- Re-import updated existing notes instead of duplicating them.
- No Objective 1.2 content was created.

## 2026-07-12 - Independent-review fixes

- Rewrote `1.1-B006` from duplicate iPadOS direct recall into a distinct
  iOS/iPadOS/Android platform-comparison card.
- Added the official Objective 1.1 bullet scope to `checklist.md`.
- Reclassified direct-recognition Basic cards `1.1-B002`, `1.1-B003`,
  `1.1-B004`, `1.1-B005`, `1.1-B012`, and `1.1-B013` from Medium to Easy.

## 2026-07-12 - Objective 1.1 draft authoring

- Added the Core 2 Objective 1.1 study guide for OS purpose, workstation OSs,
  mobile OSs, filesystems, lifecycle limits, and cross-OS compatibility.
- Added 15 Basic cards and 8 Cloze cards.
- Used CompTIA A+ 220-1202 Exam Objectives v4.0 Objective 1.1 as the primary
  scope authority.
- Used Professor Messer 220-1202 v1.40 pages 1-2 as the approved secondary
  validation/page-reference source.
- Completed a private Professor Messer Core 2 practice-exam gap check; it
  reinforced filesystem selection and cross-OS compatibility coverage without
  being cited in card or study-guide source fields.
- Image cards were considered and omitted because this objective does not need
  visual recognition.

### Scope and source decisions

- Vendor app-store and mobile development details remain study-guide context
  rather than card targets because they are supporting details under the broader
  OS-purpose objective.
- Exact vendor update mechanisms were not carded because lifecycle and update
  limitation risk is the stable objective-level learning target.
- No new secondary sources were used.
