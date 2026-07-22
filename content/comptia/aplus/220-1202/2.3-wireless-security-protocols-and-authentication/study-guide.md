# Objective 2.3: Wireless Security Protocols and Authentication

Objective 2.3 asks you to compare wireless protection and authentication
methods. Keep two questions separate: how wireless traffic is protected, and
how a user or device proves its identity. WPA2, WPA3, TKIP, and AES concern
wireless protection; RADIUS, TACACS+, Kerberos, and multifactor authentication
address authentication in different ways. (CompTIA Objective 2.3; Professor
Messer, pp. 30–32)

## Encryption and Authentication

Wireless signals can be received by anyone within radio range, so protected
networks encrypt traffic for confidentiality and check integrity to detect
changes. Encryption does not by itself establish which individual is allowed
to use a resource. Authentication supplies that identity decision, while an
encryption protocol protects the wireless communication. (Professor Messer,
p. 30)

## WPA2, WPA3, TKIP, and AES

**Temporal Key Integrity Protocol (TKIP)** was designed as a transitional
improvement for the original WPA and could operate on existing hardware. It is
the older choice in this comparison.

**Advanced Encryption Standard (AES)** provides stronger encryption than TKIP.
WPA2 replaced the original WPA and uses AES, although its higher processing
requirements sometimes required access-point hardware upgrades.

**WPA3** upgrades WPA2 with stronger cryptographic options and better
protection during the initial key exchange. It can also provide encryption on
an open wireless network even when users do not enter a shared authentication
password. (Professor Messer, p. 31)

## Personal and Enterprise Modes

WPA Personal, also called **pre-shared key (PSK)** mode, uses a shared key for
the network. It is simpler, but everyone using that configuration relies on the
same wireless secret.

WPA Enterprise, also called **802.1X** mode, authenticates users individually
through an authentication server such as RADIUS. Enterprise mode separates
user authentication from the shared-key model and fits organizations that need
central identity management. (Professor Messer, p. 31)

## RADIUS

**Remote Authentication Dial-in User Service (RADIUS)** is a widely supported
authentication, authorization, and accounting (AAA) protocol. It centralizes
user authentication for many kinds of access devices and services, including
wireless 802.1X, routers, switches, firewalls, servers, remote-access VPNs, and
other services that can communicate with a RADIUS server.

RADIUS is therefore an authentication integration method, not a wireless
encryption algorithm. The wireless connection still needs an appropriate WPA
security mode and encryption. (Professor Messer, p. 31)

## TACACS+

**Terminal Access Controller Access-Control System Plus (TACACS+)** is a remote
authentication protocol and the current form of TACACS. It supports more
authentication request and response codes than the earlier protocol and is
commonly associated with Cisco network devices.

Choose TACACS+ when it matches the network-device environment and available
authentication service. Like RADIUS, it authenticates access rather than
encrypting Wi-Fi radio traffic. (Professor Messer, pp. 31–32)

## Kerberos

**Kerberos** is a network authentication protocol that uses cryptographic
tickets. A user authenticates once and can then use trusted services without
repeatedly entering a username and password. Kerberos provides mutual
authentication between client and server and helps defend against replay and
on-path attacks.

Kerberos is strongly associated with Microsoft domain environments, although
it is an open standard and can work on other platforms. Its ticket-based SSO
role differs from RADIUS or TACACS+ requests sent by access devices to a
central authentication server. (Professor Messer, p. 31)

## Multifactor Authentication

**Multifactor authentication (MFA)** requires evidence from more than one
factor category. Examples include something known, possessed, inherent to the
user, associated with location, or based on behavior. Two passwords remain one
factor category and therefore do not create MFA.

MFA can use dedicated hardware or specialized biometric equipment, but it can
also use lower-cost options such as authenticator applications. MFA adds a
verification layer; it does not replace WPA encryption or turn RADIUS,
TACACS+, or Kerberos into encryption protocols. (Professor Messer, p. 32)

## References

- CompTIA A+ 220-1202 Exam Objectives v4.0, Objective 2.3
- Professor Messer 220-1202 v1.40 pp. 30–32
