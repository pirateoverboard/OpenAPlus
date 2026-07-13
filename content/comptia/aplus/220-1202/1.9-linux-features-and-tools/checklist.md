# Objective 1.9 completion checklist

**Objective status: ACCEPTED.** Core 2 Objective 1.9 has passed independent
content review, blocker-fix verification, bloat review, generated-output
verification, and manual Anki smoke testing.

Official context:

```text
Domain 1.0 Operating Systems, Objective 1.9: Identify common features and tools
of the Linux client/desktop operating system.
```

Official bullet scope reviewed:

- File management: `ls`, `pwd`, `mv`, `cp`, `rm`, `chmod`, `chown`, `grep`,
  and `find`.
- Filesystem management: `fsck` and `mount`.
- Administrative: `su` and `sudo`.
- Package management: `apt` and `dnf`.
- Network: `ip`, `ping`, `curl`, `dig`, and `traceroute`.
- Informational: `man`, `cat`, `top`, `ps`, `du`, and `df`.
- Text editors: `nano`.
- Common configuration files: `/etc/passwd`, `/etc/shadow`, `/etc/hosts`,
  `/etc/fstab`, and `/etc/resolv.conf`.
- OS components: `systemd`, kernel, and bootloader.
- Root account.

Source-scope decision:

- Professor Messer p. 21 includes option-specific `ping` examples, while the
  official Objective 1.9 bullet names the base command. Learner recall is
  limited to the base command and its sourced reachability purpose.

## Coverage map

| Concept | Source | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- |
| `ls` | CompTIA Objective 1.9; Messer p. 19 | File and Directory Management | 1.9-T001 | Command | N/A | Self-reviewed |
| `pwd` | CompTIA Objective 1.9; Messer p. 19 | File and Directory Management | 1.9-T002 | Command | N/A | Self-reviewed |
| `mv` | CompTIA Objective 1.9; Messer p. 19 | File and Directory Management | 1.9-T003 | Command | N/A | Self-reviewed |
| `cp` | CompTIA Objective 1.9; Messer p. 19 | File and Directory Management | 1.9-T004 | Command | N/A | Self-reviewed |
| `rm` | CompTIA Objective 1.9; Messer p. 19 | File and Directory Management | 1.9-T005 | Command | N/A | Self-reviewed |
| `chmod` | CompTIA Objective 1.9; Messer p. 20 | File and Directory Management | 1.9-B001, 1.9-T006 | Basic, Command | N/A; Basic tests the permissions/ownership distinction | Self-reviewed |
| `chown` | CompTIA Objective 1.9; Messer pp. 19-20 | File and Directory Management | 1.9-B001, 1.9-T007 | Basic, Command | N/A; Basic tests the permissions/ownership distinction | Self-reviewed |
| `grep` | CompTIA Objective 1.9; Messer p. 19 | File and Directory Management | 1.9-B002, 1.9-T008 | Basic, Command | N/A; Basic tests content search versus pathname search | Self-reviewed |
| `find` | CompTIA Objective 1.9; Messer p. 20 | File and Directory Management | 1.9-B002, 1.9-T009 | Basic, Command | N/A; Basic tests content search versus pathname search | Self-reviewed |
| `fsck` | CompTIA Objective 1.9; Messer p. 20 | Filesystems and Storage | 1.9-T010 | Command | N/A | Self-reviewed |
| `mount` | CompTIA Objective 1.9; Messer p. 20 | Filesystems and Storage | 1.9-T011 | Command | N/A | Self-reviewed |
| `su` and `sudo` | CompTIA Objective 1.9; Messer p. 20 | Administrative Access | 1.9-B003, 1.9-T012, 1.9-T013 | Basic, Command | N/A; Basic tests scope of identity change | Self-reviewed |
| `apt` and `dnf` | CompTIA Objective 1.9; Messer p. 20 | Package Management | 1.9-T014, 1.9-T015 | Command | N/A; the redundant reverse-association Basic card was removed | Independently reviewed |
| `ip` | CompTIA Objective 1.9; Messer p. 21 | Network Tools | 1.9-T016 | Command | N/A | Self-reviewed |
| `ping` | CompTIA Objective 1.9; Messer p. 21 | Network Tools | 1.9-T017 | Command | N/A | Self-reviewed |
| `curl` | CompTIA Objective 1.9; Messer p. 21 | Network Tools | 1.9-T018 | Command | N/A | Self-reviewed |
| `dig` | CompTIA Objective 1.9; Messer p. 21 | Network Tools | 1.9-T019 | Command | N/A | Self-reviewed |
| `traceroute` | CompTIA Objective 1.9; Messer p. 21 | Network Tools | 1.9-T020 | Command | N/A | Self-reviewed |
| `man` | CompTIA Objective 1.9; Messer pp. 19, 21 | Information and Editing | 1.9-T021 | Command | N/A | Self-reviewed |
| `cat` | CompTIA Objective 1.9; Messer p. 21 | Information and Editing | 1.9-T022 | Command | N/A | Self-reviewed |
| `top` and `ps` | CompTIA Objective 1.9; Messer p. 21 | Information and Editing | 1.9-B005, 1.9-T023, 1.9-T024 | Basic, Command | N/A; Basic tests live view versus process listing | Self-reviewed |
| `du` and `df` | CompTIA Objective 1.9; Messer p. 21 | Filesystems and Storage | 1.9-B006, 1.9-T025, 1.9-T026 | Basic, Command | N/A; Basic tests used space versus free filesystem space | Self-reviewed |
| `nano` | CompTIA Objective 1.9; Messer p. 21 | Information and Editing | 1.9-T027 | Command | N/A | Self-reviewed |
| `/etc/passwd` | CompTIA Objective 1.9; Messer p. 19 | Common Configuration Files | 1.9-C001 | Cloze | N/A | Self-reviewed |
| `/etc/shadow` | CompTIA Objective 1.9; Messer p. 19 | Common Configuration Files | 1.9-C002 | Cloze | N/A | Self-reviewed |
| `/etc/hosts` | CompTIA Objective 1.9; Messer p. 19 | Common Configuration Files | 1.9-B007, 1.9-C003 | Basic, Cloze | N/A; Basic contrasts local mappings with resolver settings | Self-reviewed |
| `/etc/fstab` | CompTIA Objective 1.9; Messer p. 19 | Common Configuration Files | 1.9-C004 | Cloze | N/A | Self-reviewed |
| `/etc/resolv.conf` | CompTIA Objective 1.9; Messer p. 19 | Common Configuration Files | 1.9-B007, 1.9-C005 | Basic, Cloze | N/A; Basic contrasts resolver settings with local mappings | Self-reviewed |
| Bootloader | CompTIA Objective 1.9; Messer p. 18 | Linux OS Components | 1.9-B008 | Basic | N/A | Self-reviewed |
| Kernel | CompTIA Objective 1.9; Messer p. 18 | Linux OS Components | 1.9-B009 | Basic | N/A | Self-reviewed |
| `systemd` | CompTIA Objective 1.9; Messer p. 18 | Linux OS Components | 1.9-B010 | Basic | N/A | Self-reviewed |
| Root account | CompTIA Objective 1.9; Messer p. 18 | Administrative Access | 1.9-B011 | Basic | N/A | Self-reviewed |

## Objective-specific cautions

- Keep Linux feature identification separate from macOS tools in Objective 1.8
  and application-requirement decisions in Objective 1.10.
- Do not teach distribution-specific options when the official scope names only
  the base command.
- Do not expand `ping` recall beyond the base command named in the official
  objective.
- Distinguish permissions (`chmod`) from ownership (`chown`), filesystem free
  space (`df`) from item usage (`du`), and a live process view (`top`) from a
  process listing (`ps`).
- Treat root access as broad administrative authority, not an ordinary working
  identity.

## HighYield review

| Card ID | Rubric justification | Review status |
| --- | --- | --- |
| 1.9-B001 | Permissions versus ownership is a foundational Linux distinction | Approved by independent review |
| 1.9-B003 | `sudo` versus `su` is a common administrative-access distinction | Approved by independent review |
| 1.9-B005 | `top` versus `ps` is a practical process-inspection distinction | Approved by independent review |
| 1.9-B006 | `df` versus `du` is a common storage-triage distinction | Approved by independent review |
| 1.9-B007 | Local host mappings versus DNS resolver settings is a foundational network distinction | Approved by independent review |
| 1.9-B009 | The kernel is the foundational core of Linux | Approved by independent review |
| 1.9-B011 | Root authority is central to Linux administration and security | Approved by independent review |
| 1.9-C002 | Recognizing `/etc/shadow` protects against confusing hashes with general account data | Approved by independent review |
| 1.9-C004 | `/etc/fstab` is the central persistent mount configuration file | Approved by independent review |
| 1.9-T006 | `chmod` is a frequently used permission command reinforced by the private gap check | Approved by independent review |
| 1.9-T008 | `grep` is a foundational text-search tool reinforced by the private gap check | Approved by independent review |
| 1.9-T010 | `fsck` is the core filesystem-check command reinforced by the private gap check | Approved by independent review |
| 1.9-T013 | `sudo` is a foundational administrative command reinforced by the private gap check | Approved by independent review |
| 1.9-T015 | `dnf` is an explicit package-manager distinction reinforced by the private gap check | Approved by independent review |
| 1.9-T019 | `dig` is the Linux DNS-query tool reinforced by the private gap check | Approved by independent review |
| 1.9-T020 | `traceroute` is the route-discovery command reinforced by the private gap check | Approved by independent review |
| 1.9-T023 | `top` is the primary live process and resource view in this scope | Approved by independent review |
| 1.9-T027 | `nano` is the named text editor and is reinforced by the private gap check | Approved by independent review |

## Research and extraction

- [x] The matching exam version and objective scope are confirmed.
- [x] Official CompTIA objective PDF scope was confirmed as the primary scope
      authority.
- [x] Professor Messer PDF validation and printed page references 18-21 were
      confirmed after official scope was established.
- [x] Professor Messer practice exam PDF was used only as a private secondary
      gap-check source after official scope was established.
- [x] The private gap check reinforced permission, filesystem, package,
      text-search, text-editor, DNS, and route-discovery tools without supplying
      card wording or citations.
- [x] No new secondary source was used.
- [x] Sources were reviewed according to their defined roles.
- [x] Concepts were extracted without copying source language.
- [x] Option-specific `ping` examples are excluded because the official
      objective names only the base command.

## Authoring

- [x] `study-guide.md` is written, sourced, and internally consistent.
- [x] Basic cards cover justified distinctions and component recognition.
- [x] Cloze cards cover compact configuration-file associations.
- [x] Command cards cover all 27 officially named commands with exact base-name
      recall and no option-string trivia.
- [x] Image cards were considered and not created because visual recognition
      does not improve these command, file, and component associations.
- [x] `checklist.md` reflects the objective's concepts and dispositions.
- [x] Instructor Notes add distinctions or operational context.
- [x] Practice-gap concepts that are official-scope, source-supported, stable,
      and useful for recall or application have cards.
- [x] HighYield decisions have independent reviewer agreement.
- [x] Custom tags and stable IDs follow repository rules.
- [x] `changelog.md` records this draft.

## Review and build

- [x] Independent-review source-fidelity, redundancy, and answer-boundary
      blockers were fixed and passed blocker-fix verification.
- [x] Original diagrams are not applicable; no image cards were created.
- [x] `.venv/bin/python scripts/validate.py` passes without unexplained warnings.
- [x] `.venv/bin/python scripts/build.py` passes and removes no expected output.
- [x] Generated TSV changes were regenerated after review fixes:
      `Basic.tsv` contains 10 data rows, `Cloze.tsv` contains five, and
      `Command.tsv` contains 27.
- [x] The 90-test pytest suite and Ruff lint and format checks pass.
- [x] Manual Anki smoke testing passed for Basic, Cloze, and Command TSV files.

## Acceptance record

- Date accepted: 2026-07-13.
- Final card count: 10 Basic cards, five Cloze cards, and 27 Command cards,
  including 18 HighYield cards.
- Generated TSV output verified: `Basic.tsv` contains 10 data rows,
  `Cloze.tsv` contains five, and `Command.tsv` contains 27; no Image TSV is
  expected.
- Manual Anki smoke test: User-reported pass for Basic, Cloze, and Command
  imports on 2026-07-13; headers were not imported as notes, HTML and Cloze
  content rendered correctly, typed-answer comparison worked, Instructor Notes
  displayed after reveal, Card ID supported update behavior, re-import created
  no duplicates, tags imported as Anki metadata, and observed counts matched 10
  Basic, five Cloze, and 27 Command notes. Anki version and disposable profile
  name were not provided.
- Media verification: Not applicable; Objective 1.9 has no Image cards.
- Acceptance decision: Accepted.

## Peer review record

| Reviewer | Date | Result | Required Changes | Approval Status |
| --- | --- | --- | --- | --- |
| Self-review | 2026-07-13 | Draft authored from official Objective 1.9 and Messer pp. 18-21; private practice gap check completed | Independent content review and manual Anki smoke test remain | Needs independent review |
| Independent content review | 2026-07-13 | Official scope and generated structure were complete; source-fidelity, duplicate-learning-target, and exact Command-answer-boundary blockers were found | Source-narrow unsupported statements; delete 1.9-B004; rewrite 1.9-T014, 1.9-T018, and 1.9-T019; regenerate output | Changes required; fixes applied pending verification |
| Blocker-fix verification | 2026-07-13 | All source-fidelity, redundancy, prompt-boundary, documentation, and generated-output blockers were resolved without new issues | None | Approved |
| Bloat review | 2026-07-13 | All 42 cards reviewed; comparison Basics, compact configuration-file Clozes, and exact command-recall cards have distinct justified roles | None; no delete, rewrite, or merge candidates | Approved |
| Manual Anki smoke test | 2026-07-13 | User-reported Basic, Cloze, and Command import, rendering, metadata tags, typed answers, 42-note total, and Card ID re-import/update behavior passed; Anki version/profile not provided | None | Accepted |
