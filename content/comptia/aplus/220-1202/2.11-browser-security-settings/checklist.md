# Objective 2.11 completion checklist

**Objective status: ACCEPTED.** Core 2 Objective 2.11 has passed independent
content review, blocker-fix verification, generated-output verification, and
manual Anki smoke testing.

Official context:

```text
Domain 2.0 Security, Objective 2.11: Given a scenario, configure relevant
security settings in a browser.
```

Official bullet scope reviewed:

1. Browser download/installation: trusted sources and hashing; untrusted
   sources.
2. Browser patching.
3. Extensions and plug-ins from trusted and untrusted sources.
4. Password managers.
5. Secure connections/sites and valid certificates.
6. Settings: pop-up blocker, clearing browsing data, clearing cache,
   private-browsing mode, sign-in/browser data synchronization, ad blockers,
   proxy, and secure DNS.
7. Browser feature management: enable or disable plug-ins, extensions, and
   features.

Source-scope decisions:

- The official objective supplies the browser setting list and the applied
  `Given a scenario` learner task. Professor Messer pp. 47–48 validates the
  setting purposes, distinctions, and page references.
- The private Core 2 practice-exam gap check reinforced secure DNS for
  protecting lookup privacy, the local clock as a certificate-validation
  dependency, cache clearing for stale or incomplete page content, and checking
  whether a required approved extension is enabled. No question, scenario,
  answer choice, explanation, or citation was copied or reconstructed.
- Malware diagnosis and removal for persistent pop-ups or redirection remains
  under Objectives 2.4, 2.6, and 3.4. This objective focuses on configuring the
  browser setting when the scenario supports that action.
- No new secondary source was used, and no unresolved source ambiguity blocks
  the supported card set.

## Coverage map

| Concept | Source | Study Guide Section | Card IDs | Card Types | No-Card Reason | Reviewed |
| --- | --- | --- | --- | --- | --- | --- |
| Trusted browser download source and untrusted-source avoidance | CompTIA 2.11; Messer p. 47 | Install the Browser from a Trusted Source | 2.11-B001 | Basic | N/A | Self-reviewed |
| Download hash verification | CompTIA 2.11; Messer p. 47 | Install the Browser from a Trusted Source | 2.11-B002 | Basic | N/A | Self-reviewed |
| Browser patching | CompTIA 2.11; Messer p. 47 | Patch the Browser | 2.11-B003 | Basic | N/A | Self-reviewed |
| Trusted extension and plug-in sources | CompTIA 2.11; Messer p. 47 | Control Extensions, Plug-ins, and Features | 2.11-B004 | Basic | N/A | Self-reviewed |
| Untrusted or unexpected extensions and plug-ins | CompTIA 2.11; Messer pp. 47–48 | Control Extensions, Plug-ins, and Features | 2.11-B005 | Basic | N/A | Self-reviewed |
| Password managers and unique credentials | CompTIA 2.11; Messer p. 48 | Use a Password Manager | 2.11-B006 | Basic | N/A | Self-reviewed |
| Valid certificate checks | CompTIA 2.11; Messer p. 48 | Validate Secure Sites | 2.11-B007 | Basic | N/A | Self-reviewed |
| Local date/time and certificate validation | CompTIA 2.11; Messer p. 48 | Validate Secure Sites | 2.11-B008 | Basic | N/A | Self-reviewed |
| Pop-up blocker and narrow exceptions | CompTIA 2.11; Messer p. 48 | Manage Pop-ups, Ads, and Site Exceptions | 2.11-B009 | Basic | N/A | Self-reviewed |
| Clearing browsing data | CompTIA 2.11; Messer p. 48 | Clear the Right Local Data | 2.11-B010 | Basic | N/A | Self-reviewed |
| Clearing browser cache | CompTIA 2.11; Messer p. 48 | Clear the Right Local Data | 2.11-B011 | Basic | N/A | Self-reviewed |
| Private-browsing mode | CompTIA 2.11; Messer p. 48 | Use Private Browsing and Synchronization Deliberately | 2.11-B012 | Basic | N/A | Self-reviewed |
| Sign-in/browser data synchronization | CompTIA 2.11; Messer p. 48 | Use Private Browsing and Synchronization Deliberately | 2.11-B013 | Basic | N/A | Self-reviewed |
| Ad blockers | CompTIA 2.11; Messer p. 48 | Manage Pop-ups, Ads, and Site Exceptions | 2.11-B014 | Basic | N/A | Self-reviewed |
| Explicit and transparent proxy configuration | CompTIA 2.11; Messer p. 48 | Configure Proxies and Secure DNS | 2.11-B015 | Basic | N/A | Self-reviewed |
| Secure DNS and DNS over HTTPS | CompTIA 2.11; Messer p. 48 | Configure Proxies and Secure DNS | 2.11-B016 | Basic | N/A | Self-reviewed |
| Enable/disable browser features and approved add-ons | CompTIA 2.11; Messer p. 48 | Control Extensions, Plug-ins, and Features | 2.11-B017 | Basic | N/A | Self-reviewed |
| Password-vault synchronization | Messer p. 48 | Use a Password Manager | None | None | Study-guide context; synchronization behavior varies and the active-recall target is choosing a password manager for unique encrypted credentials | Self-reviewed |
| Vendor-specific browser menus, extension stores, and update paths | Messer pp. 47–48 | None | None | None | Volatile implementation detail is not required by the official objective | Self-reviewed |
| Detailed proxy deployment and authentication design | Messer p. 48 | Configure Proxies and Secure DNS | None | None | Study-guide boundary only; the objective requires relevant browser configuration, not enterprise proxy architecture | Self-reviewed |

## Objective-specific cautions

- Do not treat a matching hash as proof that an untrusted publisher is safe.
- Do not treat private browsing as a substitute for trusted downloads,
  patching, or secure connections.
- Do not disable pop-up blocking globally when one trusted site needs an
  exception.
- Do not confuse clearing cached site resources with clearing all browsing
  history and stored credentials.
- Do not expand browser configuration scenarios into malware-removal content
  owned by neighboring objectives.
- Do not prescribe vendor-specific menu paths or extension-store names as the
  durable answer.

## HighYield review

| Card IDs | Rubric justification | Review status |
| --- | --- | --- |
| 2.11-B001–B008, 2.11-B011, 2.11-B016 | Central software-trust, patching, credential, certificate, cache, and DNS-privacy decisions with practical entry-level support value | Independent review approved |

## Research and extraction

- [x] The matching 220-1202 exam version and Objective 2.11 scope are confirmed.
- [x] The official CompTIA objective PDF was used as the primary scope authority.
- [x] Professor Messer v1.40 printed pages 47–48 were used only for approved
      secondary validation and page references.
- [x] The Professor Messer Core 2 practice exam was used only as a private
      secondary gap check after official scope was established.
- [x] Practice-gap concepts useful for active recall are carded.
- [x] No new secondary source was used.
- [x] Concepts were extracted and expressed without copying source language.
- [x] No unresolved source ambiguity was identified.

## Authoring

- [x] `study-guide.md` is written, sourced, and internally consistent.
- [x] Basic cards emphasize short configuration and consequence scenarios in
      line with the official `Given a scenario` wording.
- [x] Cloze cards were considered; compact expansions such as DoH would
      duplicate applied Basic-card learning targets.
- [x] Command cards were considered and are not applicable.
- [x] Image cards were considered; browser screen recognition would be
      vendor-specific and does not improve these configuration decisions.
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
- [x] Generated TSV changes match the Markdown sources: `Basic.tsv` contains 17
      data rows; no Cloze, Command, Image, or media output is expected.
- [x] The 103-test pytest suite and Ruff lint and format checks pass.
- [x] Manual Anki smoke testing passes for the generated Basic file.

## Acceptance record

- Date accepted: 2026-07-22.
- Final card count: 17 Basic cards, including 10 HighYield cards.
- Generated TSV output: `Basic.tsv` contains 17 verified data rows; no Cloze,
  Command, Image, or media output is expected.
- Manual Anki smoke test: User-reported pass on 2026-07-22 for the Basic
  import; headers were not imported as notes, HTML rendered correctly,
  Instructor Notes displayed after reveal, tags imported as Anki metadata,
  Card ID supported update behavior, re-import created no duplicates, and the
  observed count matched 17 Basic notes. The Anki version and disposable
  profile name were not provided.
- Media verification: Not applicable; Objective 2.11 has no Image cards.
- Acceptance decision: Accepted.

## Peer review record

| Reviewer | Date | Result | Required Changes | Approval Status |
| --- | --- | --- | --- | --- |
| Self-review | 2026-07-22 | Draft authored from official Objective 2.11 and Messer pp. 47–48; private practice gap check completed | Independent content review remains | Needs independent review |
| Independent content review | 2026-07-22 | NO-GO; approved scope, coverage, omissions, redundancy, difficulty, and HighYield classifications, but found two practice-adjacent scenarios and two unsupported wording extensions | Rewrite B008 and B016 from the approved notes; limit B005 to disabling; remove unsupported tracking and site-compatibility claims from B014 | Changes required |
| Author fix pass | 2026-07-22 | Rewrote B008 and B016 with independent configuration scenarios, limited B005 to the sourced disable action, corrected B014 and study-guide ad-blocker claims, and rewrapped B001 | Blocker-fix verification remains | Needs blocker-fix verification |
| Blocker-fix verification | 2026-07-22 | GO; all four blockers resolved with no new source, copyright, scope, redundancy, metadata, or generated-output issues | None | Approved; ready for manual Anki smoke test |
| Manual Anki smoke test | 2026-07-22 | User-reported Basic import, rendering, metadata tags, 17-note total, and Card ID re-import/update behavior passed; Anki version/profile not provided | None | Accepted |
