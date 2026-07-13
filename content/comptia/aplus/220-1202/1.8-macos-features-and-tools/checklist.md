# Objective 1.8 completion checklist

**Objective status: ACCEPTED.** Core 2 Objective 1.8 has passed independent
review, blocker-fix verification, generated-output verification, and manual
Anki smoke testing.

Official context:

```text
Domain 1.0 Operating Systems, Objective 1.8: Explain common features and tools
of the macOS/desktop operating system.
```

Official bullet scope reviewed:

- Application installation and uninstallation: `.dmg`, `.pkg`, `.app`, App
  Store, and the uninstallation process.
- System folders: `/Applications`, `/Users`, `/Library`, `/System`, and the
  user-specific Library folder written in the official objectives as
  `/Users/Library`.
- Apple ID and corporate restrictions.
- Best practices: backups, antivirus, updates/patches, and Rapid Security
  Response (RSR).
- System Preferences areas: Displays, Networks, Printers, Scanners, Privacy,
  Accessibility, and Time Machine.
- Features and tools: multiple desktops, Mission Control, Keychain, Spotlight,
  iCloud services, gestures, Finder, Dock, Continuity, Disk Utility, FileVault,
  Terminal, and Force Quit.

Source terminology decisions:

- The official objectives list `/Users/Library`, while Professor Messer p. 15
  describes the user-specific location as `~/Library`, where `~` is the current
  user's home directory. Learner content uses `~/Library` and explains that it
  resolves to `/Users/<username>/Library` rather than treating
  `/Users/Library` as a literal shared path.
- The official objectives use `System Preferences`; Professor Messer uses both
  `System Preferences` and `System Settings`. Because the name varies by macOS
  release, learner content tests the stable purpose of each settings area and
  avoids volatile click paths.

## Coverage map

| Concept | Source | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- |
| `.dmg` disk image | CompTIA Objective 1.8; Messer p. 15 | Applications and File Types | 1.8-C001 | Cloze | N/A | Self-reviewed |
| `.pkg` installer package | CompTIA Objective 1.8; Messer p. 15 | Applications and File Types | 1.8-C002 | Cloze | N/A | Self-reviewed |
| `.app` application bundle | CompTIA Objective 1.8; Messer p. 15 | Applications and File Types | 1.8-C003 | Cloze | N/A | Self-reviewed |
| App Store and centralized updates | CompTIA Objective 1.8; Messer p. 15 | Applications and File Types | 1.8-B002 | Basic | N/A | Self-reviewed |
| Uninstallation process | CompTIA Objective 1.8; Messer p. 15 | Applications and File Types | 1.8-B001 | Basic | N/A | Self-reviewed |
| `/Applications` | CompTIA Objective 1.8; Messer p. 15 | Important System Folders and Accounts | 1.8-B003 | Basic | N/A | Self-reviewed |
| `/Users` | CompTIA Objective 1.8; Messer p. 15 | Important System Folders and Accounts | None | None | Study-guide context; the folder-to-user-home association is direct and a separate card would be low-value recall | Self-reviewed |
| Shared `/Library` versus user `~/Library` | CompTIA Objective 1.8; Messer p. 15 | Important System Folders and Accounts | 1.8-B004 | Basic | N/A | Self-reviewed |
| `/System` | CompTIA Objective 1.8; Messer p. 15 | Important System Folders and Accounts | None | None | Study-guide caution is sufficient; memorizing that OS files are under `/System` adds little application value | Self-reviewed |
| Personal versus Managed Apple ID | CompTIA Objective 1.8; Messer p. 15 | Important System Folders and Accounts | 1.8-B005 | Basic | N/A | Self-reviewed |
| Backups and Time Machine | CompTIA Objective 1.8; Messer pp. 15-16 | Maintenance and Best Practices | 1.8-B006 | Basic | N/A | Self-reviewed |
| Antivirus best practice | CompTIA Objective 1.8; Messer p. 16 | Maintenance and Best Practices | 1.8-B007 | Basic | N/A | Self-reviewed |
| Updates and patches | CompTIA Objective 1.8; Messer p. 16 | Maintenance and Best Practices | 1.8-B008 | Basic | General patching is taught with the distinctive RSR decision rather than duplicated as a second card | Self-reviewed |
| Rapid Security Response | CompTIA Objective 1.8; Messer p. 16 | Maintenance and Best Practices | 1.8-B008 | Basic | N/A | Self-reviewed |
| Displays settings | CompTIA Objective 1.8; Messer p. 16 | macOS Settings Areas | 1.8-B009 | Basic | N/A | Self-reviewed |
| Network settings | CompTIA Objective 1.8; Messer p. 16 | macOS Settings Areas | 1.8-B010 | Basic | N/A | Self-reviewed |
| Printers and scanners settings | CompTIA Objective 1.8; Messer p. 16 | macOS Settings Areas | 1.8-B011 | Basic | N/A | Self-reviewed |
| Privacy permissions | CompTIA Objective 1.8; Messer p. 16 | macOS Settings Areas | 1.8-B012 | Basic | N/A | Self-reviewed |
| Accessibility permissions | CompTIA Objective 1.8; Messer p. 16 | macOS Settings Areas | 1.8-B013 | Basic | N/A | Self-reviewed |
| Time Machine settings | CompTIA Objective 1.8; Messer p. 16 | macOS Settings Areas | 1.8-B006 | Basic | Covered with the Time Machine backup decision; a settings-only duplicate would add no new retrieval target | Self-reviewed |
| Multiple desktops/Spaces | CompTIA Objective 1.8; Messer p. 17 | Desktop and Search Features | 1.8-B014 | Basic | N/A | Self-reviewed |
| Mission Control | CompTIA Objective 1.8; Messer p. 17 | Desktop and Search Features | 1.8-B015 | Basic | N/A | Self-reviewed |
| Keychain | CompTIA Objective 1.8; Messer p. 17 | Accounts, Cloud Services, and Cross-Device Work | 1.8-B016 | Basic | N/A | Self-reviewed |
| Spotlight | CompTIA Objective 1.8; Messer p. 17 | Desktop and Search Features | 1.8-B017 | Basic | N/A | Self-reviewed |
| iCloud synchronization and Drive | CompTIA Objective 1.8; Messer p. 17 | Accounts, Cloud Services, and Cross-Device Work | 1.8-B018 | Basic | N/A | Self-reviewed |
| iMessage and FaceTime | CompTIA Objective 1.8; Messer p. 17 | Accounts, Cloud Services, and Cross-Device Work | None | None | Study-guide context is sufficient; messaging versus audio/video communication is self-evident and would create filler cards | Self-reviewed |
| Gestures | CompTIA Objective 1.8; Messer p. 17 | Desktop and Search Features | None | None | Customizable interaction context; exact gesture memorization is volatile and not required by official scope | Self-reviewed |
| Finder | CompTIA Objective 1.8; Messer p. 17 | Desktop and Search Features | 1.8-B019 | Basic | N/A | Self-reviewed |
| Dock | CompTIA Objective 1.8; Messer p. 17 | Desktop and Search Features | 1.8-B020 | Basic | N/A | Self-reviewed |
| Continuity | CompTIA Objective 1.8; Messer p. 17 | Accounts, Cloud Services, and Cross-Device Work | 1.8-B021 | Basic | N/A | Self-reviewed |
| Disk Utility | CompTIA Objective 1.8; Messer p. 17 | Administrative and Recovery Tools | 1.8-B022 | Basic | N/A | Self-reviewed |
| FileVault | CompTIA Objective 1.8; Messer p. 17 | Administrative and Recovery Tools | 1.8-B023 | Basic | N/A | Self-reviewed |
| Terminal | CompTIA Objective 1.8; Messer p. 18 | Administrative and Recovery Tools | 1.8-B024 | Basic | N/A | Self-reviewed |
| Force Quit | CompTIA Objective 1.8; Messer p. 18 | Administrative and Recovery Tools | 1.8-B025 | Basic | N/A | Self-reviewed |

## Objective-specific cautions

- Keep macOS feature explanation in Objective 1.8 separate from Linux command
  identification in Objective 1.9 and general application requirements in
  Objective 1.10.
- Do not over-card macOS-version-specific labels, click paths, gestures, or
  keyboard shortcuts.
- Do not interpret the official `/Users/Library` text as a literal path when
  explaining the user-specific Library folder; use the source-validated
  `~/Library` form and document the discrepancy.
- Distinguish Keychain credential storage from FileVault full-disk encryption.
- Do not imply that Disk Utility replaces backups or that moving every
  application to the Trash removes all software components.
- Treat Apple IDs and managed accounts as ownership and administration choices;
  avoid implementation detail not supported by the approved sources.

## HighYield review

| Card ID | Rubric justification | Review status |
| --- | --- | --- |
| 1.8-B001 | Correct application removal is a practical support task | Approved by independent review |
| 1.8-B003 | `/Applications` recognition is a core macOS support distinction reinforced by the private gap check | Approved by independent review |
| 1.8-B006 | Time Machine is the central macOS backup and restore feature and is reinforced by the private gap check | Approved by independent review |
| 1.8-B008 | RSR is an explicit security-update distinction reinforced by the private gap check | Approved by independent review |
| 1.8-B012 | Per-app privacy permissions are a common security and support decision | Approved by independent review |
| 1.8-B014 | Spaces is the core multiple-desktop feature | Approved by independent review |
| 1.8-B015 | Mission Control is commonly confused with Spaces and is central to desktop navigation | Approved by independent review |
| 1.8-B016 | Keychain is foundational credential protection and must be distinguished from disk encryption | Approved by independent review |
| 1.8-B017 | Spotlight is the standard macOS search feature | Approved by independent review |
| 1.8-B019 | Finder is the central macOS file-management tool | Approved by independent review |
| 1.8-B022 | Disk Utility is the core storage and disk-image management tool | Approved by independent review |
| 1.8-B023 | FileVault full-disk encryption is a central security feature reinforced by the private gap check | Approved by independent review |
| 1.8-B025 | Force Quit is a common first response to an unresponsive application | Approved by independent review |
| 1.8-C001 | `.dmg` recognition is a common macOS file-type distinction reinforced by the private gap check | Approved by independent review |
| 1.8-C002 | `.pkg` identifies an installer package, a core installation distinction | Approved by independent review |

## Research and extraction

- [x] The matching exam version and objective scope are confirmed.
- [x] Official CompTIA objective PDF scope was confirmed as the primary scope
      authority.
- [x] Professor Messer PDF validation and printed page references 15-18 were
      confirmed after official scope was established.
- [x] Professor Messer practice exam PDF was used only as a private secondary
      gap-check source after official scope was established.
- [x] The private gap check reinforced Time Machine, `/Applications`,
      FileVault, RSR, and `.dmg` recognition without supplying card wording or
      citations.
- [x] No new secondary source was used.
- [x] Sources were reviewed according to their defined roles.
- [x] Concepts were extracted without copying source language.
- [x] The user-Library path and settings-label ambiguities are documented and
      resolved without guessing.

## Authoring

- [x] `study-guide.md` is written, sourced, and internally consistent.
- [x] Basic cards cover justified explanation, comparison, and short
      application needs.
- [x] Cloze cards are limited to the three compact application file-type
      associations.
- [x] Command cards are not used because Objective 1.8 asks for tool purposes,
      not exact command entry.
- [x] Image cards were considered and not created because visual recognition
      does not materially improve these file, setting, and utility concepts.
- [x] `checklist.md` reflects the objective's concepts and dispositions.
- [x] Instructor Notes add distinctions or support context.
- [x] Practice-gap concepts that are official-scope, source-supported, stable,
      and useful for recall or application have cards.
- [x] Every HighYield decision has independent reviewer agreement.
- [x] Custom tags and stable IDs follow repository rules.
- [x] `changelog.md` records this draft.

## Review and build

- [x] Every factual claim and card has a reviewable approved source.
- [x] Cards have passed independent review for accuracy, atomicity, wording,
      omissions, and ambiguity.
- [x] Original diagrams are not applicable; no image cards were created.
- [x] `.venv/bin/python scripts/validate.py` passes without unexplained warnings.
- [x] `.venv/bin/python scripts/build.py` passes and removes no expected output.
- [x] Generated TSV changes are verified with their Markdown sources:
      `Basic.tsv` contains 25 data rows and `Cloze.tsv` contains three.
- [x] The 89-test pytest suite and Ruff lint and format checks pass.
- [x] Manual Anki smoke testing has passed for the generated Basic and Cloze
      TSV files.

## Acceptance record

- Date accepted: 2026-07-13.
- Final card count: 25 Basic cards and three Cloze cards, including 15
  HighYield cards.
- Generated TSV output verified: `Basic.tsv` contains 25 data rows and
  `Cloze.tsv` contains three; no Command or Image TSV is expected.
- Manual Anki smoke test: User-reported pass for Basic and Cloze imports on
  2026-07-13; headers were not imported as notes, HTML and Cloze rendered,
  Card ID supported update behavior, re-import created no duplicates, tags
  imported as Anki metadata, and observed counts matched 25 Basic and three
  Cloze notes. Anki version and disposable profile name were not provided.
- Media verification: Not applicable; Objective 1.8 has no Image cards.
- Acceptance decision: Accepted.

## Peer review record

| Reviewer | Date | Result | Required Changes | Approval Status |
| --- | --- | --- | --- | --- |
| Self-review | 2026-07-13 | Draft authored from official Objective 1.8 and Messer pp. 15-18; private practice gap check completed | Independent content review and manual Anki smoke test remain | Needs independent review |
| Independent content review | 2026-07-13 | Scope, omissions, card roles, redundancy, difficulty, tags, generated structure, and source fidelity reviewed; narrow unsupported explanatory details found | Remove unsupported uninstaller rationale, RSR release comparison, Spotlight indexing, Force Quit consequences/ranking, and backup-verification advice; regenerate output | Changes required; fixes applied pending verification |
| Blocker-fix verification | 2026-07-13 | All five source-fidelity blockers resolved; no new scope, source, redundancy, ID, or generated-output issues found | None | Approved |
| Manual Anki smoke test | 2026-07-13 | User-reported Basic and Cloze import, rendering, metadata tags, 28-note total, and Card ID re-import/update behavior passed; Anki version/profile not provided | None | Accepted |
