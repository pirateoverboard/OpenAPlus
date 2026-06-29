# Objective 2.3 study guide: Network Services

Objective 2.3 covers common network services and the symptoms or use cases that
point to each service. The goal is to recognize what a service does, when a
technician would use it, and what kind of failure it may cause when unavailable
or misconfigured.

## Scope and source handling

CompTIA 220-1201 Objective 2.3 defines the scope. Professor Messer 220-1201
v1.70 pages 9–10 were used as private validation/reference pages only. This
guide uses original wording and does not reproduce source tables, diagrams,
layout, or phrasing.

## Core infrastructure services

DNS translates names and IP addresses. When users can reach a resource by IP
address but not by name, DNS is a likely path to investigate.

DHCP automatically provides IP configuration. In small networks, the service may
be integrated into a router. In larger environments, DHCP commonly runs on
centralized and redundant servers.

NTP provides time synchronization. Shared time matters for logs,
authentication, encryption, backups, and troubleshooting timelines. The approved
source associates NTP with UDP 123.

## User-facing services

File share services centralize access to documents and other files. The user may
only see actions such as copy, delete, or rename, while the underlying protocol
is hidden by the front end.

Print servers provide printing services for network devices. A print server can
be software on a computer or functionality built into a network printer.

Mail servers store incoming mail and send outgoing mail. They are often managed
by an ISP or IT department and are important enough to require reliable support.

Web servers respond to browser requests using web protocols and provide web
pages to clients.

Authentication servers centralize login authentication to resources. They are
usually enterprise services and are often deployed redundantly.

## Application and logging services

Database servers store structured data. Relational databases organize data in
tables and link related information. SQL is a common language for accessing
database data.

Syslog centralizes message logging from diverse systems. Centralized logging can
support troubleshooting, monitoring, and security event review.

Proxy servers sit between clients and the destination service. A client makes a
request to the proxy, the proxy performs the request, and the proxy returns the
result. Proxies may provide access control, caching, URL filtering, or content
scanning.

Load balancers distribute requests across multiple servers. Users may not see
the individual back-end servers, and a load balancer can help keep a service
available when one server fails.

Spam gateways filter unsolicited or malicious email before it reaches users.
They may be deployed on-site or as a cloud-based service.

All-in-one security appliances combine multiple security and networking
functions, such as firewalling, filtering, malware inspection, VPN endpoint
support, IDS/IPS, routing, switching, and traffic shaping.

## Specialized and constrained systems

SCADA and ICS environments manage industrial control systems such as power,
manufacturing, facilities, energy, or logistics systems. These environments
require strong segmentation and should not be broadly exposed.

Legacy systems are older systems that may still be important. Embedded systems
are purpose-built devices where direct operating-system access is not typical.

IoT devices include appliances, smart speakers, thermostats, smart doorbells,
and similar network-connected devices. Segmentation can limit the impact if one
of these devices is compromised.

## Intentionally limited details

OpenAPlus does not create cards for vendor-specific products, exact sizing
requirements, specific database brands, or detailed appliance feature matrices
in this draft. Those details are either volatile, implementation-specific, or
better left as study-guide context unless a reviewer confirms official-scope
active-recall value.

## References

- Professor Messer 220-1201 v1.70 p.9
- Professor Messer 220-1201 v1.70 p.10
- CompTIA 220-1201 Exam Objectives v2.0, Objective 2.3
