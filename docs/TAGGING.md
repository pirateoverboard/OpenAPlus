# Tagging policy

Authors place only custom content tags in front matter:

```yaml
tags:
  - Scenario
  - Memory
```

Custom tags must be non-empty and cannot contain whitespace, tabs, or commas.
The `A+::` namespace, `Basic`, `Cloze`, `Image`, `Command`, `HighYield`, and
generated source-validation tags such as `Source::Messer-v170` are reserved.
Adding a derived tag manually fails validation with `OA013_MANUAL_DERIVED_TAG`.

The generator emits tags in this order:

1. `A+::<exam>::<objective>`
2. Domain tags when a domain mapping exists, such as
   `A+::220-1201::Domain1-MobileDevices`
3. `A+::<exam>::<normalized-objective-name>`
4. `Basic`, `Cloze`, `Image`, or `Command`
5. `HighYield` when `high_yield: true`
6. Custom topic tags in source order
7. Source-validation tags when a validation layer exists, such as
   `Source::Messer-v170`

Objective names are normalized by removing spaces and non-alphanumeric
characters. For example, `Mobile Device Networks` becomes
`MobileDeviceNetworks`. Duplicate tags are removed without changing the order
of their first occurrence.

## Domain/source-validation tags

Some objectives use path-derived domain tags and Messer validation tags. The
generator adds the tags below during TSV export; authors do not write them in
card front matter. A tag such as `Source::Messer-v170` means the objective was
validated against the Professor Messer PDF v1.70. It does not mean Professor
Messer defines objective scope; the official CompTIA objective PDF remains the
scope authority.

| Folder | Generated domain tag | Generated source-validation tag |
| --- | --- | --- |
| `1.1-operating-system-types-and-purposes` | `A+::220-1202::Domain1-OperatingSystems` | `Source::Messer-v140` |
| `1.2-os-installations-and-upgrades` | `A+::220-1202::Domain1-OperatingSystems` | `Source::Messer-v140` |
| `1.3-microsoft-windows-editions` | `A+::220-1202::Domain1-OperatingSystems` | `Source::Messer-v140` |
| `1.4-microsoft-windows-features-and-tools` | `A+::220-1202::Domain1-OperatingSystems` | `Source::Messer-v140` |
| `1.5-microsoft-command-line-tools` | `A+::220-1202::Domain1-OperatingSystems` | `Source::Messer-v140` |
| `1.6-microsoft-windows-settings` | `A+::220-1202::Domain1-OperatingSystems` | `Source::Messer-v140` |
| `1.7-microsoft-windows-networking-features` | `A+::220-1202::Domain1-OperatingSystems` | `Source::Messer-v140` |
| `1.8-macos-features-and-tools` | `A+::220-1202::Domain1-OperatingSystems` | `Source::Messer-v140` |
| `1.3-mobile-device-networks` | `A+::220-1201::Domain1-MobileDevices` | `Source::Messer-v170` |
| `1.3-mobile-device-management` | `A+::220-1201::Domain1-MobileDevices` | `Source::Messer-v170` |
| `1.3-mobile-device-security` | `A+::220-1201::Domain1-Security` | `Source::Messer-v170` |
| `2.1-ip-addressing-and-common-ports` | `A+::220-1201::Domain2-Networking` | `Source::Messer-v170` |
| `3.1-display-types-and-attributes` | `A+::220-1201::Domain3-Hardware` | `Source::Messer-v170` |
| `3.2-cable-types-connectors-features-and-purposes` | `A+::220-1201::Domain3-Hardware` | `Source::Messer-v170` |
| `3.3-ram-characteristics` | `A+::220-1201::Domain3-Hardware` | `Source::Messer-v170` |
| `3.4-storage-devices` | `A+::220-1201::Domain3-Hardware` | `Source::Messer-v170` |
| `3.5-motherboards-cpus-and-add-on-cards` | `A+::220-1201::Domain3-Hardware` | `Source::Messer-v170` |
| `3.6-power-supplies` | `A+::220-1201::Domain3-Hardware` | `Source::Messer-v170` |
| `3.7-multifunction-devices-and-printers` | `A+::220-1201::Domain3-Hardware` | `Source::Messer-v170` |
| `3.8-printer-maintenance` | `A+::220-1201::Domain3-Hardware` | `Source::Messer-v170` |
| `4.1-virtualization-concepts` | `A+::220-1201::Domain4-VirtualizationCloud` | `Source::Messer-v170` |
| `4.2-cloud-computing-concepts` | `A+::220-1201::Domain4-VirtualizationCloud` | `Source::Messer-v170` |
| `5.1-troubleshooting-hardware` | `A+::220-1201::Domain5-Troubleshooting` | `Source::Messer-v170` |
| `5.2-troubleshooting-storage-devices` | `A+::220-1201::Domain5-Troubleshooting` | `Source::Messer-v170` |
| `5.3-troubleshooting-display-issues` | `A+::220-1201::Domain5-Troubleshooting` | `Source::Messer-v170` |
| `5.4-troubleshooting-mobile-devices` | `A+::220-1201::Domain5-Troubleshooting` | `Source::Messer-v170` |
| `5.5-troubleshooting-networks` | `A+::220-1201::Domain5-Troubleshooting` | `Source::Messer-v170` |
| `5.6-troubleshooting-printers` | `A+::220-1201::Domain5-Troubleshooting` | `Source::Messer-v170` |

Author-provided tags in these folders are Layer 3 topic tags, such as
`Bluetooth`, `WiFi`, `MDM`, `BYOD`, or `Synchronization`.

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
