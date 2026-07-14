# Objective 2.1: Security Measures and Purposes

Objective 2.1 asks you to connect a security control with the risk or access
problem it addresses. The useful distinction is not simply physical versus
logical: some controls deter, some detect, some authenticate, some authorize,
and some limit the duration or scope of access. (CompTIA Objective 2.1;
Professor Messer, pp. 24–27)

## Physical Security

Physical controls protect facilities, people, and equipment.

- **Bollards** are sturdy barriers that keep vehicles away from a protected
  area while allowing pedestrian access to be directed elsewhere.
- An **access control vestibule** uses two interlocked doors so passage can be
  limited to one person or controlled group at a time.
- A **badge reader** reads an identification medium such as RFID, NFC, or a
  magnetic stripe for access or attendance decisions.
- **Video surveillance** records activity for monitoring and later review.
- **Alarm systems** signal a detected security event. A **motion sensor** is a
  specific detector that reacts to movement without requiring a camera.
- **Door locks** control entry to a room or building. **Equipment locks** and
  locked racks or cabinets restrain particular assets.
- **Security guards** can verify identities, enforce access lists, manage
  visitors, and respond to events.
- **Fences** establish a visible perimeter and can be designed to resist
  cutting or climbing. (Professor Messer, p. 24)

## Physical Access Security

Access credentials can be carried, stored on a device, or based on a physical
trait.

- A **key fob** is a small proximity or contactless token commonly used instead
  of a mechanical door key.
- A **smart card** stores a credential and normally works with a card reader;
  it is often combined with another factor.
- A **mobile digital key** lets an authorized phone act as a key for a door,
  vehicle, or other lock.
- Mechanical **keys** still serve standalone locks. Controlled storage and a
  check-in/check-out record improve accountability.
- **Biometrics** authenticate from a physical or behavioral characteristic.
  Retina, fingerprint, palm-print, facial, and voice systems use different
  traits, but all require careful handling because a compromised biometric
  trait cannot be replaced as easily as a password.
- **Lighting** improves visibility for people and cameras and can discourage
  activity that depends on concealment.
- A **magnetometer** detects metal objects. It is a screening control, not an
  identity credential, and it does not detect nonmetallic objects. (Professor
  Messer, p. 25)

## Least Privilege, Zero Trust, and ACLs

The **principle of least privilege** gives users and applications only the
rights needed for their assigned work. It limits what a compromised account or
malicious process can reach.

A **Zero Trust model** assumes that location inside a network does not make a
person, device, or process trustworthy. Access is continually based on
verification and policy.

An **access control list (ACL)** contains permit or deny rules. ACLs can filter
network traffic using attributes such as addresses, protocols, and ports, and
the same general allow/deny idea can protect operating-system resources.
(Professor Messer, p. 26)

## Multifactor Authentication and One-Time Codes

**Multifactor authentication (MFA)** requires evidence from different factor
categories, such as something known, possessed, or inherent to the user. Two
passwords are two pieces of knowledge, not two factors.

MFA and account verification can use several delivery mechanisms:

- **Email** can validate control of an address or deliver a verification code.
- A **hardware token** generates or holds authentication evidence on a
  dedicated device.
- An **authenticator application** generates codes on a phone without relying
  on a text message for every login.
- **SMS** and a **voice call** deliver codes through a phone number. Both depend
  on the security of the telephone channel and number assignment.
- A **time-based one-time password (TOTP)** is derived from a shared secret and
  the current time, so it expires after a short interval.
- A general **one-time password/passcode (OTP)** is valid for one use. OTP is a
  category; TOTP is a time-based member of that category. (Professor Messer,
  p. 26)

## Federated and Simplified Access

**Security Assertion Markup Language (SAML)** is an open standard that lets an
identity provider pass authentication and authorization assertions to another
service. This enables a service to rely on a separate identity provider.

**Single sign-on (SSO)** lets a user authenticate once and then use assigned
resources without entering credentials again for each one during the allowed
session. SSO reduces repeated prompts; it does not remove the need to control
what the identity may access. (Professor Messer, p. 27)

## Privileged and Device Access

**Just-in-time access** grants elevated rights only for a limited period or
session instead of leaving them permanently assigned. Temporary accounts or
credentials can be removed when the work is complete.

**Privileged access management (PAM)** centrally controls powerful
administrator or root access. It can vault credentials, approve requests,
track use, and provide temporary access; just-in-time access is one technique
within the broader PAM approach.

**Mobile device management (MDM)** centrally applies policy to managed mobile
devices. It can control device access, screen locks, applications, and the
separation of organizational data. (Professor Messer, p. 27)

## Data and Identity Controls

**Data loss prevention (DLP)** identifies sensitive information and blocks or
controls unauthorized disclosure through endpoints, email, cloud services, or
other channels.

**Identity and access management (IAM)** manages digital identities and their
access throughout a lifecycle. It connects authentication, authorization,
governance, and timely permission assignment.

**Directory services** provide a centralized database of identities and
resources such as users, computers, groups, printers, and file shares. They
support centralized authentication and access administration. IAM is the
broader identity-and-access discipline; a directory is one foundational
service it may use. (Professor Messer, p. 27)

## References

- CompTIA A+ 220-1202 Exam Objectives v4.0, Objective 2.1
- Professor Messer 220-1202 v1.40 pp. 24–27
