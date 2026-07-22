# Objective 2.10: Securing a SOHO Network

Objective 2.10 asks you to apply security settings to small-office/home-office
(SOHO) wired and wireless networks. The exam task is to match a setting to a
specific risk or access requirement, not merely memorize a list of router menu
options. (CompTIA Objective 2.10; Professor Messer, pp. 46–47)

## Protect the Router and Its Management Interface

Default router and access-point credentials are widely known and can provide
administrator control. Replace them during setup with strong credentials. If
the device supports an additional authentication factor, enable it for
management access.

Management access should also be limited by where it originates. Prefer local
management, restrict the permitted source IP addresses when supported, and
disable remote management when it is not required. These controls protect the
administrative interface; they are separate from rules that control ordinary
client traffic. (Professor Messer, p. 46)

## Filter Traffic for the Intended Result

IP filtering applies allow or deny decisions to IP addresses or address
ranges. An allow list admits only approved entries, while a deny list blocks
listed entries. This is appropriate when the requirement is expressed in
terms of network addresses.

Content filtering instead evaluates characteristics of the traffic, such as a
URL or website category. It can restrict inappropriate material, sensitive
content, or known malicious content. Choose the control that matches the
evidence in the scenario: an address-based requirement points to IP filtering,
while a site or content-category requirement points to content filtering.
(Professor Messer, p. 46)

## Maintain and Physically Protect Network Equipment

SOHO routers, firewalls, access points, and switches depend on manufacturer
firmware. Updates may fix defects, add features, and patch security problems,
so the installed firmware should be kept current through the supported update
process.

Physical placement is also a security setting. Network equipment should be in
a secure location that prevents unauthorized physical access. Wireless
placement must still support useful coverage, and the installation should
allow authorized staff to perform maintenance or power-cycle equipment when
needed. (Professor Messer, p. 46)

## Reduce Automatic and Public Exposure

Universal Plug and Play (UPnP) lets internal applications automatically
discover devices and request inbound port openings. That convenience removes
an explicit approval step. Disable UPnP by default and enable it only when a
required application justifies the exposure.

A screened subnet places public-facing resources in a network segment between
the Internet and the internal network. It allows public access to the intended
service while adding separation from internal systems. The term replaces the
older use of *demilitarized zone (DMZ)* in this context. (Professor Messer,
p. 46)

## Configure the Wireless Network Deliberately

The service set identifier (SSID) is the wireless network name. Replace an
obvious default name with one that does not advertise the router brand or make
the network needlessly identifiable. Disabling SSID broadcast removes the name
from ordinary lists of available networks, but wireless analysis can still
discover it. Hidden broadcasting is therefore obscurity, not a substitute for
encryption and authentication.

An open wireless network requires no authentication password. A SOHO network
should instead use supported WPA2- or WPA3-Personal encryption with a
pre-shared key. Enterprise modes authenticate individual users through an
authentication service, but the Personal/PSK model is the common fit when a
SOHO scenario calls for one shared wireless credential.

Guest access should not remain enabled without a reason. If guests or a
separate device group need it, configure the guest network with WPA2 or WPA3
rather than leaving it open. Otherwise, disable it to remove unnecessary
access. (Professor Messer, pp. 46–47)

## Limit Wired Ports and Firewall Mappings

Administratively disable unused physical network ports, especially those in
public or shared spaces. A port that cannot communicate until it is enabled
removes an unnecessary connection point. Environments that require per-user or
per-device authentication can add network access control such as 802.1X.

Port forwarding, also called port mapping, creates a persistent association
from an external IP address and port to an internal IP address and port. It is
used when an internal service must accept connections from outside the
network. Create only the mapping needed for the required service; the external
and internal port numbers do not have to be identical. (Professor Messer,
p. 47)

## Scenario Decision Summary

- Unknown users can administer a new router: change its default password and
  restrict management access.
- One address or address range must be allowed or denied: use IP filtering.
- A website or category must be restricted: use content filtering.
- An application is automatically opening inbound ports: disable UPnP unless
  the application truly requires it.
- A public service needs separation from internal systems: use a screened
  subnet.
- A wireless name should not appear in normal discovery lists: disable SSID
  broadcast, while recognizing that this does not provide strong security.
- Wireless clients need shared-key protection: use WPA2- or WPA3-Personal.
- An internal service must be reachable from outside: configure a deliberate
  port-forwarding rule.

## References

- CompTIA A+ 220-1202 Exam Objectives v4.0, Objective 2.10
- Professor Messer 220-1202 v1.40 pp. 46–47
