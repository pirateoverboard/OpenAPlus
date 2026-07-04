# Objective 5.5 Interview Practice - Troubleshooting Networks

Use these prompts to practice spoken help desk answers. These are not regular
Anki cards and are not exported to TSV.

## Scenario: No Network Connectivity

Question:
A user says their desktop has no network connectivity. How would you explain
your troubleshooting path?

Strong answer pattern:
I would first confirm the scope and whether this affects one device, one area,
or many users. Then I would work from closest to farthest: check link light and
cabling, verify local IP configuration, test loopback or local address as
appropriate, test the default gateway, and then test a known remote address. I
would document each result so escalation shows exactly where the path fails.

What to say first:
"I would start by identifying whether this is one endpoint or a wider outage."

Information to gather:
- Whether other users or devices are affected.
- Link light or physical connection status.
- Local IP address and gateway.
- Which ping or connectivity tests pass or fail.

Mistakes to avoid:
- Restarting network equipment before checking scope.
- Treating internet failure and local link failure as the same problem.

## Scenario: Intermittent Wireless

Question:
A user says Wi-Fi drops only in one conference room. What would you ask and
check?

Strong answer pattern:
I would ask whether the symptom follows the user or the room. I would compare
signal strength in that location, look for interference or reflective surfaces,
and consider access point placement or channel issues. I would avoid replacing
the user's laptop until the location pattern is tested.

What to say first:
"I would use the location pattern as evidence before blaming the endpoint."

What to document:
- Location and time pattern.
- Signal quality observations.
- Whether other devices have the same symptom.
- Any access point, channel, or interference evidence.

Mistakes to avoid:
- Assuming the wireless adapter is bad when only one room is affected.
- Ignoring interference or placement.

## Scenario: Slow Network Complaint

Question:
A user says "the network is slow." How would you make that actionable?

Strong answer pattern:
I would ask what specific application or task is slow and whether others are
affected. Then I would confirm end-to-end connectivity with a practical test,
validate with a speed test where appropriate, and evaluate each hop or segment
if the symptom is reproducible. If needed, I would escalate with timestamps and
test results.

What to say first:
"I would turn the vague complaint into a measurable symptom."

Information to gather:
- Application or service affected.
- Time and scope.
- Speed test or ping results.
- Any hop, utilization, error, or filtering evidence.

## Scenario: Choppy Voice Calls

Question:
A user reports choppy VoIP calls. What would you focus on?

Strong answer pattern:
I would treat this as a real-time traffic issue. I would check internet speed
and latency, verify local networking equipment, and collect performance evidence
such as packet loss, jitter, or packet captures if simpler tests do not explain
it. I would document the timing and whether other real-time apps are affected.

What to say first:
"I would check whether delay or delay variation is disrupting real-time media."

When to escalate:
Escalate when repeated tests show provider, network equipment, or path issues
beyond the local endpoint.

## Scenario: Port Flapping

Question:
A switch port keeps going up and down for one workstation. How would you isolate
it?

Strong answer pattern:
I would verify the cable and wiring first, then move the connection to another
switch port. If the symptom follows the cable or workstation, I would focus on
that path. If it stays with the original switch interface, I would escalate the
switch port or network hardware evidence.

What to document:
- Cable tested.
- Original and alternate switch ports.
- Whether the symptom followed the endpoint or stayed with the switch.

Mistakes to avoid:
- Replacing the workstation before testing the cable and switch interface.

## Scenario: Intermittent Internet Outage

Question:
Several users report internet drops throughout the day. What evidence would you
collect before contacting the ISP?

Strong answer pattern:
I would determine scope, run ongoing pings, use traceroute to a known location,
run speed tests during the issue, and record timestamps. If the evidence points
outside the local network, I would contact the ISP with account/contact details,
test results, and any SLA expectations.

What to say first:
"I would collect repeatable evidence before escalating to the provider."

What to document:
- Affected users or locations.
- Ping, traceroute, and speed-test results.
- Timestamps and duration.
- ISP account/contact information and SLA details.
