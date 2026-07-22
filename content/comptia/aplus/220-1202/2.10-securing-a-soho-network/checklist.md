# Objective 2.10 completion checklist

**Objective status: ACCEPTED.** Core 2 Objective 2.10 has passed independent
content review, blocker-fix verification, generated-output verification, and
manual Anki smoke testing.

Official context:

```text
Domain 2.0 Security, Objective 2.10: Given a scenario, apply security settings
on SOHO wireless and wired networks.
```

Official bullet scope reviewed:

1. Router settings: change default passwords, IP filtering, firmware updates,
   content filtering, physical placement/secure locations, UPnP, screened
   subnet, and secure management access.
2. Wireless-specific settings: change the SSID, disable SSID broadcast,
   configure encryption settings, and configure guest access.
3. Firewall settings: disable unused ports and configure port
   forwarding/mapping.

Source-scope decisions:

- The official objective defines both the setting list and the applied
  `Given a scenario` learner task. Professor Messer pp. 46–47 validates the
  setting purposes, distinctions, and page references.
- The card set uses short selection and consequence scenarios rather than
  reproducing the official bullet list.
- The private Core 2 practice-exam gap check reinforced IP filtering for an
  address-based exclusion, changing default router credentials to protect
  configuration, and the limited discovery effect of disabling SSID broadcast.
  No published wording, scenario, answer choice, explanation, or citation was
  taken from it.
- Wireless protocol history and enterprise authentication depth remain under
  Objective 2.3; this objective cards only the configuration decision needed
  to secure a SOHO wireless network.
- No new secondary source was used, and no unresolved ambiguity blocks the
  supported card set.

## Coverage map

| Concept | Source | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- |
| Change default router passwords | CompTIA 2.10; Messer p. 46 | Protect the Router and Its Management Interface | 2.10-B001 | Basic | N/A | Self-reviewed |
| IP filtering and allow/deny decisions | CompTIA 2.10; Messer p. 46 | Filter Traffic for the Intended Result | 2.10-B002 | Basic | N/A | Self-reviewed |
| Firmware security updates | CompTIA 2.10; Messer p. 46 | Maintain and Physically Protect Network Equipment | 2.10-B003 | Basic | N/A | Self-reviewed |
| Content filtering | CompTIA 2.10; Messer p. 46 | Filter Traffic for the Intended Result | 2.10-B004 | Basic | N/A | Self-reviewed |
| Physical placement and secure location | CompTIA 2.10; Messer p. 46 | Maintain and Physically Protect Network Equipment | 2.10-B005 | Basic | N/A | Self-reviewed |
| UPnP automatic inbound openings | CompTIA 2.10; Messer p. 46 | Reduce Automatic and Public Exposure | 2.10-B006 | Basic | N/A | Self-reviewed |
| Screened subnet | CompTIA 2.10; Messer p. 46 | Reduce Automatic and Public Exposure | 2.10-B007 | Basic | N/A | Self-reviewed |
| Secure management access | CompTIA 2.10; Messer p. 46 | Protect the Router and Its Management Interface | 2.10-B008 | Basic | N/A | Self-reviewed |
| Change an identifying default SSID | CompTIA 2.10; Messer p. 46 | Configure the Wireless Network Deliberately | 2.10-B009 | Basic | N/A | Self-reviewed |
| Disable SSID broadcast and understand its limit | CompTIA 2.10; Messer p. 46 | Configure the Wireless Network Deliberately | 2.10-B010 | Basic | N/A | Self-reviewed |
| SOHO wireless encryption | CompTIA 2.10; Messer pp. 46–47 | Configure the Wireless Network Deliberately | 2.10-B011 | Basic | N/A | Self-reviewed |
| Guest access | CompTIA 2.10; Messer p. 47 | Configure the Wireless Network Deliberately | 2.10-B012 | Basic | N/A | Self-reviewed |
| Disable unused physical ports | CompTIA 2.10; Messer p. 47 | Limit Wired Ports and Firewall Mappings | 2.10-B013 | Basic | N/A | Self-reviewed |
| Port forwarding/mapping | CompTIA 2.10; Messer p. 47 | Limit Wired Ports and Firewall Mappings | 2.10-B014 | Basic | N/A | Self-reviewed |
| SSID and UPnP acronym expansions | Messer pp. 46–47 | Configure the Wireless Network Deliberately; Reduce Automatic and Public Exposure | None | None | The terms are explained in context; separate acronym cards would not improve the applied setting-selection task | Self-reviewed |
| WPA Enterprise authentication-server details | Messer p. 47; neighboring Objective 2.3 depth | Configure the Wireless Network Deliberately | None | None | Study-guide contrast only; separate enterprise-authentication recall belongs to Objective 2.3 | Self-reviewed |
| 802.1X network access control | Messer p. 47; supports CompTIA 2.10 disabling ports | Limit Wired Ports and Firewall Mappings | None | None | Supporting context; the official retrieval target is disabling unused ports, and separate authentication detail would expand into neighboring scope | Self-reviewed |
| Vendor-specific router menus, cloud logins, and update procedures | Messer p. 46 | None | None | None | Volatile implementation details are not required by the official objective | Self-reviewed |

## Objective-specific cautions

- Do not treat hiding an SSID as a replacement for wireless encryption.
- Do not confuse content filtering with an address-based IP filtering rule.
- Do not enable UPnP, remote management, guest access, unused physical ports,
  or port forwarding without a stated requirement.
- Do not expand this objective into wireless-protocol history or detailed
  enterprise authentication covered by neighboring objectives.
- Do not prescribe vendor-specific interface paths or firmware procedures.

## HighYield review

| Card IDs | Rubric justification | Review status |
| --- | --- | --- |
| 2.10-B001, 2.10-B003, 2.10-B006–B008, 2.10-B010–B014 | Central SOHO hardening decisions, exposure controls, and common configuration traps | Independent review approved |

## Research and extraction

- [x] The matching 220-1202 exam version and Objective 2.10 scope are confirmed.
- [x] The official CompTIA objective PDF was used as the primary scope authority.
- [x] Professor Messer v1.40 printed pages 46–47 were used only for approved
      secondary validation and page references.
- [x] The Professor Messer Core 2 practice exam was used only as a private
      secondary gap check after official scope was established.
- [x] Practice-gap concepts useful for active recall are carded.
- [x] No new secondary source was used.
- [x] Concepts were extracted and expressed without copying source language.
- [x] No unresolved source ambiguity was identified.

## Authoring

- [x] `study-guide.md` is written, sourced, and internally consistent.
- [x] Basic cards emphasize short setting-selection and consequence scenarios
      in line with the official `Given a scenario` wording.
- [x] Cloze cards were considered; acronym recall would not improve the applied
      task and would overlap with explained Basic-card concepts.
- [x] Command cards were considered and are not applicable.
- [x] Image cards were considered; visual recognition does not improve the
      configuration decisions in this objective.
- [x] Interview material was considered and is not justified by this scoped
      configuration objective.
- [x] Instructor Notes add a boundary, consequence, or nearby-setting contrast.
- [x] Custom tags and stable IDs follow repository rules.
- [x] Study-guide-only concepts have specific no-card reasons.
- [x] `changelog.md` records the draft.

## Review and build

- [x] Independent review confirms accuracy, scope, atomicity, wording,
      redundancy, omissions, and HighYield classifications.
- [x] Original diagrams are not applicable; no image cards were created.
- [x] `.venv/bin/python scripts/validate.py` passes without unexplained warnings.
- [x] `.venv/bin/python scripts/build.py` passes and removes no expected output.
- [x] Generated TSV changes match the Markdown sources: `Basic.tsv` contains 14
      data rows; no Cloze, Command, Image, or media output is expected.
- [x] The 102-test pytest suite and Ruff lint and format checks pass.
- [x] Manual Anki smoke testing passes for the generated Basic file.

## Acceptance record

- Date accepted: 2026-07-22.
- Final card count: 14 Basic cards, including 10 HighYield cards.
- Generated TSV output: `Basic.tsv` contains 14 verified data rows; no Cloze,
  Command, Image, or media output is expected.
- Manual Anki smoke test: User-reported pass on 2026-07-22 for the Basic
  import; headers were not imported as notes, HTML rendered correctly,
  Instructor Notes displayed after reveal, tags imported as Anki metadata,
  Card ID supported update behavior, re-import created no duplicates, and the
  observed count matched 14 Basic notes. The Anki version and disposable
  profile name were not provided.
- Media verification: Not applicable; Objective 2.10 has no Image cards.
- Acceptance decision: Accepted.

## Peer review record

| Reviewer | Date | Result | Required Changes | Approval Status |
| --- | --- | --- | --- | --- |
| Self-review | 2026-07-22 | Draft authored from official Objective 2.10 and Messer pp. 46–47; private practice gap check completed | Independent content review remains | Needs independent review |
| Independent content review | 2026-07-22 | NO-GO; found unsupported priority wording in B001 and an Easy/Medium rubric mismatch in B009; approved scope, sources, omissions, redundancy, and HighYield classifications | Remove `first` from B001 and change B009 to Medium | Changes required |
| Author fix pass | 2026-07-22 | Removed the unsupported priority from B001 and changed B009 to Medium | Blocker-fix verification remains | Needs blocker-fix verification |
| Blocker-fix verification | 2026-07-22 | GO; both blockers resolved with no new source, scope, redundancy, metadata, or generated-output issues | None | Approved; ready for manual Anki smoke test |
| Manual Anki smoke test | 2026-07-22 | User-reported Basic import, rendering, metadata tags, 14-note total, and Card ID re-import/update behavior passed; Anki version/profile not provided | None | Accepted |
