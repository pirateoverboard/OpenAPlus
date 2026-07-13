# Objective 1.10 completion checklist

**Objective status: ACCEPTED.** Core 2 Objective 1.10 has passed independent
content review, blocker-fix verification, generated-output verification, and
manual Anki smoke testing.

Official context:

```text
Domain 1.0 Operating Systems, Objective 1.10: Given a scenario, install
applications according to requirements.
```

Official bullet scope reviewed:

- System requirements for applications: 32-bit versus 64-bit dependent
  requirements, dedicated versus integrated graphics, VRAM, RAM, CPU, external
  hardware tokens, storage, and application-to-OS compatibility.
- Distribution methods: physical media versus mountable ISO file, downloadable
  package, and image deployment.
- Impact considerations for new applications: device, network, operation, and
  business.

Source-scope decisions:

- The official objective defines the installation-decision scope; Professor
  Messer pp. 22-23 validate the requirements, distribution, and impact details.
- The private practice-exam gap check reinforced 32-bit memory limits,
  application/OS architecture compatibility, and destination storage capacity.
  It did not supply card wording, scenarios, or citations.
- No source ambiguity remains unresolved.

## Coverage map

| Concept | Source | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- |
| 32-bit versus 64-bit application requirements | CompTIA Objective 1.10; Messer p. 22 | Operating system and architecture | 1.10-B001, 1.10-C001 | Basic, Cloze | N/A; Basic tests compatibility while Cloze tests the reinforced memory limit | Self-reviewed |
| Application-to-OS compatibility | CompTIA Objective 1.10; Messer p. 22 | Operating system and architecture | 1.10-B002 | Basic | N/A | Self-reviewed |
| Dedicated versus integrated graphics | CompTIA Objective 1.10; Messer p. 22 | CPU, RAM, graphics, and storage | 1.10-B003 | Basic | N/A | Self-reviewed |
| VRAM requirements | CompTIA Objective 1.10; Messer p. 22 | CPU, RAM, graphics, and storage | 1.10-B004 | Basic | N/A | Self-reviewed |
| RAM requirements | CompTIA Objective 1.10; Messer p. 22 | CPU, RAM, graphics, and storage | 1.10-B005 | Basic | N/A | Self-reviewed |
| CPU requirements | CompTIA Objective 1.10; Messer p. 22 | CPU, RAM, graphics, and storage | 1.10-B006 | Basic | N/A | Self-reviewed |
| External hardware tokens | CompTIA Objective 1.10; Messer p. 22 | External hardware tokens | 1.10-B007 | Basic | N/A | Self-reviewed |
| Storage requirements | CompTIA Objective 1.10; Messer p. 22 | CPU, RAM, graphics, and storage | 1.10-B008 | Basic | N/A | Self-reviewed |
| Physical media versus mountable ISO | CompTIA Objective 1.10; Messer p. 22 | Distribution Methods | 1.10-B009 | Basic | N/A | Self-reviewed |
| Downloadable package | CompTIA Objective 1.10; Messer p. 22 | Distribution Methods | 1.10-B010 | Basic | N/A | Self-reviewed |
| Image deployment | CompTIA Objective 1.10; Messer pp. 22-23 | Distribution Methods | 1.10-B011 | Basic | N/A | Self-reviewed |
| Device impact | CompTIA Objective 1.10; Messer p. 23 | Impact Considerations | 1.10-B012 | Basic | N/A | Self-reviewed |
| Network impact | CompTIA Objective 1.10; Messer p. 23 | Impact Considerations | 1.10-B013 | Basic | N/A | Self-reviewed |
| Operational impact | CompTIA Objective 1.10; Messer p. 23 | Impact Considerations | 1.10-B014 | Basic | N/A | Self-reviewed |
| Business impact | CompTIA Objective 1.10; Messer p. 23 | Impact Considerations | 1.10-B015 | Basic | N/A | Self-reviewed |
| Applications inherit the user's access | Messer p. 23 | Impact Considerations | None | None | Supporting installation-risk context; the four official impact cards provide the active-recall targets | Self-reviewed |

## Objective-specific cautions

- Keep local application requirements separate from cloud-productivity setup in
  Objective 1.11 and OS installation methods in Objective 1.2.
- Do not assume an application is compatible merely because the installer can
  be opened; verify OS version and architecture requirements.
- Do not over-card volatile vendor-specific minimum specifications or exact UI
  installation paths.
- Keep the four impact categories distinct without turning this objective into
  broad change-management or troubleshooting content.

## HighYield review

| Card ID | Rubric justification | Review status |
| --- | --- | --- |
| 1.10-B001 | Architecture compatibility is a central installation gate reinforced by the private gap check | Approved by independent review |
| 1.10-B003 | Integrated versus dedicated graphics is a central hardware-requirement distinction | Approved by independent review |
| 1.10-B005 | Available application RAM must account for the OS and concurrent workloads | Approved by independent review |
| 1.10-B008 | Destination capacity includes installed and working-data needs and was reinforced by the private gap check | Approved by independent review |
| 1.10-B011 | Image deployment is the main scalable distribution distinction in this objective | Approved by independent review |
| 1.10-B013 | Network permissions and internal-service access are practical installation-impact checks | Approved by independent review |
| 1.10-C001 | The approximate 4 GB 32-bit address-space limit is a compact exam-relevant fact reinforced by the private gap check | Approved by independent review |

## Research and extraction

- [x] The matching 220-1202 exam version and Objective 1.10 scope are confirmed.
- [x] The official CompTIA objective PDF was used as the primary scope authority.
- [x] Professor Messer v1.40 printed pages 22-23 were used only for approved
      secondary validation and page references.
- [x] The Professor Messer Core 2 practice exam was used only as a private
      secondary gap check after official scope was established.
- [x] Practice-gap concepts that were official-scope, source-supported, stable,
      and useful for recall were carded.
- [x] No new secondary source was used.
- [x] Concepts were extracted and expressed without copying source language.
- [x] No unresolved source ambiguity was found.

## Authoring

- [x] `study-guide.md` is written, sourced, and internally consistent.
- [x] Basic cards apply requirement, distribution, and impact decisions to
      concise scenarios matching the official objective wording.
- [x] The single Cloze card covers a compact 32-bit memory fact without
      duplicating the compatibility decision card.
- [x] Command cards were considered and not created because the objective does
      not require exact command recall.
- [x] Image cards were considered and not created because visual recognition
      does not improve these installation decisions.
- [x] Instructor Notes add a distinction, consequence, or decision boundary.
- [x] Custom tags and stable IDs follow repository rules.
- [x] This checklist records all study-guide-only context with a specific
      no-card reason.
- [x] `changelog.md` records the draft.

## Review and build

- [x] Independent review and blocker-fix verification confirmed accuracy,
      scope, atomicity, wording,
      redundancy, and HighYield classifications.
- [x] Original diagrams are not applicable; no image cards were created.
- [x] `.venv/bin/python scripts/validate.py` passes without unexplained warnings.
- [x] `.venv/bin/python scripts/build.py` passes and removes no expected output.
- [x] Generated TSV changes match the Markdown sources: `Basic.tsv` contains 15
      data rows and `Cloze.tsv` contains one; no Command, Image, or media output
      is expected.
- [x] The 91-test pytest suite and Ruff lint and format checks pass.
- [x] Manual Anki smoke testing passed for the generated Basic and Cloze files.

## Acceptance record

- Date accepted: 2026-07-13.
- Final card count: 15 Basic cards and one Cloze card, including seven
  HighYield cards.
- Generated TSV output verified: `Basic.tsv` contains 15 data rows and
  `Cloze.tsv` contains one; no Command, Image, or media output is expected.
- Manual Anki smoke test: User-reported pass for Basic and Cloze imports on
  2026-07-13; headers were not imported as notes, HTML and Cloze content
  rendered correctly, Instructor Notes displayed after answer reveal, Card ID
  supported update behavior, re-import created no duplicates, tags imported as
  Anki metadata, and observed counts matched 15 Basic and one Cloze note. Anki
  version and disposable profile name were not provided.
- Media verification: Not applicable; Objective 1.10 has no Image cards.
- Acceptance decision: Accepted.

## Peer review record

| Reviewer | Date | Result | Required Changes | Approval Status |
| --- | --- | --- | --- | --- |
| Self-review | 2026-07-13 | Draft authored from official Objective 1.10 and Messer pp. 22-23; private practice gap check completed | Independent content review and manual Anki smoke test remain | Needs independent review |
| Independent content review | 2026-07-13 | Official scope, coverage, source hierarchy, copyright safety, card roles, HighYield choices, and generated output passed; one address-space precision blocker was found | Correct the 32-bit address-space explanation; refine two difficulty ratings and the integrated-graphics note | Changes required; fixes applied pending verification |
| Blocker-fix verification | 2026-07-13 | Address count and byte capacity are now distinguished; recommended card refinements were applied; generated output and the full verification suite pass | None | Approved; ready for manual Anki smoke test |
| Manual Anki smoke test | 2026-07-13 | User-reported Basic and Cloze import, rendering, metadata tags, 16-note total, and Card ID re-import/update behavior passed; Anki version/profile not provided | None | Accepted |
