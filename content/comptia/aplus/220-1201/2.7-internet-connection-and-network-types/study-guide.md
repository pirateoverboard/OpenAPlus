# Objective 2.7 study guide: Internet Connection and Network Types

Objective 2.7 compares common ways to reach the internet and common network
scopes. The useful technician skill is recognizing the medium, coverage area,
and operational tradeoff that distinguishes each option—not memorizing a
provider's current plan or advertised speed.

## Scope and source handling

CompTIA 220-1201 Objective 2.7 defines the scope. Professor Messer 220-1201
v1.70 pages 18–19 were used privately to confirm concept presence and concise
page references. This guide uses original wording and organization; it does not
reproduce source tables, diagrams, layouts, or examples.

## Internet connection types

### Satellite

**Satellite internet** uses a non-terrestrial radio link. It can serve remote
locations where terrestrial infrastructure is unavailable, but the long signal
path can add noticeable latency. The installation also needs a usable view of
the satellite, and weather can affect some links. Satellite is therefore a
coverage solution with tradeoffs, not automatically the fastest choice.

### Fiber

**Fiber internet** carries data as light through optical cabling. It supports
high data rates and long-distance communication, but optical equipment,
installation, and repair can cost more than copper alternatives. An optical
network terminal at the premises was covered as provider hardware in Objective
2.5; this objective focuses on fiber as the connection medium.

### Cable

**Cable internet** delivers broadband data over a cable-provider network.
DOCSIS is the standard family used to carry data on that infrastructure. A
cable connection may coexist with other services on the provider network.
Current speed tiers and DOCSIS versions vary and are not active-recall targets
here.

### DSL

**Digital subscriber line (DSL)** carries broadband service over telephone
lines. Common residential DSL service is asymmetric: downstream capacity is
greater than upstream capacity. Performance depends in part on the line and
distance to provider equipment, so exact limits should not be generalized
across every deployment.

### Cellular

**Cellular internet** uses a mobile provider's radio network. A phone can share
its data connection through tethering or a hotspot, and a dedicated hotspot can
provide the same general function without tying up the phone.

### WISP

A **wireless internet service provider (WISP)** supplies terrestrial internet
access over a wireless link. It is useful in rural or remote locations where a
wired provider connection is impractical. Customer premises commonly use an
outdoor antenna as part of the WISP connection.

## Network types

### LAN and WLAN

A **local area network (LAN)** connects systems across a limited local area,
such as a building or nearby group of buildings. Ethernet is a common wired LAN
technology.

A **wireless local area network (WLAN)** is a LAN implemented with wireless
technology such as 802.11. It provides mobility within a limited area, and
additional access points can extend coverage. WLAN describes the local network;
it does not describe the upstream internet service.

### WAN and MAN

A **wide area network (WAN)** connects networks across substantial geographic
distance. An organization may use a WAN to connect separate LANs in different
cities or regions.

A **metropolitan area network (MAN)** spans a city or metropolitan region. It
is generally larger than a building-scale LAN and smaller in geographic scope
than a broad WAN.

### PAN

A **personal area network (PAN)** connects devices around one person over a
short range. Bluetooth peripherals, nearby personal devices, and similar
connections fit this scope. PAN identifies the network's personal scale rather
than a specific internet-access method.

### SAN

A **storage area network (SAN)** provides dedicated network access to shared
block storage. To connected servers, the storage behaves more like directly
attached block storage than a normal shared-file service. SANs commonly need
high bandwidth and may use an isolated network.

## Comparison cues

- Choose **satellite** when remote coverage matters and added latency is an
  acceptable tradeoff.
- Choose **fiber** when optical service and high-capacity connectivity are
  available and installation cost is acceptable.
- Recognize **cable** by the cable-provider infrastructure and DOCSIS.
- Recognize **DSL** by telephone-line service and distance-sensitive,
  commonly asymmetric operation.
- Choose **cellular** for provider-based mobile connectivity or tethering.
- Recognize a **WISP** by terrestrial wireless service to premises, often with
  an outdoor antenna.
- Classify networks by scope: personal (**PAN**), local (**LAN/WLAN**),
  metropolitan (**MAN**), wide-area (**WAN**), or storage-focused (**SAN**).

## Intentionally limited details

The following details are not active-recall targets in this draft:

- exact provider speeds, prices, data caps, and availability;
- exact satellite latency figures, orbital details, and branded constellations;
- specific DSL distance limits, variants, and central-office calculations;
- DOCSIS versions, channels, modulation, and current cable speed tiers;
- cellular generations, frequency bands, carrier features, and plan behavior;
- WISP proprietary radio systems, antenna alignment values, and deployment
  ranges;
- vendor-specific WAN, MAN, SAN, and WLAN architectures; and
- network troubleshooting tools, which belong to Objective 2.8.

## References

- Professor Messer 220-1201 v1.70 p.18
- Professor Messer 220-1201 v1.70 p.19
- CompTIA 220-1201 Exam Objectives v2.0, Objective 2.7
