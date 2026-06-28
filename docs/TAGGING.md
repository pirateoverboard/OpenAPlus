# Tagging policy

Authors place only custom content tags in front matter:

```yaml
tags:
  - Scenario
  - Memory
```

Custom tags must be non-empty and cannot contain whitespace, tabs, or commas.
The `A+::` namespace and `Basic`, `Cloze`, `Image`, and `HighYield` are reserved.
Adding a derived tag manually fails validation with
`OA013_MANUAL_DERIVED_TAG`.

The generator emits tags in this order:

1. `A+::<exam>::<objective>`
2. `A+::<exam>::<normalized-objective-name>`
3. `Basic`, `Cloze`, or `Image`
4. `HighYield` when `high_yield: true`
5. Custom tags in source order

Objective names are normalized by removing spaces and non-alphanumeric
characters. For example, `Mobile Device Networks` becomes
`MobileDeviceNetworks`. Duplicate tags are removed without changing the order
of their first occurrence.

## HighYield rubric

Set `high_yield: true` when a card covers one or more of these:

- a frequently tested CompTIA concept;
- a required troubleshooting decision;
- a common exam trap;
- a common real help desk issue;
- a foundational concept used by later objectives; or
- a fact that must be recalled quickly, such as common ports, APIPA, DHCP/DNS,
  RAID, Wi-Fi standards, printer processes, BIOS/UEFI, TPM, or cable and
  connector identification.

Do not mark a card HighYield merely because it contains an interesting but
low-value fact, rare trivia, an overly specific out-of-scope detail, an easily
inferred fact, or content added only for completeness. HighYield must not be
applied to every card in an objective.

Production HighYield classification requires reviewer agreement. When reviewer
agreement is unavailable or disputed, record the justification and approval
status in the objective checklist or changelog.
