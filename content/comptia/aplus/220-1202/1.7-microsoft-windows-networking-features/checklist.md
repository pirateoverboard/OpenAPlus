# Objective 1.7 completion checklist

**Objective status: ACCEPTED.** Core 2 Objective 1.7 has passed independent
review, blocker-fix verification, generated-output verification, and manual
Anki smoke testing.

Official context:

```text
Domain 1.0 Operating Systems, Objective 1.7: Given a scenario, configure
Microsoft Windows networking features on a client/desktop.
```

Official bullet scope reviewed:

- Domain joined versus workgroup, including shared resources, printers, file
  servers, and mapped drives.
- Local OS firewall settings, including application restrictions and
  exceptions and configuration.
- Client network configuration: IP addressing scheme, DNS settings, subnet
  mask, gateway, and static versus dynamic configuration.
- Establish network connections: VPN, wireless, wired, and WWAN/cellular.
- Proxy settings.
- Public network versus private network.
- File Explorer navigation of network paths.
- Metered connections and limitations.

The official objective expands DNS as `Domain Name System`; Professor Messer
p. 14 labels it `Domain Name Services`. The official term controls, so learner
content uses `Domain Name System` while retaining Messer's validated
name-resolution function.

## Coverage map

| Concept | Source | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- |
| Domain-joined client | CompTIA Objective 1.7; Messer p. 13 | Domains, Workgroups, and Shared Resources | 1.7-B002 | Basic | N/A | Self-reviewed |
| Workgroup client | CompTIA Objective 1.7; Messer p. 13 | Domains, Workgroups, and Shared Resources | 1.7-B001 | Basic | N/A | Self-reviewed |
| Shared folders and file-server resources | CompTIA Objective 1.7; Messer p. 13 | Domains, Workgroups, and Shared Resources | 1.7-B003, 1.7-B005 | Basic | N/A | Self-reviewed |
| Shared printers | CompTIA Objective 1.7; Messer p. 13 | Domains, Workgroups, and Shared Resources | 1.7-B004 | Basic | N/A | Self-reviewed |
| Mapped drives | CompTIA Objective 1.7; Messer pp. 13 and 15 | Domains, Workgroups, and Shared Resources | 1.7-B003 | Basic | N/A | Self-reviewed |
| File Explorer network paths | CompTIA Objective 1.7; Messer p. 15 | Domains, Workgroups, and Shared Resources | 1.7-B005 | Basic | N/A | Self-reviewed |
| Hidden-share `$` suffix | Messer p. 13 | Domains, Workgroups, and Shared Resources | None | None | Supporting caution; hiding a share name is not a separate configuration skill | Self-reviewed |
| Firewall application restrictions and exceptions | CompTIA Objective 1.7; Messer p. 14 | Local Windows Firewall | 1.7-B006 | Basic | N/A | Self-reviewed |
| Firewall block-all-incoming setting | CompTIA Objective 1.7; Messer p. 14 | Local Windows Firewall | 1.7-B007 | Basic | N/A | Self-reviewed |
| Predefined versus custom firewall rules | CompTIA Objective 1.7; Messer p. 14 | Local Windows Firewall | 1.7-B008 | Basic | N/A | Self-reviewed |
| Firewall notifications and temporary disable option | CompTIA Objective 1.7; Messer p. 14 | Local Windows Firewall | None | None | Study-guide context; lower-value controls than safe exception and rule decisions | Self-reviewed |
| Dynamic addressing through DHCP | CompTIA Objective 1.7; Messer p. 14 | Client IP Configuration | 1.7-B009 | Basic | N/A | Self-reviewed |
| Static client addressing | CompTIA Objective 1.7; Messer p. 14 | Client IP Configuration | 1.7-B010 | Basic | N/A | Self-reviewed |
| APIPA fallback | Messer p. 14 | Client IP Configuration | 1.7-B011 | Basic | N/A | Self-reviewed |
| IP address purpose | CompTIA Objective 1.7; Messer p. 14 | Client IP Configuration | None | None | Study-guide context; the applied cards focus on choosing and interpreting configuration values | Self-reviewed |
| Subnet mask | CompTIA Objective 1.7; Messer p. 14 | Client IP Configuration | 1.7-B012 | Basic | N/A | Self-reviewed |
| Default gateway | CompTIA Objective 1.7; Messer p. 14 | Client IP Configuration | 1.7-B013 | Basic | N/A | Self-reviewed |
| DNS settings | CompTIA Objective 1.7; Messer p. 14 | Client IP Configuration | 1.7-B014 | Basic | N/A | Self-reviewed |
| Alternate static configuration | Messer p. 14 | Client IP Configuration | 1.7-B015 | Basic | N/A | Self-reviewed |
| VPN connection | CompTIA Objective 1.7; Messer p. 14 | Establishing Connections | 1.7-B016 | Basic | N/A | Self-reviewed |
| Wireless connection | CompTIA Objective 1.7; Messer p. 14 | Establishing Connections | None | None | Study-guide coverage is sufficient; choosing Wi-Fi when an SSID is the stated access method is self-evident and would be filler | Self-reviewed |
| Wired connection | CompTIA Objective 1.7; Messer p. 14 | Establishing Connections | None | None | Study-guide coverage is sufficient; choosing wired for a direct Ethernet cable is self-evident and would be filler | Self-reviewed |
| WWAN/cellular connection | CompTIA Objective 1.7; Messer p. 14 | Establishing Connections | 1.7-B017 | Basic | N/A | Self-reviewed |
| Wireless security fields and provider-specific WWAN setup | Messer p. 14 | Establishing Connections | None | None | Supporting, implementation-specific context; wireless security methods are covered elsewhere | Self-reviewed |
| Proxy settings and exceptions | CompTIA Objective 1.7; Messer p. 15 | Proxy, Network Profiles, and Metered Connections | 1.7-B018 | Basic | N/A | Self-reviewed |
| Public versus private network profile | CompTIA Objective 1.7; Messer pp. 14-15 | Proxy, Network Profiles, and Metered Connections | 1.7-B019 | Basic | N/A | Self-reviewed |
| Metered connections and limitations | CompTIA Objective 1.7; Messer p. 15 | Proxy, Network Profiles, and Metered Connections | 1.7-B020 | Basic | N/A | Self-reviewed |

## Objective-specific cautions

- Keep client configuration in Objective 1.7 separate from network-command
  troubleshooting in Objective 1.5 and Windows security permissions in
  Objective 2.2.
- Do not over-card Windows-version-specific click paths, provider software, or
  exact wireless-security setup screens.
- Treat a hidden share name as browsing convenience, not security.
- Prefer a targeted firewall exception or rule; do not normalize leaving the
  host firewall disabled.
- Use the official `Domain Name System` expansion despite the secondary
  source's `Domain Name Services` label.

## HighYield review

| Card ID | Rubric justification | Review status |
| --- | --- | --- |
| 1.7-B001 | Workgroup recognition is a central domain-versus-workgroup scenario | Approved by independent review |
| 1.7-B002 | Centralized domain authentication is a foundational Windows networking distinction | Approved by independent review |
| 1.7-B003 | Mapped drives are a common help-desk resource-access task | Approved by independent review |
| 1.7-B004 | Shared-printer configuration is a common support task reinforced by the private gap check | Approved by blocker-fix verification |
| 1.7-B006 | A targeted firewall exception is a practical, security-sensitive configuration decision | Approved by independent review |
| 1.7-B009 | DHCP is foundational to client address configuration | Approved by independent review |
| 1.7-B011 | APIPA is a common client-networking diagnostic clue | Approved by independent review |
| 1.7-B012 | Subnet-mask interpretation is foundational to local connectivity | Approved by independent review |
| 1.7-B013 | Default-gateway selection is foundational and reinforced by the private gap check | Approved by independent review |
| 1.7-B014 | DNS selection is foundational to name-resolution troubleshooting | Approved by independent review |
| 1.7-B016 | VPN selection is a common remote-work connection decision | Approved by independent review |
| 1.7-B019 | Public versus private profiles affect common sharing and firewall behavior | Approved by independent review |
| 1.7-B020 | Metered connections are an official limitation-management decision reinforced by the private gap check | Approved by independent review |

## Research and extraction

- [x] The matching exam version and objective scope are confirmed.
- [x] Official CompTIA objective PDF scope was confirmed as the primary scope
      authority.
- [x] Professor Messer PDF validation/page references were confirmed as the
      approved secondary source after official scope was established.
- [x] Professor Messer practice exam PDF was used only as a private secondary
      gap-check source after official scope was established.
- [x] A private practice-exam gap check reinforced workgroup selection, shared
      printer configuration, default-gateway purpose, VPN selection, and
      metered connections. A share-permission precedence item was not imported
      into Objective 1.7 because the approved notes place that concept under
      Objective 2.2.
- [x] No new secondary source was used.
- [x] Sources were reviewed according to their defined roles.
- [x] Concepts were extracted without copying source language.
- [x] The DNS expansion discrepancy is documented and resolved in favor of the
      official scope source.
- [x] No unresolved source ambiguity remains in this draft.

## Authoring

- [x] `study-guide.md` is written, sourced, and internally consistent.
- [x] Basic cards cover justified scenario and configuration-selection needs.
- [x] Cloze cards are not used because scenario-based feature selection is the
      intended learner task.
- [x] Command cards are not used because exact command entry belongs to
      Objective 1.5 and is not required here.
- [x] Image cards were considered and not created because visual recognition
      does not materially improve these configuration decisions.
- [x] `checklist.md` reflects the objective's concepts and coverage.
- [x] Instructor Notes add concise value rather than repeat answers.
- [x] Practice-test-relevant, official-scope concepts were converted to cards;
      the out-of-scope permissions item is explicitly assigned to Objective
      2.2.
- [x] Every HighYield card has a documented draft justification.
- [x] Custom tags and stable IDs follow repository rules.
- [x] `changelog.md` records the objective's authoring changes.

## Review and build

- [x] Every factual claim and card has been independently reviewed against a
      reviewable source.
- [x] Cards were peer reviewed for accuracy, atomicity, wording, and ambiguity.
- [x] Original diagrams are not applicable; no image cards were created.
- [x] `.venv/bin/python scripts/validate.py` passes without unexplained warnings.
- [x] `.venv/bin/python scripts/build.py` passes and removes no expected output.
- [x] Generated TSV changes are ready to commit with their Markdown sources;
      `Basic.tsv` contains 20 data rows and no other TSV type is expected.
- [x] `pytest` and Ruff pass. Website checks are not applicable unless website
      files change.
- [x] Manual Anki smoke testing passed for Objective 1.7 Basic TSV import,
      including header handling, rendered HTML, Card ID update behavior, and
      tags imported as metadata.

## Acceptance record

- Date accepted: 2026-07-13.
- Final card count: 20 Basic cards, including 13 HighYield cards.
- Generated TSV output verified: `Basic.tsv` contains 20 data rows; no Cloze,
  Command, or Image TSV is expected for this objective.
- Manual Anki smoke test passed for the Basic note type; headers were not
  imported as notes, HTML rendered, Card ID supported update behavior,
  re-import created no duplicates, and tags imported as Anki metadata.
- Media verification: Not applicable; Objective 1.7 has no Image cards.
- Acceptance decision: Accepted.

## Peer review record

| Reviewer | Date | Result | Required Changes | Approval Status |
| --- | --- | --- | --- | --- |
| Self-review | 2026-07-13 | Draft authored from official Objective 1.7 and Messer pp. 13-15; private practice gap check completed | Independent content review, generated-output review, and any required manual Anki acceptance remain | Needs independent review |
| Independent content review | 2026-07-13 | Source scope, omissions, card roles, redundancy, difficulty, tags, and generated structure reviewed; citation and printer-sharing blockers found | Correct page-15 citations, remove unsupported B004 share-name requirement, regenerate output | Changes required |
| Blocker-fix verification | 2026-07-13 | All citation, B004 source-boundary, generated-output, and recommended HighYield changes verified; no new issues or duplicate targets | None | Approved |
| Manual Anki smoke test | 2026-07-13 | Basic TSV import, rendering, metadata tags, 20-note count, and Card ID re-import/update behavior passed | None | Accepted |
