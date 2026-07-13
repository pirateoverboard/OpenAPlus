# Objective 1.7: Microsoft Windows Networking Features

Objective 1.7 asks you to configure Windows client networking from a scenario.
The useful skill is recognizing the environment or connectivity requirement,
then choosing the matching Windows network feature. Exact Settings and Control
Panel paths can vary by Windows release, so focus on stable purposes and
configuration choices. (CompTIA Objective 1.7; Professor Messer, pp. 13-15)

## Domains, Workgroups, and Shared Resources

A workgroup is a peer arrangement suited to a small network. Each computer
maintains its own accounts and settings, so administration is decentralized. A
domain instead centralizes authentication and device access and can support
many systems across multiple networks. Joining a domain requires an eligible
Windows edition and an account with the necessary rights. (Professor Messer,
p. 13)

Windows can share folders and printers with other network users. A shared
printer is enabled through its printer properties, while a shared folder or
file server can be reached from File Explorer. A network path identifies both
the server and the share, such as `\\server\share`. A mapped drive assigns a
local drive letter to that path and can be configured to reconnect
automatically. (Professor Messer, pp. 13 and 15)

A share name ending in `$` is hidden from ordinary browsing, but the suffix is
not an access-control feature. Users who know the path still need appropriate
authorization, and hiding the name does not replace permissions. (Professor
Messer, p. 13)

## Local Windows Firewall

Windows Defender Firewall can use different settings for public and private
network profiles. Keep the firewall enabled during normal operation. If a
legitimate application needs inbound access, allow the application or create a
narrow rule instead of leaving the entire firewall disabled. (Professor
Messer, p. 14)

An application exception is a focused way to permit an approved application.
Predefined exceptions cover common services, while a custom rule provides more
control when a specific port or other condition must be allowed or blocked.
The option to block all incoming connections overrides the normal exception
list and is intended for a more restrictive situation. Firewall notifications
can also report when an application is blocked. (Professor Messer, p. 14)

## Client IP Configuration

Dynamic configuration normally uses DHCP to obtain the client's IP parameters
automatically. Static configuration requires the technician to enter the
needed values manually. Windows can also use an alternate static configuration
when DHCP is unavailable; otherwise its fallback is APIPA. (Professor Messer,
p. 14)

The main IPv4 client values have different jobs:

- The IP address identifies the client interface on the network.
- The subnet mask determines which addresses the client treats as local.
- The default gateway is the route used to reach destinations outside the
  local subnet.
- DNS settings identify the resolver used to translate names into IP
  addresses.

If a client has neither a valid static address nor a reachable DHCP service,
Windows can assign itself an APIPA address in the `169.254.x.x` link-local
space. That can permit communication with nearby link-local hosts, but it does
not provide normal routed internet connectivity. (Professor Messer, p. 14)

## Establishing Connections

Windows can establish wired Ethernet, Wi-Fi, VPN, and WWAN/cellular
connections. Wired networking uses a direct Ethernet connection. Wi-Fi setup
selects a network name and supplies the required security information. A VPN
uses the built-in client to connect to a workplace and may require credentials
or a smart card. (CompTIA Objective 1.7; Professor Messer, p. 14)

WWAN provides cellular connectivity through compatible mobile-network
hardware. Provider software and setup details vary, so the stable exam choice
is recognizing WWAN/cellular as the connection type when Ethernet and Wi-Fi
are not the intended access methods. Tethering or a hotspot can provide another
way to use mobile service. (Professor Messer, p. 14)

## Proxy, Network Profiles, and Metered Connections

A proxy is an intermediary that changes the path of supported application
traffic. Windows proxy configuration can specify the proxy address and
exceptions for destinations that should bypass it. Not every application or
protocol necessarily follows the same proxy setting. (Professor Messer,
p. 15)

Choose the public profile for an untrusted network such as public Wi-Fi; it
restricts local sharing and discovery. Choose private for a trusted home or
work network where connecting to local devices and shares is intended. The
profile also lets Windows apply the corresponding firewall behavior.
(Professor Messer, pp. 14-15)

A metered connection tells Windows that data use should be limited because the
link is slow, capped, or billed by usage. Windows and applications can reduce
some background communication, including update or synchronization activity.
Metering is a traffic-management choice, not a substitute for fixing an IP,
DNS, or gateway problem. (Professor Messer, p. 15)

## Decision Summary

- Use a workgroup for small peer administration; use a domain for centralized
  authentication and device access.
- Use a network path for direct share access or map it to a drive letter for
  familiar, repeat access.
- Prefer a narrow firewall exception or rule over disabling the firewall.
- Use DHCP for automatic addressing and static configuration when fixed manual
  values are required.
- Associate the subnet mask with local-network boundaries, the gateway with
  off-subnet traffic, and DNS with name resolution.
- Match VPN, Wi-Fi, wired Ethernet, or WWAN to the connection requirement.
- Use public for untrusted networks, private for trusted sharing, and metered
  for limited or usage-billed links.

## References

- CompTIA A+ 220-1202 Exam Objectives v4.0, Objective 1.7
- Professor Messer 220-1202 v1.40 pp. 13-15
