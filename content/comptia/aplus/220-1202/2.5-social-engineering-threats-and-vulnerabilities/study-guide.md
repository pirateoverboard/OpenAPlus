# Objective 2.5: Social Engineering, Threats, and Vulnerabilities

Objective 2.5 asks you to compare common social-engineering attacks, technical
threats, and conditions that leave systems vulnerable. The useful exam skill is
recognizing what makes one attack different from a similar one: the delivery
channel, target, trust relationship, technical mechanism, or missing control.
(CompTIA Objective 2.5; Professor Messer, pp. 35–41)

## Phishing and Its Variants

**Phishing** uses a deceptive message or site to persuade a person to reveal
information, follow a malicious link, or take an unsafe action. A spoofed
sender, copied branding, or misleading URL may make the request appear
legitimate.

The delivery channel distinguishes several variants:

- **Vishing** uses a voice call or voicemail. Caller-ID information can be
  spoofed, so the displayed number is not proof of identity.
- **Smishing** uses SMS or another text-message channel, often to deliver a link
  or request personal information.
- **QR code phishing** replaces or presents a QR code that sends the scanner to
  an attacker-controlled destination. The destination is harder to inspect
  before scanning than a visible text URL.

Target selection distinguishes two more variants. **Spear phishing** is
customized for a particular person or group and may use information learned
about the target. **Whaling** is spear phishing directed at a senior executive
or another high-value leader. (Professor Messer, p. 35)

## Physical and Human-Focused Attacks

**Shoulder surfing** obtains information by watching a screen, keyboard, or
other input. Awareness, screen placement, and privacy filters reduce exposure.

**Tailgating** is unauthorized entry gained by following an authorized person
through a controlled access point. The approved notes distinguish this from
piggybacking, where the authorized person knowingly allows the follower to
enter; in either case, the follower lacks independent authorization.

**Impersonation** means pretending to be a trusted person, such as a support
technician or senior manager. The attacker may use authority, familiarity, or
technical language to make a request believable.

**Dumpster diving** searches discarded material for useful information.
Names, phone numbers, schedules, invoices, and other fragments can support a
later impersonation or phishing attempt. (Professor Messer, pp. 35–36)

## Availability and Wireless Threats

A **denial-of-service (DoS)** attack makes a service unavailable by exhausting
resources, exploiting a design weakness, or otherwise interrupting operation.
A **distributed denial-of-service (DDoS)** attack has the same availability
goal but coordinates traffic or work from many systems, commonly compromised
devices in a botnet.

An **evil twin** is a malicious wireless access point made to resemble a
legitimate network, often with a matching or similar SSID and captive portal.
It attracts users so the attacker can observe or manipulate their traffic.
Encryption such as HTTPS or a trusted VPN still matters even after joining what
appears to be a familiar wireless network. (Professor Messer, pp. 36–37)

## Spoofing, On-Path, and Zero-Day Attacks

**Spoofing** falsifies identity information so a message, device, address, or
service appears to be another trusted source. Spoofing can help enable other
attacks, but the defining action is the false identity.

An **on-path attack** places the attacker between communicating parties. The
attacker intercepts and relays traffic, potentially reading or altering it
while both endpoints appear to communicate normally. ARP poisoning is one way
to redirect local-subnet traffic through an attacker.

A **zero-day attack** exploits a vulnerability before it has been detected or
publicly disclosed. Attackers may keep an unknown flaw private so they can use
it before defenders publish details and begin remediation. (Professor Messer,
pp. 37–38)

## Password Attacks

A **brute-force attack** systematically tries possible password combinations.
It may operate online against a login service or offline against obtained
password hashes. Account lockouts can slow or stop repeated online attempts.

A **dictionary attack** narrows the guesses to likely words and human-created
patterns. Wordlists may include common substitutions, languages, or terms from
a particular industry. It is more selective than trying the entire possible
character space. (Professor Messer, p. 38)

## Insider and Application Threats

An **insider threat** comes from a person with trusted access or organizational
knowledge, such as an employee, contractor, or recruited insider. The
attacker's familiarity with valuable systems and normal processes can make the
threat difficult to recognize.

**Structured Query Language (SQL) injection** sends crafted input that an
application incorrectly treats as part of a database query. Successful
injection can expose or change database information because the application
failed to keep user input separate from query instructions.

**Cross-site scripting (XSS)** causes attacker-supplied script to run in a
victim's browser in the context of a trusted site. Reflected XSS delivers the
payload through a request such as a malicious link; stored XSS saves the
payload where later visitors receive it. Input validation is central to
preventing both SQL injection and XSS, but their execution targets differ:
SQL injection manipulates database queries, while XSS targets the user's
browser. (Professor Messer, pp. 38–39)

## Business Email and Supply Chain Attacks

**Business email compromise (BEC)** uses a trusted-looking or compromised
business communication channel to manipulate a victim. Common goals include
changing payment instructions, redirecting payroll, or obtaining gift-card
codes. Sensitive or urgent requests should be verified through a separate,
trusted channel.

A **supply chain or pipeline attack** compromises a supplier, service provider,
hardware source, software source, or update mechanism to reach downstream
customers. The attack abuses an organization's trust in something it receives
from another party. Provider reviews, controlled supplier relationships, and
verification of software or updates reduce this exposure. (Professor Messer,
pp. 40–41)

## Conditions That Create Vulnerability

A **non-compliant system** does not meet an organization's approved baseline or
policy. It may have unauthorized software, missing required updates, or another
configuration that falls outside the standard operating environment.

An **unpatched system** lacks available operating-system or application fixes,
leaving known vulnerabilities open. Patch management must identify, test,
prioritize, and deploy fixes rather than assume every device updated itself.

An **unprotected system** is missing an expected defense such as antivirus or a
firewall. Permanently disabling a control to make an application work trades a
visible problem for a larger security exposure.

**End of life (EOL)** indicates that a product has reached a vendor lifecycle
boundary. The approved notes distinguish the end of sales from the later end
of service life, when ongoing support and security fixes stop. For security
planning, the critical risk is operating technology after the vendor no longer
provides necessary patches.

With **bring your own device (BYOD)**, an employee-owned device handles company
access or data. Personal ownership and mixed home/work use complicate security
requirements, malware exposure, data separation, and what happens to company
data when the device is lost, sold, or replaced. (Professor Messer, p. 41)

## References

- CompTIA A+ 220-1202 Exam Objectives v4.0, Objective 2.5
- Professor Messer 220-1202 v1.40 pp. 35–41
