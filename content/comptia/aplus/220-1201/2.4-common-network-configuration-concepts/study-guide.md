# Objective 2.4 study guide: Common Network Configuration Concepts

Objective 2.4 explains common DNS, DHCP, VLAN, and VPN configuration concepts.
The emphasis is on choosing the right record or setting, recognizing what a
misconfiguration affects, and separating stable concepts from product-specific
administration.

## Scope and source handling

CompTIA 220-1201 Objective 2.4 defines the scope. Professor Messer 220-1201
v1.70 pages 11–15 were used privately to confirm concept presence and source
page references. This guide uses original organization and wording and does not
reproduce source tables, diagrams, command output, or page layout.

## DNS record selection

DNS stores different record types for different jobs:

- An **A** record associates a host name with an IPv4 address.
- An **AAAA** record associates a host name with an IPv6 address.
- A **CNAME** record makes one name an alias of another host name. The alias
  follows the canonical name instead of storing a separate address.
- An **MX** record identifies the host name of a domain's mail exchanger. It
  points to a host name rather than directly to an IP address.
- A **TXT** record publishes text in DNS. TXT records support domain
  verification and email-security information, among other uses.

The record type must match the intended result. Editing an A record does not
publish an IPv6 destination, and an MX record does not replace the address
record needed to resolve the named mail host.

## DNS-based email protection

Three related mechanisms use DNS-published information to help receiving mail
systems evaluate messages:

- **SPF** identifies the mail systems authorized to send for a domain.
- **DKIM** lets a sending domain digitally sign outgoing mail. A receiving
  system obtains the public key from a DKIM TXT record to validate the
  signature.
- **DMARC** publishes a policy for mail that does not pass SPF or DKIM checks
  and can request reports about those results.

These mechanisms have different roles. SPF concerns an authorized sender,
DKIM concerns a verifiable signature, and DMARC supplies policy and reporting
around the authentication results.

## DHCP configuration

DHCP supplies clients with IP configuration automatically. A **lease** makes an
assignment available for a configured period and allows the client to renew it.

A DHCP **scope** defines the address pool and related settings available to a
subnet. If the scope has no usable addresses left, new clients cannot receive a
normal dynamic assignment from that scope.

A **reservation** associates a device's MAC address with a chosen IP address so
the DHCP server consistently offers that address to the device. An
**exclusion** removes an address or range from dynamic assignment. Reservations
are useful for centrally managed, predictable assignments; exclusions protect
addresses that DHCP must not distribute from its pool.

Exact lease durations, pool sizes, and option values depend on the network.
OpenAPlus focuses on the purpose and symptoms of each setting rather than
inventing universal values.

## VLANs

A VLAN creates a logical broadcast domain. Devices can use the same physical
switching infrastructure while being placed in separate logical networks.
This supports segmentation without requiring a separate physical switch for
every group.

Objective 2.4 requires the VLAN concept, not vendor-specific switch commands,
menu paths, or a full trunking configuration exercise.

## VPNs

A VPN protects private traffic as it crosses a public network. A
**client-to-site VPN** connects an individual remote device to an organization's
network. A **site-to-site VPN** connects networks, such as two office locations,
through VPN endpoints.

Products differ in setup workflow and cryptographic options. The stable
learning target is choosing the connection model that fits the access need.

## Intentionally limited details

The following details are not active-recall targets in this draft:

- DORA step ordering, because Objective 2.4 names leases rather than requiring
  a DHCP message-sequence drill;
- exact DHCP lease durations, pool sizes, and option values, because they are
  environment-specific;
- DNS command output and record-file syntax, because the objective focuses on
  record purpose;
- MX priority-number rules, because basic MX selection is sufficient here;
- VLAN IDs, tagging syntax, trunk configuration, and switch-vendor commands;
- VPN brands, exact user-interface paths, and cryptographic suites.

## References

- Professor Messer 220-1201 v1.70 p.11
- Professor Messer 220-1201 v1.70 p.12
- Professor Messer 220-1201 v1.70 p.13
- Professor Messer 220-1201 v1.70 p.14
- Professor Messer 220-1201 v1.70 p.15
- CompTIA 220-1201 Exam Objectives v2.0, Objective 2.4
