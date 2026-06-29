# Objective 2.1 study guide: IP Addressing and Common Ports

Objective 2.1 covers how IP carries application traffic, how TCP and UDP differ,
and why common service ports matter for configuration and troubleshooting.

## Scope and source handling

CompTIA 220-1201 Objective 2.1 defines the scope. Professor Messer 220-1201
v1.70 pages 6–7 were used as private validation/reference pages only. This
guide uses original wording and does not reproduce the source diagrams, layout,
or examples.

## IP, TCP, UDP, and applications

IP moves traffic between IP addresses. TCP and UDP ride inside IP and provide
different transport behavior for applications.

TCP is connection-oriented. It establishes communication state, tracks delivery,
handles retransmission and ordering, and uses flow control. This makes TCP a
strong fit when the application needs reliable delivery.

UDP is connectionless. It does not provide TCP-style setup, recovery,
reordering, retransmission, or flow control. UDP is useful when low delay or
simple connectionless exchange matters more than transport-layer recovery.

## Ports and sockets

A port identifies the service or application conversation on a device. A network
connection is not just “to an IP address”; the protocol and port also matter.

Well-known service ports are important for client/server compatibility,
firewall rules, and troubleshooting. TCP and UDP each have their own port space,
so a TCP port number and a UDP port number are not automatically equivalent.

Ports 0 through 1023 are commonly used as permanent service ports. Client
systems commonly use temporary ephemeral ports for the client side of a
conversation.

## Common Objective 2.1 ports

| Protocol | Common port(s) in this objective | Purpose |
| --- | --- | --- |
| FTP | TCP 20, TCP 21 | File transfer; active data and control channels |
| SSH | TCP 22 | Encrypted remote administration |
| Telnet | TCP 23 | In-clear remote terminal access |
| SMTP | TCP 25 | Email transfer between mail systems; also used by clients to send mail |
| DNS | UDP 53 | Name-to-IP lookup |
| DHCP | UDP 67, UDP 68 | Automatic IP configuration |
| HTTP | TCP 80 | Unencrypted web communication |
| HTTPS | TCP 443 | Encrypted web communication |
| POP3 | TCP 110 | Basic mail retrieval |
| IMAP4 | TCP 143 | Mail retrieval with mailbox management |
| SMB/NetBIOS | UDP 137, TCP 139 | SMB communication using NetBIOS over TCP/IP |
| SMB direct | TCP 445 | Direct SMB file/printer sharing without NetBIOS transport |
| LDAP | TCP 389 | Network directory lookup |
| SNMP | UDP 161, UDP 162 | Network monitoring and management |
| RDP | TCP 3389 | Remote desktop access |

## Troubleshooting focus

When a network service fails, identify:

1. the application protocol;
2. whether the expected transport is TCP or UDP;
3. the destination service port;
4. whether a firewall or network control blocks that protocol/port; and
5. whether the service itself is running and reachable.

Do not treat a port number as security by itself. Ports help route traffic to
the right service and help administrators write firewall rules, but the protocol
and service configuration still determine the security properties.

## References

- Professor Messer 220-1201 v1.70 p.6
- Professor Messer 220-1201 v1.70 p.7
- CompTIA 220-1201 Exam Objectives v2.0, Objective 2.1
