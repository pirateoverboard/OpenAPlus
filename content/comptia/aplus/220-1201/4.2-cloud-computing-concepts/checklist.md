# Objective 4.2 completion checklist

**Objective status: DRAFTED.** Objective 4.2 has source-backed draft content.
Generated TSV output and automated verification are complete.
Omitted-concepts review and independent content review required fixes are
complete. Manual Anki smoke testing is complete. Maintainer acceptance is still
pending.

## Official objective context

Domain 4.0 Virtualization and Cloud Computing, Objective 4.2: Summarize cloud
computing concepts.

Official bullet scope:

- Common cloud models
  - Private cloud
  - Public cloud
  - Hybrid cloud
  - Community cloud
  - Infrastructure as a service (IaaS)
  - Software as a service (SaaS)
  - Platform as a service (PaaS)
- Cloud characteristics
  - Shared resources vs. dedicated resources
  - Metered utilization, including ingress/egress
  - Elasticity
  - Availability
  - File synchronization
  - Multitenancy

## Domain mapping

| Folder | Domain | Required domain tag |
| --- | --- | --- |
| `4.2-cloud-computing-concepts` | Virtualization and Cloud Computing | `A+::220-1201::Domain4-VirtualizationCloud` |

## Scope decision

Objective 4.2 is driven by the official `Summarize` wording. Cards emphasize
recognition, comparison, concise explanations, and short scenario selection.
This is standard objective content, not troubleshooting-heavy material, so no
interview-practice directory was created.

## Objective-specific cautions

- Do not drift into cloud provider product catalogs or pricing tables.
- Do not expand into Kubernetes, container orchestration, migration planning,
  or cloud architecture certification depth.
- Keep DaaS/VDI as Objective 4.1 context unless a reviewer explicitly asks for
  a study-guide note.
- Do not treat practice-exam wording, examples, or answer choices as card
  source material.

## Coverage map with Messer validation

| Concept | Source | Messer Validation | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cloud computing overview and resource consumption | CompTIA 4.2; Messer v1.70 p.47 | Present, p.47 | Cloud Computing Overview | 4.2-B001 | Basic | N/A | Self-reviewed |
| Private cloud | CompTIA 4.2; Messer v1.70 pp.47-48; private practice gap check | Present, pp.47-48 | Deployment Models | 4.2-B002, 4.2-C001 | Basic, Cloze | N/A; recognition and compact definition are distinct | Self-reviewed |
| Public cloud | CompTIA 4.2; Messer v1.70 pp.47-48; private practice gap check | Present, pp.47-48 | Deployment Models | 4.2-B003, 4.2-C002 | Basic, Cloze | N/A; recognition and compact definition are distinct | Self-reviewed |
| Hybrid cloud | CompTIA 4.2; Messer v1.70 p.47; private practice gap check | Present, p.47 | Deployment Models | 4.2-B004, 4.2-C003 | Basic, Cloze | N/A; scenario selection and compact definition are distinct | Self-reviewed |
| Community cloud | CompTIA 4.2; Messer v1.70 p.47; private practice gap check | Present, p.47 | Deployment Models | 4.2-B005, 4.2-C004 | Basic, Cloze | N/A; recognition and compact definition are distinct | Self-reviewed |
| IaaS | CompTIA 4.2; Messer v1.70 p.47; private practice gap check | Present, p.47 | Service Models | 4.2-B006, 4.2-C005 | Basic, Cloze | N/A; responsibility model and acronym recall are distinct | Self-reviewed |
| PaaS | CompTIA 4.2; Messer v1.70 p.47; private practice gap check | Present, p.47 | Service Models | 4.2-B007, 4.2-C006 | Basic, Cloze | N/A; scenario selection and acronym recall are distinct | Self-reviewed |
| SaaS | CompTIA 4.2; Messer v1.70 p.47; private practice gap check | Present, p.47 | Service Models | 4.2-B008, 4.2-C007 | Basic, Cloze | N/A; scenario selection and acronym recall are distinct | Self-reviewed |
| Shared versus dedicated resources | CompTIA 4.2; Messer v1.70 p.48 | Present, p.48 | Resource and Cost Characteristics | 4.2-B009 | Basic | N/A | Self-reviewed |
| Metered utilization | CompTIA 4.2; Messer v1.70 p.48; private practice gap check | Present, p.48 | Resource and Cost Characteristics | 4.2-B010 | Basic | N/A | Self-reviewed |
| Ingress and egress | CompTIA 4.2; Messer v1.70 p.48 | Present, p.48 | Resource and Cost Characteristics | 4.2-B011, 4.2-C008 | Basic, Cloze | N/A; scenario/cost distinction and term recall are distinct | Self-reviewed |
| Non-metered utilization | Messer v1.70 p.48; private practice gap check | Present, p.48 | Resource and Cost Characteristics | 4.2-B012 | Basic | N/A; included as contrast to official metered-utilization scope | Self-reviewed |
| Elasticity | CompTIA 4.2; Messer v1.70 p.48; private practice gap check | Present, p.48 | Availability, Elasticity, Synchronization, and Multitenancy | 4.2-B013 | Basic | N/A | Self-reviewed |
| Availability | CompTIA 4.2; Messer v1.70 p.48; private practice gap check | Present, p.48 | Availability, Elasticity, Synchronization, and Multitenancy | 4.2-B014 | Basic | N/A | Self-reviewed |
| File synchronization | CompTIA 4.2; Messer v1.70 p.48; private practice gap check | Present, p.48 | Availability, Elasticity, Synchronization, and Multitenancy | 4.2-B015 | Basic | N/A | Self-reviewed |
| Multitenancy | CompTIA 4.2; Messer v1.70 p.48; private practice gap check | Present, p.48 | Availability, Elasticity, Synchronization, and Multitenancy | 4.2-B016 | Basic | N/A | Self-reviewed |
| Service-model responsibility shift | CompTIA 4.2; Messer v1.70 p.47 | Present, p.47 | Service Models | 4.2-B017 | Basic | N/A | Self-reviewed |
| Public cloud shared-resource scenario | CompTIA 4.2; Messer v1.70 p.48; private practice gap check | Present, p.48 | Resource and Cost Characteristics | 4.2-B018 | Basic | N/A | Self-reviewed |
| Elasticity versus availability distinction | CompTIA 4.2; Messer v1.70 p.48; private practice gap check | Present, p.48 | Availability, Elasticity, Synchronization, and Multitenancy | 4.2-B019 | Basic | N/A | Self-reviewed |
| Vendor pricing tables, named provider products, Kubernetes administration, cloud migration project planning, SLA math, and DaaS as a 4.2 service model | Messer v1.70 pp.47-48; adjacent Objective 4.1 | Present as examples/details or outside 4.2 scope | Scope Caveats | None | None | Omitted; product-specific, volatile, too advanced, or already covered under Objective 4.1 VDI context | Self-reviewed |

## HighYield review

| Card ID | Rubric justification | Review status |
| --- | --- | --- |
| 4.2-B002 | Private cloud recognition is an explicit deployment-model target | Needs reviewer agreement |
| 4.2-B003 | Public cloud recognition is an explicit deployment-model target | Needs reviewer agreement |
| 4.2-B004 | Hybrid cloud is a common exam distinction and practice-gap relevant | Needs reviewer agreement |
| 4.2-B005 | Community cloud is a common confusion point with public cloud | Needs reviewer agreement |
| 4.2-B006 | IaaS responsibility split is foundational to service models | Needs reviewer agreement |
| 4.2-B007 | PaaS is commonly confused with IaaS and SaaS | Needs reviewer agreement |
| 4.2-B008 | SaaS recognition is a common exam target | Needs reviewer agreement |
| 4.2-B010 | Metered utilization is explicit characteristic scope and practice-gap relevant | Needs reviewer agreement |
| 4.2-B011 | Ingress/egress is explicit objective scope | Needs reviewer agreement |
| 4.2-B013 | Elasticity is a core cloud characteristic and practice-gap relevant | Needs reviewer agreement |
| 4.2-B014 | Availability is a core cloud characteristic and practice-gap relevant | Needs reviewer agreement |
| 4.2-B016 | Multitenancy is explicit characteristic scope | Needs reviewer agreement |
| 4.2-B017 | Responsibility shift separates IaaS, PaaS, and SaaS decisions | Needs reviewer agreement |
| 4.2-B019 | Elasticity versus availability is a common distractor distinction | Needs reviewer agreement |
| 4.2-C005 | IaaS acronym recall supports service-model classification | Needs reviewer agreement |
| 4.2-C006 | PaaS acronym recall supports service-model classification | Needs reviewer agreement |
| 4.2-C007 | SaaS acronym recall supports service-model classification | Needs reviewer agreement |

## Omitted-concepts review

Omitted-concepts review found the intentionally not-carded details acceptable:
vendor pricing tables, named provider products, Kubernetes administration,
cloud migration project planning, detailed SLA math, and DaaS as a 4.2 service
model should remain omitted from Objective 4.2 cards.

## Independent content review

Independent content review found one required fix: `4.2-B001` over-narrowed the
cloud computing definition by implying cloud computing must be shared or
provider-managed. The card was rewritten to include public, private, hybrid,
and community cloud models without that implication.

## Source ambiguity

No unresolved content ambiguity was identified. The documented AGENTS path for
the official objectives PDF did not match the local filename, so the matching
private file `CompTIA A+ 220-1201 Exam Objectives (4.0).pdf` was used as the
official CompTIA v4.0 scope source.

## Research and extraction

- [x] Objective 4.2 title and slug selected from official objective scope and repository naming convention.
- [x] Official CompTIA 220-1201 v4.0 Objective 4.2 reviewed as the primary scope source.
- [x] Professor Messer 220-1201 v1.70 pages 47-48 reviewed privately for validation and page citations.
- [x] Professor Messer 220-1201 practice exams used only as a private gap check after official scope was confirmed.
- [x] Concepts extracted without copying source wording, diagrams, question wording, answer choices, or explanations.
- [x] Initial card and no-card decisions recorded.
- [x] Official objective domain, number, full phrase, and bullet scope recorded in this checklist.
- [x] No unresolved source conflict was guessed into content.

## Authoring

- [x] Study guide written with a References section.
- [x] Basic cards cover justified recognition, comparison, and scenario-selection needs.
- [x] Cloze cards cover justified compact acronym and term recall.
- [x] No image cards created in this initial draft; cloud model recognition does not require visual identification.
- [x] Instructor Notes add value on every production card.
- [x] HighYield decisions are documented for review.
- [x] No redundant learning targets intentionally retained.
- [x] Current draft card counts: 19 Basic, 8 Cloze, 0 Image.

## Review and build

- [x] Omitted-concepts review completed.
- [x] Independent content review completed; required fix applied.
- [x] `python scripts/validate.py` passes without unexplained warnings.
- [x] `python scripts/build.py` passes and generated output is regenerated.
- [x] `pytest` and Ruff checks pass.
- [x] Manual Anki smoke test passed.
- [ ] Objective accepted by maintainer.

## Manual Anki smoke test

Manual Anki smoke test passed on 2026-07-11 per maintainer report. Tested
generated Objective 4.2 TSV imports for 19 Basic notes and 8 Cloze notes.
Objective 4.2 has no Image cards, so Image.tsv/media smoke testing is not
applicable unless image cards are added later.

## Peer review record

| Reviewer | Date | Result | Required Changes | Approval Status |
| --- | --- | --- | --- | --- |
| Self-review | 2026-07-11 | Initial Objective 4.2 draft and coverage decisions completed | Validation, build, omitted-concepts review, independent review, verification, and any required Anki smoke test | Needs independent review |
| Codex omitted-concepts review | 2026-07-11 | Omitted-concepts decisions acceptable | None | Approved |
| Codex independent review | 2026-07-11 | One required wording fix found for `4.2-B001` | Broaden cloud computing definition; completed | Changes completed |
