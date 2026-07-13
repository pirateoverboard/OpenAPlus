# Objective 1.11 completion checklist

**Objective status: ACCEPTED.** Core 2 Objective 1.11 has passed independent
content review, generated-output verification, and manual Anki smoke testing.

Official context:

```text
Domain 1.0 Operating Systems, Objective 1.11: Given a scenario, install and
configure cloud-based productivity tools.
```

Official bullet scope reviewed:

- Email systems.
- Storage, including synchronization and folder settings.
- Collaboration tools: spreadsheets, videoconferencing, presentation tools,
  word processing tools, and instant messaging.
- Identity synchronization.
- Licensing assignment.

Source-scope decisions:

- The official objective defines the installation and configuration scope;
  Professor Messer p. 23 validates the cloud email, storage, collaboration,
  identity, and licensing concepts.
- The private Core 2 practice-exam gap check found no additional Objective 1.11
  concept that was both official-scope and independently supported by the
  approved notes. It supplied no card wording, scenarios, or citations.
- No source ambiguity remains unresolved.

## Coverage map

| Concept | Source | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- |
| Cloud email systems | CompTIA Objective 1.11; Messer p. 23 | Cloud Email Systems | 1.11-B001 | Basic | N/A | Self-reviewed |
| Storage synchronization across registered devices | CompTIA Objective 1.11; Messer p. 23 | Cloud Storage and Folder Settings | 1.11-B002 | Basic | N/A | Self-reviewed |
| Folder selection and local versus streaming access | CompTIA Objective 1.11; Messer p. 23 | Cloud Storage and Folder Settings | 1.11-B003 | Basic | N/A | Self-reviewed |
| Spreadsheet collaboration | CompTIA Objective 1.11; Messer p. 23 | Collaboration Tools | 1.11-B004 | Basic | N/A | Self-reviewed |
| Videoconferencing | CompTIA Objective 1.11; Messer p. 23 | Collaboration Tools | 1.11-B005 | Basic | N/A | Self-reviewed |
| Presentation tools | CompTIA Objective 1.11; Messer p. 23 | Collaboration Tools | 1.11-B006 | Basic | N/A | Self-reviewed |
| Word processing tools | CompTIA Objective 1.11; Messer p. 23 | Collaboration Tools | 1.11-B007 | Basic | N/A | Self-reviewed |
| Instant messaging | CompTIA Objective 1.11; Messer p. 23 | Collaboration Tools | 1.11-B008 | Basic | N/A | Self-reviewed |
| Identity synchronization | CompTIA Objective 1.11; Messer p. 23 | Identity Synchronization | 1.11-B009 | Basic | N/A | Self-reviewed |
| User-based cloud license assignment | CompTIA Objective 1.11; Messer p. 23 | Licensing Assignment | 1.11-B010 | Basic | N/A | Self-reviewed |
| Cloud scalability and consumption-based capacity | Messer p. 23 | None | None | None | General cloud context rather than an Objective 1.11 installation/configuration target | Self-reviewed |
| Vendor examples and provider-specific setup paths | Messer p. 23 | Cloud Email Systems | None | None | Volatile examples; stable service roles and configuration decisions are carded | Self-reviewed |

## Objective-specific cautions

- Keep productivity-tool configuration separate from local application
  installation requirements in Objective 1.10 and general cloud-computing
  models in Core 1 Objective 4.2.
- Do not over-card vendor names, subscription tiers, storage quotas, or UI
  paths that can change.
- Distinguish synchronized identity from application authorization: an account
  may exist before a license is assigned.

## HighYield review

| Card ID | Rubric justification | Review status |
| --- | --- | --- |
| 1.11-B001 | Cloud email is a central service-selection target in the objective | Approved by independent review |
| 1.11-B002 | File synchronization is the central cloud-storage behavior named in scope | Approved by independent review |
| 1.11-B003 | Local versus streaming folder access is a practical configuration decision | Approved by independent review |
| 1.11-B009 | Identity synchronization is a foundational account-management distinction | Approved by independent review |
| 1.11-B010 | License assignment is a required access check distinct from identity creation | Approved by independent review |

## Research and extraction

- [x] The matching 220-1202 exam version and Objective 1.11 scope are confirmed.
- [x] The official CompTIA objective PDF was used as the primary scope authority.
- [x] Professor Messer v1.40 printed page 23 was used only for approved
      secondary validation and page references.
- [x] The Professor Messer Core 2 practice exam was used only as a private
      secondary gap check after official scope was established.
- [x] No practice-gap concept required an additional card.
- [x] No new secondary source was used.
- [x] Concepts were extracted and expressed without copying source language.
- [x] No unresolved source ambiguity was found.

## Authoring

- [x] `study-guide.md` is written, sourced, and internally consistent.
- [x] Basic cards use concise configuration and tool-selection scenarios that
      match the official objective wording.
- [x] Cloze cards were considered and not created because the objective's useful
      targets are applied selections rather than compact memorization facts.
- [x] Command cards were considered and not created because no exact command or
      launch-name recall is required.
- [x] Image cards were considered and not created because visual recognition
      does not improve these configuration decisions.
- [x] Instructor Notes add a distinction, consequence, or decision boundary.
- [x] Custom tags and stable IDs follow repository rules.
- [x] This checklist records study-guide-only and omitted context with specific
      no-card reasons.
- [x] `changelog.md` records the draft.

## Review and build

- [x] Independent review has confirmed accuracy, scope, atomicity, wording,
      redundancy, and HighYield classifications.
- [x] Original diagrams are not applicable; no image cards were created.
- [x] `.venv/bin/python scripts/validate.py` passes without unexplained warnings.
- [x] `.venv/bin/python scripts/build.py` passes and removes no expected output.
- [x] Generated TSV changes match the Markdown sources: `Basic.tsv` contains ten
      data rows; no Cloze, Command, Image, or media output is expected.
- [x] The 92-test pytest suite and Ruff lint and format checks pass.
- [x] Manual Anki smoke testing passes for the generated Basic file.

## Acceptance record

- Date accepted: 2026-07-13.
- Final card count: Ten Basic cards, including five HighYield cards.
- Generated TSV output: `Basic.tsv` contains ten verified data rows; no Cloze,
  Command, Image, or media output is expected.
- Manual Anki smoke test: User-reported pass for the Basic import on 2026-07-13;
  headers were not imported as notes, HTML rendered correctly, Instructor Notes
  displayed after answer reveal, Card ID supported update behavior, re-import
  created no duplicates, tags imported as Anki metadata, and the observed count
  matched ten Basic notes. The Anki version and disposable profile name were
  not provided.
- Media verification: Not applicable; Objective 1.11 has no Image cards.
- Acceptance decision: Accepted.

## Peer review record

| Reviewer | Date | Result | Required Changes | Approval Status |
| --- | --- | --- | --- | --- |
| Self-review | 2026-07-13 | Draft authored from official Objective 1.11 and Messer p. 23; private practice gap check completed | Independent content review and manual Anki smoke test remain | Needs independent review |
| Independent content review | 2026-07-13 | GO; official scope, source hierarchy, copyright safety, coverage, card quality, omissions, HighYield choices, and generated output passed | None; removing the obsolete cards placeholder was recommended | Approved; ready for manual Anki smoke test |
| Manual Anki smoke test | 2026-07-13 | User-reported Basic import, rendering, metadata tags, ten-note total, and Card ID re-import/update behavior passed; Anki version/profile not provided | None | Accepted |
