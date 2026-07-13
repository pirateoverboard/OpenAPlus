# Objective 1.10: Application Installation Requirements

Objective 1.10 asks you to choose and install an application only after checking
that the target environment meets its requirements. The practical sequence is
to verify compatibility and resources, choose an appropriate distribution
method, and consider what the change could affect. (CompTIA Objective 1.10;
Professor Messer, pp. 22-23)

## System Requirements and Compatibility

An application's published requirements establish the minimum supported
environment. Check the operating system, processor architecture, CPU, memory,
graphics, storage, and any required external hardware before installation.

### Operating system and architecture

Application-to-OS compatibility includes the supported operating system and
version as well as 32-bit or 64-bit architecture. A 64-bit application requires
a 64-bit operating system. A 64-bit Windows installation can commonly run
32-bit applications, but the reverse combination does not work. Hardware
drivers must also match the operating-system architecture. (Professor Messer,
p. 22)

A 32-bit address space contains 2^32 addresses. When each address identifies
one byte, that corresponds to approximately 4 GiB of address space. This is why
32-bit operating systems are commonly associated with a roughly 4 GB
system-memory limit, while 64-bit platforms can address far more. The
application's own requirements still determine whether the available memory is
sufficient.

### CPU, RAM, graphics, and storage

- **CPU:** Compare the application's required processor and processing speed
  with the installed CPU. A demanding workload such as video editing typically
  needs more processing capacity than a simple office application.
- **RAM:** The application needs memory in addition to the operating system and
  other running programs. Insufficient RAM can cause poor performance or keep
  the application from operating.
- **Graphics:** Integrated graphics shares system memory, while a dedicated or
  discrete graphics card has its own video memory. Check whether the application
  requires dedicated graphics and how much VRAM it specifies.
- **Storage:** Account for both the space needed to install the application and
  the space it may consume while in use. Application data and other working
  files can make the post-installation requirement more important than
  the installer size alone. (Professor Messer, p. 22)

### External hardware tokens

Some high-value applications use a physical token, commonly connected by USB,
to authorize use. If the application requires one, it operates only while the
required token is available and connected. Token availability is therefore an
installation and ongoing-use requirement, not merely a packaging detail.
(Professor Messer, p. 22)

## Distribution Methods

- **Physical media:** Installation files arrive on removable media such as an
  optical disc or USB drive. This method requires access to the corresponding
  drive or port.
- **Mountable ISO file:** An ISO is an optical-disc image stored as one file.
  Mounting it makes its contents appear as a separate drive, allowing the OS to
  use the installation files without a physical disc.
- **Downloadable package:** The installer is retrieved electronically. Use a
  trusted source such as the software publisher or a centralized application
  store rather than an unrelated third-party download site.
- **Image deployment:** A prepared system image can install the operating
  system and included applications together. Images support fast, consistent
  deployment but must match the target platform and its device drivers.
  Virtual machines are well suited to this approach because their presented
  hardware can be consistent. (Professor Messer, pp. 22-23)

## Impact Considerations

Installing or updating an application can affect more than the application
itself. Evaluate impact at four levels before changing a production system:

- **Device:** The application or upgrade can introduce slowdowns, stop working,
  or delete local files.
- **Network:** The application may need access to internal services or specific
  rights and permissions on shared resources.
- **Operation:** A changed application can disrupt a time-sensitive workflow or
  require users to follow a different process.
- **Business:** Application downtime can interrupt a critical process and can
  affect other teams that depend on its results. (Professor Messer, p. 23)

Applications run with the rights and permissions of the user who launches
them, so an untrusted application can cause significant problems within that
user's access. Treat installation as a controlled change, especially when the
device or workflow is business-critical.

## Installation Decision Sequence

1. Confirm the application supports the operating system and architecture.
2. Compare CPU, RAM, graphics/VRAM, storage, and token requirements with the
   target device.
3. Select a distribution method that fits the source media and deployment
   scale.
4. Consider device, network, operational, and business effects before rollout.
5. Install only when the environment satisfies the requirements and the impact
   is acceptable.

## References

- CompTIA A+ 220-1202 Exam Objectives v4.0, Objective 1.10
- Professor Messer 220-1202 v1.40 pp. 22-23
