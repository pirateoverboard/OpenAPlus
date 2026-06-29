# Objective 2.5 study guide: Networking Hardware Devices

Objective 2.5 compares common devices that connect clients, move traffic,
enforce network boundaries, distribute Ethernet power, and terminate provider
connections. The goal is to select hardware by function rather than memorize a
particular vendor's appearance or administration interface.

## Scope and source handling

CompTIA 220-1201 Objective 2.5 defines the scope. Professor Messer 220-1201
v1.70 pages 15–16 were used privately to validate concept presence and page
references. This guide uses original wording and organization and does not
reproduce source tables, diagrams, layouts, or product examples.

## Moving traffic

A **router** moves packets between IP networks or subnets. Its forwarding
decision is based on the destination IP address. A router may connect networks
that use different media or operate across LAN and WAN boundaries.

A **switch** connects devices within a local network and forwards Ethernet
frames according to MAC addresses. Switches offer multiple ports and may also
supply Power over Ethernet.

An **unmanaged switch** is intended for simple, fixed, plug-and-play operation.
A **managed switch** adds administrative functions such as VLAN support,
traffic prioritization, redundancy features, port mirroring, and remote
management. Select a managed switch when the network requires control or
visibility rather than basic connectivity alone.

An **access point** bridges wireless clients onto a wired network. An access
point is not inherently a router, although a consumer wireless router commonly
combines routing, switching, firewall, and access-point functions in one unit.

## Organizing and protecting connections

A **patch panel** terminates permanent cable runs and provides ports that can be
patched to switch interfaces. It supports organized cabling and easier changes;
it does not forward or filter traffic.

A **firewall** applies rules to network traffic. It commonly controls traffic
at a network boundary and may filter by transport-layer information or by
application when that capability is available.

## Power over Ethernet

**Power over Ethernet (PoE)** carries electrical power and network data over an
Ethernet connection. It is useful for devices such as access points, IP phones,
and cameras where a separate nearby power outlet would be inconvenient.

A **PoE switch** supplies power directly from compatible switch ports. A **PoE
injector** adds power inline when the existing switch does not provide PoE. The
powered device and power source must support compatible PoE standards.

PoE, PoE+, and PoE++ represent increasing power capabilities. A source that
supports only PoE+ cannot satisfy a device that requires PoE++. Exact power
figures are not carded here because standards compatibility is the more useful
technician decision for this objective.

The approved source provides these reference values for comparing the
standards:

- **PoE:** 15.4 W
- **PoE+:** 25.5 W
- **PoE++ Type 3:** 51 W
- **PoE++ Type 4:** 71.3 W

These figures remain study-guide reference material rather than separate card
targets.

## Provider connection devices

A **cable modem** connects a customer network to broadband service delivered
over a cable-provider network. DOCSIS is the associated cable-data standard,
but versions and speed tiers are intentionally outside this objective's active
recall set.

A **DSL modem** uses a telephone-line connection for digital subscriber line
service. Distance and speed characteristics belong with internet connection
types in Objective 2.7 rather than hardware selection here.

An **optical network terminal (ONT)** terminates the provider's optical
connection and presents the customer-side network handoff. It is the relevant
device when fiber reaches the premises.

## NICs and physical MAC addresses

A **network interface card (NIC)** provides a device's interface to a network.
It may be built into the system or installed separately, and it must support the
network type being used.

The NIC contains a physical **media access control (MAC) address** used for
local data-link forwarding. This hardware address is distinct from an IP
address, which identifies a device at the network layer.

## Intentionally limited details

The following details are not active-recall targets in this draft:

- exact PoE wattage, current, and delivery-loss figures;
- DOCSIS versions, provider speed tiers, and channel details;
- DSL distance limits, speed ratios, and provider-specific provisioning;
- vendor interfaces, default credentials, model-specific ports, and pricing;
- switch ASIC design, multilayer-switch implementation, and detailed STP/SNMP
  configuration;
- firewall rule syntax, VPN configuration, and proxy features;
- physical product appearance, because form factors vary and would make an
  Image card unreliable;
- detailed internet-connection comparisons reserved for Objective 2.7; and
- networking tools reserved for Objective 2.8.

## References

- Professor Messer 220-1201 v1.70 p.15
- Professor Messer 220-1201 v1.70 p.16
- CompTIA 220-1201 Exam Objectives v2.0, Objective 2.5
