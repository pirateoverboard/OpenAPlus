# Objective 1.2 completion checklist

**Objective status: DRAFT.** Core 2 Objective 1.2 has been authored and needs
independent review, generated-output review, and manual Anki acceptance work
before it can be accepted.

Official context:

```text
Domain 1.0 Operating Systems, Objective 1.2: Given a scenario, perform OS
installations and upgrades in a diverse environment.
```

Official scope categories reviewed: boot methods, installation types,
partitioning, drive format, upgrade considerations, feature updates, and product
life cycle.

Official bullet scope reviewed:

- Boot methods: USB, network, solid-state/flash drives, Internet-based,
  external/hot-swappable drive, internal hard drive partition, and multiboot.
- Installation types: clean install, upgrade, image deployment, remote network
  installation, zero-touch deployment, recovery partition, repair installation,
  and third-party driver considerations.
- Partitioning: GPT and MBR.
- Drive format.
- Upgrade considerations: backup files and user preferences, application and
  driver support/backward compatibility, and hardware compatibility.
- Feature updates and product life cycle.

## Coverage map

This map was created during card authoring and should be rechecked during
independent review.

| Concept | Source | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- |
| USB boot media requirements | Professor Messer 220-1202 v1.40 p. 3 | Boot Methods | 1.2-B001 | Basic | N/A | Self-reviewed |
| PXE/network installation | Professor Messer 220-1202 v1.40 p. 3 | Boot Methods | 1.2-B002, 1.2-C001 | Basic, Cloze | N/A; scenario selection and acronym recall are distinct | Self-reviewed |
| Solid-state and external/hot-swappable boot/install sources | Professor Messer 220-1202 v1.40 p. 3 | Boot Methods | 1.2-B017 | Basic | N/A | Self-reviewed |
| Internet-based installation source | Professor Messer 220-1202 v1.40 p. 3 | Boot Methods | 1.2-B018 | Basic | N/A | Self-reviewed |
| Internal drive partitions and multiboot | Professor Messer 220-1202 v1.40 p. 3 | Boot Methods | 1.2-B003 | Basic | N/A | Self-reviewed |
| Clean install | Professor Messer 220-1202 v1.40 pp. 3-4 | Installation Types | 1.2-B004 | Basic | N/A | Self-reviewed |
| In-place upgrade | Professor Messer 220-1202 v1.40 p. 4 | Installation Types | 1.2-B005 | Basic | N/A | Self-reviewed |
| Image deployment | Professor Messer 220-1202 v1.40 p. 3 | Installation Types | 1.2-B006 | Basic | N/A | Self-reviewed |
| Remote network installation | Professor Messer 220-1202 v1.40 p. 3 | Installation Types | 1.2-B019 | Basic | N/A | Self-reviewed |
| Zero-touch deployment | Professor Messer 220-1202 v1.40 p. 3 | Installation Types | 1.2-B007 | Basic | N/A | Self-reviewed |
| Recovery partition | Professor Messer 220-1202 v1.40 p. 3 | Installation Types | 1.2-B008 | Basic | N/A | Self-reviewed |
| Repair installation | Professor Messer 220-1202 v1.40 p. 3 | Installation Types | 1.2-B009 | Basic | N/A | Self-reviewed |
| Third-party storage/controller drivers | Professor Messer 220-1202 v1.40 p. 3 | Installation Types | 1.2-B010 | Basic | N/A | Self-reviewed |
| GPT partition style | Professor Messer 220-1202 v1.40 pp. 3-4 | Partitioning | 1.2-B011, 1.2-C002, 1.2-C004 | Basic, Cloze | N/A; selection and acronym/UEFI recall are distinct | Self-reviewed |
| MBR partition style | Professor Messer 220-1202 v1.40 pp. 3-4 | Partitioning | 1.2-B012, 1.2-C003 | Basic, Cloze | N/A; limitation and acronym recall are distinct | Self-reviewed |
| Quick format versus full format | Professor Messer 220-1202 v1.40 p. 4 | Drive Format | 1.2-B013, 1.2-C006 | Basic, Cloze | N/A; choice and compact fact are distinct | Self-reviewed |
| Backup files and user preferences | Professor Messer 220-1202 v1.40 p. 4 | Upgrade Preparation | 1.2-B014 | Basic | N/A | Self-reviewed |
| Hardware, application, and driver compatibility checks | Professor Messer 220-1202 v1.40 p. 4 | Upgrade Preparation | 1.2-B015 | Basic | N/A | Self-reviewed |
| Quality updates, feature updates, and product life cycle | Professor Messer 220-1202 v1.40 p. 4 | Upgrade Preparation | 1.2-B016, 1.2-C007, 1.2-C008 | Basic, Cloze | N/A; lifecycle decision and compact update distinctions are distinct | Self-reviewed |
| Exact Windows support durations | Professor Messer 220-1202 v1.40 p. 4 | Upgrade Preparation | None | None | Version/edition-dependent context; lifecycle planning is the stable card target | Self-reviewed |

## HighYield review

| Card ID | Rubric justification | Review status |
| --- | --- | --- |
| 1.2-B004 | Clean install is a common destructive installation decision | Draft justification |
| 1.2-B005 | In-place upgrade is the main preservation-focused upgrade decision | Draft justification |
| 1.2-B006 | Image deployment is core to standardized endpoint rollout | Draft justification |
| 1.2-B007 | Zero-touch deployment is a common automated deployment scenario | Draft justification |
| 1.2-B010 | Third-party drivers can unblock storage visibility during installation | Draft justification |
| 1.2-B011 | GPT selection is a common partitioning decision | Draft justification |
| 1.2-B012 | MBR limitations are a common partitioning trap | Draft justification |
| 1.2-B014 | Backups are required before destructive install/upgrade work | Draft justification |
| 1.2-B015 | Compatibility checks prevent failed upgrades | Draft justification |

## Research and extraction

- [x] The matching exam version and objective scope are confirmed.
- [x] Official CompTIA objective PDF scope was confirmed as the primary scope
      authority.
- [x] Professor Messer PDF validation/page references were confirmed as the
      approved secondary source after official scope was established.
- [x] Professor Messer practice exam PDF was used only as a private secondary
      gap-check source after official scope was established.
- [x] A practice-exam gap check was completed before draft acceptance review;
      it reinforced GPT/MBR, third-party drivers, installation method choice,
      multiboot, zero-touch, and user-data preservation coverage.
- [x] No new secondary source was used.
- [x] Sources were reviewed according to their defined scope and authoring roles.
- [x] Concepts were extracted without copying source language.
- [x] No unresolved source ambiguity was identified in this draft.
- [x] No ambiguity currently requires changelog escalation.

## Authoring

- [x] `study-guide.md` is written, sourced, and internally consistent.
- [x] Basic cards cover justified scenario, selection, and comparison decisions.
- [x] Cloze cards cover justified compact recall without excessive deletions.
- [x] Image cards were considered and not created because visual recognition
      does not materially improve this objective.
- [x] `checklist.md` reflects the objective's actual concepts and coverage.
- [x] Instructor Notes add concise value rather than repeat answers.
- [x] Practice-test-relevant concepts were converted to cards when
      official-scope, source-supported, stable, and useful for recall or
      application.
- [ ] Every HighYield card has reviewer agreement or a documented approval.
- [x] Custom tags and stable IDs follow repository rules.
- [x] `changelog.md` records the objective's authoring changes.

## Review and build

- [ ] Every factual claim and card has been independently reviewed against a
      reviewable source.
- [ ] Cards were peer reviewed for accuracy, atomicity, wording, and ambiguity.
- [x] Original diagrams are not applicable; no image cards were created.
- [ ] `.venv/bin/python scripts/validate.py` passes without unexplained warnings.
- [ ] `.venv/bin/python scripts/build.py` passes and removes no expected output.
- [ ] Generated TSV changes are committed with their Markdown sources.
- [ ] `pytest`, Ruff, and Docusaurus checks pass as applicable.
- [ ] Manual Anki smoke testing is pending.

## Peer review record

| Reviewer | Date | Result | Required Changes | Approval Status |
| --- | --- | --- | --- | --- |
| Self-review | 2026-07-12 | Draft authored from official Objective 1.2 and Messer pp. 3-4; practice gap check completed privately | Independent review, generated-output review, and manual Anki acceptance still required | Needs independent review |
