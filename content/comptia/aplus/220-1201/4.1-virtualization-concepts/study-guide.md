# Objective 4.1: Virtualization Concepts

Objective 4.1 explains why virtualization is used and how virtualization
platforms are organized. The focus is conceptual: virtual machines, desktop
virtualization, containers, resource requirements, security boundaries, network
choices, storage needs, and Type 1 versus Type 2 hypervisors.

## Virtual Machines and Purpose

A virtual machine is a software-defined computer that runs as a guest on
physical hardware. Each guest has its own operating system, assigned CPU,
memory, storage, network settings, and security controls. The host still owns
the real hardware, but the guest behaves like a separate computer.

Virtual machines are useful for sandboxing because the test system can be
isolated from production. A technician or developer can test code, settings, or
software behavior without risking the main system. Snapshots can also make it
possible to return a VM to a previous state after a test.

Test and development environments use VMs to keep work-in-progress software
separate from production systems. This lets developers build and validate an
application in a controlled environment before release.

Application virtualization can support legacy software or cross-platform work.
If an application needs an older operating system, the older OS can run inside
a VM. If a user needs tools from several operating systems, multiple guests can
run on one physical computer without rebooting between operating systems.

## Requirements

Virtualization needs enough resources for the host and each guest. CPU
virtualization support can improve performance and may need to be enabled in
firmware. Memory must cover the host operating system plus the guest workloads,
and storage must hold each guest's virtual disk image.

Network requirements depend on how guests should communicate. A VM can share
the host's network connection through NAT, appear as its own device on the
physical network through bridged networking, or stay inside a private virtual
network.

Security requirements apply to both hosts and guests. Each guest should be
treated like a separate computer with its own firewall, anti-malware, patching,
and access control needs. Unknown or untrusted VMs are risky because they may
contain unwanted software. The hypervisor is also important because it manages
the virtual platform and guests.

## Desktop Virtualization

Virtual Desktop Infrastructure (VDI) runs desktop sessions or applications on
remote infrastructure while the client device mainly displays the session and
sends input. This can reduce endpoint hardware requirements, but it increases
dependence on reliable network connectivity because the desktop experience
happens across the network. Hosted virtual desktops may also be described as
Desktop as a Service (DaaS).

## Containers

A container packages an application with the code and dependencies it needs to
run. Containers are lighter than full VMs because they use the host operating
system kernel instead of carrying a full guest operating system for each
application instance.

Containers are designed to be portable and isolated. That isolation helps keep
applications separated from each other, but containers still depend on the host
operating system and container runtime.

## Hypervisors

A hypervisor, also called a virtual machine manager, creates and manages the
virtual platform for guest operating systems.

A Type 1 hypervisor is bare metal. It runs directly on the hardware and acts as
the primary platform for guest operating systems. Type 1 hypervisors are common
on dedicated virtualization servers.

A Type 2 hypervisor is hosted. It runs as an application on an existing desktop
operating system such as Windows, Linux, or macOS. Type 2 hypervisors are common
for labs, testing, and client-side virtualization.

## Scope Caveats

Objective 4.1 does not require memorizing vendor product feature matrices,
exact hardware sizing formulas, Docker commands, Kubernetes administration,
cloud service pricing, or the cloud service model details covered in Objective
4.2. Product examples can help recognition, but the stable exam target is the
concept.

## References

- CompTIA 220-1201 Exam Objectives v4.0, Objective 4.1
- Professor Messer 220-1201 v1.70 pp.46-47
