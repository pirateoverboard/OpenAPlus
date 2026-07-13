# Changelog

## 2026-07-13 - Acceptance

- Recorded passing manual Anki smoke testing for Objective 1.7 Basic TSV
  import, including headers, rendered HTML, metadata tags, the 20-note count,
  and Card ID re-import/update behavior without duplicates.
- Accepted the final Objective 1.7 card set: 20 Basic cards, including 13
  HighYield cards.
- Verified generated output expectations: `Basic.tsv` contains 20 data rows;
  no Cloze, Command, Image, or media output is expected.
- Confirmed that no Objective 1.8 content was created.

## 2026-07-13 - Independent-review fixes

- Corrected source references to include Professor Messer printed page 15,
  where the Objective 1.7 continuation covers network paths, proxy settings,
  network profiles, and metered connections.
- Narrowed the mapped-drive references to the exact supporting printed pages
  13 and 15.
- Removed the unsupported requirement to configure a printer share name from
  `1.7-B004`; the card now tests the source-backed printer sharing property.
- Promoted `1.7-B004` to HighYield as recommended because shared-printer
  configuration is a common support task reinforced by the private gap check.
- Passed read-only blocker-fix verification with no remaining source, scope,
  redundancy, stable-ID, tag, or generated-output issues.

## 2026-07-13 - Objective 1.7 draft authoring

- Added the Core 2 Objective 1.7 study guide for Microsoft Windows client
  networking features.
- Added 20 Basic cards covering domain and workgroup selection, shared
  resources and network paths, local firewall decisions, client IP
  configuration, connection types, proxy settings, network profiles, and
  metered connections.
- Used CompTIA A+ 220-1202 Exam Objectives v4.0 Objective 1.7 as the primary
  scope authority.
- Used Professor Messer 220-1202 v1.40 pages 13-15 as the approved secondary
  validation and page-reference source.
- Completed a private Professor Messer Core 2 practice-exam gap check; it
  reinforced workgroups, shared printers, default gateways, VPNs, and metered
  connections without supplying card wording or citations.
- Added generated domain and `Source::Messer-v140` tag support for the new
  objective directory, with documentation and a pipeline test.
- Generated and verified `Basic.tsv` with 20 data rows; no Cloze, Command,
  Image, or media output is expected for this draft.
- Passed validation, build, the 88-test pytest suite, Ruff lint, and Ruff format
  checks.

### Scope and source decisions

- Practice-exam content was used only as a private gap check and did not define
  scope or supply card wording. A share-permission precedence concept was left
  to Objective 2.2, where the approved notes place it.
- The official objective expands DNS as `Domain Name System`, while Professor
  Messer page 14 says `Domain Name Services`; official wording controls all
  learner-facing content.
- Version-specific Settings paths, provider software, and detailed wireless
  authentication configuration remain supporting study-guide context rather
  than separate cards.
- Wired and wireless connection basics remain study-guide-only because cards
  asking learners to match Ethernet with a cable or Wi-Fi with an SSID would
  add low-value filler.
- Cloze, Command, and Image cards were considered and omitted because the
  objective tests scenario-based configuration selection rather than isolated
  sentence recall, exact command entry, or visual identification.
- No new secondary sources were used.
