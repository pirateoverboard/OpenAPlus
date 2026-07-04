# Objective 5.5 - Troubleshooting Networks

Objective 5.5 focuses on network symptoms and the evidence a technician gathers
to decide where the fault is. Good network troubleshooting narrows the path:
physical link, local adapter, local IP configuration, default gateway, upstream
connectivity, wireless environment, service authentication, or provider outage.

## No Connectivity and Limited Connectivity

Start no-connectivity tickets with the closest evidence. A missing link light or
unplugged cable points to the physical connection. If the physical path appears
up, loopback and local-address tests can separate the host protocol stack,
adapter/configuration, and local link from broader network problems.

The default gateway is the next major boundary. Reaching the gateway shows that
the host can communicate on the local network. Reaching a known remote address
tests beyond the local router. If a Windows client reports limited connectivity
or no internet access, check the local IP address before changing remote
services. An APIPA address is a troubleshooting clue that automatic addressing
failed and normal routed internet access is not available.

## Wireless Symptoms

Intermittent wireless connectivity should not be treated as a generic "bad
network" complaint. Consider interference, signal strength, channel selection,
multipath effects from reflective surfaces, and access point placement. Movement
patterns matter: a symptom that appears only in one area is often environmental
or placement-related.

Signal-to-noise ratio describes how much useful wireless signal exists compared
with unwanted noise. A higher ratio is better; a low ratio supports an
interference or signal-quality theory.

## Slow Speeds and Path Isolation

When a user says "the network is slow," confirm the symptom end to end before
assuming the whole network is at fault. Use a practical test such as application
login, ping, or speed testing to verify the complaint. If the symptom is real,
evaluate each hop or segment for utilization, errors, filtering, and throughput.
A packet capture may be justified when simpler tests cannot explain the symptom.

## Voice, Video, Latency, and Jitter

Real-time traffic is sensitive to delay variation. Jitter can cause choppy voice
or video because late media is often not useful by the time it arrives. Poor
VoIP quality should prompt checks of the internet link, local network equipment,
and network performance evidence. High latency should be measured along the path
instead of guessed from a single user complaint.

## Port Flapping, Authentication, and Provider Scope

Port flapping means an interface repeatedly goes up and down. Start with wiring,
then move the connection to another switch interface to see whether the symptom
follows the device/cable or stays with the switch port.

Authentication issues require a different path than link failures. Verify that
the user has valid credentials and an active session; logging out and back in
can refresh the session. Packet capture may help when the authentication flow is
hidden inside an application or service.

For intermittent internet connectivity, determine the scope and collect
evidence with ongoing pings, traceroute, and speed tests. Provider-side issues
should be escalated to the ISP with contact/account information, test results,
and service-level expectations.

## Interview-ready Troubleshooting Language

For a help desk interview, explain network troubleshooting as narrowing a path
instead of trying random fixes:

"I would first confirm the symptom and scope, then test from closest to farthest:
physical link, local IP configuration, gateway, and then a known remote address.
For wireless symptoms I would compare location, signal, interference, and access
point placement. For performance or intermittent issues I would collect repeatable
evidence such as pings, traceroute, speed tests, and packet captures when needed.
I would document each result and escalate to the ISP or network team with the
scope and evidence."

Use the objective-local `interview/` directory for longer spoken-answer
practice. Regular Anki cards stay atomic: one symptom, check, interpretation,
documentation item, or escalation decision.

## References

- Professor Messer 220-1201 v1.70 p.55
- Professor Messer 220-1201 v1.70 p.56
- CompTIA 220-1201 Exam Objectives v2.0, Objective 5.5
