# Objective 2.6 study guide: Basic SOHO Network Configuration

Objective 2.6 applies core IP-addressing settings in a small office/home office
(SOHO) network. The published sub-objectives cover IPv4 public and private
addresses, IPv6, APIPA, static and dynamic assignment, subnet masks, and default
gateways.

## Scope and source handling

CompTIA 220-1201 Objective 2.6 defines the scope. Professor Messer 220-1201
v1.70 pages 17–18 were used privately to validate concept presence and page
references. This guide uses original wording and organization and does not
reproduce source diagrams, address tables, layouts, or command output.

The objective title mentions wired and wireless SOHO networks, but its explicit
bullet list is limited to IP addressing. Cabling, wireless standards, security
settings, and networking tools remain in their assigned objectives rather than
being inferred into this one.

## IPv4 public and private addresses

An IPv4 address is 32 bits long and is commonly written as four decimal octets.
Every active interface on the same IP network needs a nonconflicting address.

Public IPv4 addresses support communication across the public internet.
Private IPv4 addresses are intended for internal networks and are not routed
directly across the public internet.

A SOHO router often sits between the private local network and the ISP
connection. When private IPv4 clients access public networks, the router
commonly performs network address translation (NAT) so multiple private hosts
can share the public-facing connection. NAT is supporting context here rather
than a separate Objective 2.6 card target.

The three private IPv4 blocks are:

- `10.0.0.0/8`
- `172.16.0.0/12`
- `192.168.0.0/16`

Recognizing these blocks helps a technician distinguish an internal address
from a public one without relying on a vendor interface.

## IPv6

An IPv6 address is 128 bits long and is written in hexadecimal groups separated
by colons. IPv6 provides a much larger address space than IPv4. This objective
requires basic recognition rather than exhaustive IPv6 compression rules,
address types, or subnetting exercises.

## Static and dynamic assignment

A **static** address remains assigned until an administrator changes the
configuration. Manual static configuration requires the technician to enter and
maintain the address settings on the device.

A **dynamic** address is supplied automatically, commonly by DHCP. Dynamic
assignment scales better for ordinary clients because address settings can be
managed centrally. DHCP reservations were covered as a configuration concept
in Objective 2.4 and are not duplicated here.

## Subnet mask and default gateway

The **subnet mask** lets an IPv4 host determine which destination addresses are
on its local subnet. A wrong mask can cause the host to classify local and
remote destinations incorrectly.

The **default gateway** is the local router address a host uses to reach
destinations outside its subnet. The gateway address must be reachable on the
host's local subnet. When local communication works but off-subnet access does
not, the gateway setting is a focused first check.

## APIPA

**Automatic Private IP Addressing (APIPA)** provides an IPv4 link-local address
when a host configured for automatic addressing cannot obtain a DHCP lease.
APIPA uses the `169.254.0.0/16` block; the approved source identifies
`169.254.1.0` through `169.254.254.255` as the functional assignment range.

An APIPA host can communicate with compatible hosts on the local link, but
routers do not forward this traffic. Seeing a `169.254.x.x` address is therefore
a strong cue to investigate DHCP availability or reachability.

## Intentionally limited details

The following details are not active-recall targets in this draft:

- binary-to-decimal conversion and full subnetting mathematics;
- historical classful IPv4 addressing;
- exact IPv4 and IPv6 address-count calculations;
- exhaustive IPv6 compression, address-type, and prefix rules;
- APIPA's address-selection and ARP duplicate-check procedure;
- manual configuration paths for particular operating systems or routers;
- DHCP reservations, scopes, and exclusions already covered in Objective 2.4;
- DNS, NTP, and other optional client settings covered by earlier objectives;
- cabling and connector content assigned to Objective 3.2;
- wireless standards assigned to Objective 2.2; and
- networking tools assigned to Objective 2.8.

## References

- Professor Messer 220-1201 v1.70 p.17
- Professor Messer 220-1201 v1.70 p.18
- CompTIA 220-1201 Exam Objectives v2.0, Objective 2.6
