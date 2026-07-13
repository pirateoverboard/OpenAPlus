# Changelog

## 2026-07-13 - Acceptance

- Recorded the user-reported passing manual Anki smoke test for Objective 1.8
  Basic and Cloze imports, including headers, rendered HTML and Cloze content,
  metadata tags, the 28-note total, and Card ID re-import/update behavior
  without duplicates. The Anki version and disposable profile name were not
  provided.
- Accepted the final Objective 1.8 card set: 25 Basic cards and three Cloze
  cards, including 15 HighYield cards.
- Verified generated output expectations: `Basic.tsv` contains 25 data rows and
  `Cloze.tsv` contains three; no Command, Image, or media output is expected.
- Confirmed the custom OpenAPlus Basic and Cloze note types passed the
  applicable import checks and tags were imported as Anki metadata.
- Confirmed that no Objective 1.9 content was created.

## 2026-07-13 - Independent-review fixes

- Removed unsupported causal claims connecting dedicated uninstallers to files
  outside the application bundle while retaining the source-backed rule to use
  a separate uninstaller when one is provided.
- Reworded RSR coverage to the source-backed purpose of addressing urgent
  security issues without comparing its timing to feature releases.
- Removed the unsupported `indexed` qualifier from Spotlight coverage.
- Narrowed Force Quit coverage to its source-backed purpose of stopping a
  selected application, without asserting restart priority or unsaved-work
  consequences.
- Removed unsupported backup-verification advice from the Time Machine section.
- Preserved all 28 stable card IDs and the 25 Basic/three Cloze card counts.

## 2026-07-13 - Objective 1.8 draft authoring

- Added the Core 2 Objective 1.8 study guide for common macOS desktop features
  and tools.
- Added 25 Basic cards and three Cloze cards covering application file types,
  removal and storage locations, account management, maintenance practices,
  settings areas, desktop features, cloud integration, security, and
  administrative tools.
- Used CompTIA A+ 220-1202 Exam Objectives v4.0 Objective 1.8 as the primary
  scope authority.
- Used Professor Messer 220-1202 v1.40 pages 15-18 as the approved secondary
  validation and page-reference source.
- Completed a private Professor Messer Core 2 practice-exam gap check; it
  reinforced Time Machine, `/Applications`, FileVault, RSR, and `.dmg`
  recognition without supplying card wording or citations.
- Added generated domain and `Source::Messer-v140` tag support for the Objective
  1.8 directory, with documentation and a pipeline test.
- Generated and verified `Basic.tsv` with 25 data rows and `Cloze.tsv` with
  three data rows; no Command, Image, or media output is expected.
- Passed validation, build, the 89-test pytest suite, Ruff lint, and Ruff format
  checks.

### Scope and source decisions

- Learner content uses `~/Library` for the current user's Library folder and
  documents that it resolves beneath `/Users/<username>`; this reconciles the
  official `/Users/Library` bullet with the approved notes.
- Learner content describes stable settings functions without relying on the
  version-dependent `System Preferences` versus `System Settings` label or
  exact click paths.
- `/Users`, `/System`, gestures, iMessage, and FaceTime remain study-guide-only
  with explicit checklist reasons rather than generating low-value or volatile
  cards.
- Cloze is used only for `.dmg`, `.pkg`, and `.app` associations. Basic cards
  test explanations, comparisons, or practical feature selection, so no
  Basic/Cloze duplicate learning targets were intentionally created.
- Command and Image cards were considered and omitted because exact typed
  commands and visual identification are not the intended Objective 1.8 tasks.
- No new secondary sources were used.
