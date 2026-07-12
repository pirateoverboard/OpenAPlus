# Objective 4.2: Cloud Computing Concepts

Objective 4.2 summarizes common cloud deployment models, service models, and
cloud characteristics. The goal is to recognize which model or characteristic
fits a short scenario and to understand the tradeoff behind the choice.

## Cloud Computing Overview

Cloud computing provides computing services from shared infrastructure that can
be provisioned and released quickly. Instead of buying and operating every
server, storage system, network device, platform, and application locally, an
organization can consume only the cloud resources it needs.

Cloud use does not remove responsibility. The service model determines which
parts are managed by the provider and which parts remain the customer's
responsibility.

## Deployment Models

A private cloud is dedicated to one organization. It may run in an internal
data center or on dedicated hosted resources, but the important idea is that
the cloud is restricted to that organization instead of being open to the
general public.

A public cloud is offered by a provider over the Internet and is available to
many customers. Customers usually do not own the underlying infrastructure, and
multiple customers can consume services from the same provider environment.

A hybrid cloud combines private and public cloud resources. Organizations use
this model when some workloads need private control while other workloads can
use public cloud scale, reach, or services.

A community cloud is shared by several organizations with a common purpose or
set of requirements. It is not simply "public for everyone"; it is a shared
environment for a defined group.

## Service Models

Infrastructure as a Service (IaaS) provides core computing infrastructure such
as compute, storage, networking, and virtualization. The customer still manages
the operating systems, applications, data, access, and much of the security
configuration.

Platform as a Service (PaaS) provides an application platform or framework.
The provider manages more of the underlying platform so developers can focus on
building and deploying applications.

Software as a Service (SaaS) provides a complete application that users access
as a service. The provider manages the application platform and hosting, while
the customer mainly manages users, data, configuration, and access policies.

## Resource and Cost Characteristics

Cloud services may use shared resources, dedicated resources, or a mix of both.
Shared resources allow multiple customers or workloads to use the provider's
larger resource pool. Dedicated resources are reserved for a particular
organization or workload.

Metered utilization means usage is measured, often for billing or reporting.
Cloud costs can be based on compute time, stored data, transactions, or network
traffic. Ingress is traffic entering the cloud service, and egress is traffic
leaving it. Egress is especially important because moving data out of a cloud
service may create usage charges.

Non-metered utilization uses a fixed block, allocation, or flat access model
instead of charging directly for each measured unit of use.

## Availability, Elasticity, Synchronization, and Multitenancy

Elasticity is the ability to scale cloud resources up or down as demand
changes. The key idea is responsive resource adjustment, not simply having a
large server.

Availability describes keeping a service reachable when users need it.
Redundancy across systems or locations can improve availability because the
service can continue when one component or location has a problem.

File synchronization keeps data consistent across cloud locations, application
instances, or client devices. Synchronization is useful when users or services
need the same current files from more than one place.

Multitenancy means multiple customers or tenants use the same cloud
infrastructure while their data and access remain logically separated. This is
a core reason public cloud services can serve many customers from shared
provider resources.

## Scope Caveats

Objective 4.2 does not require vendor pricing tables, provider product names,
cloud architecture certifications, Kubernetes administration, detailed service
level agreement math, or migration-project planning. Desktop as a Service is
useful context for Objective 4.1 VDI, but the explicit Objective 4.2 service
models are IaaS, PaaS, and SaaS.

## References

- CompTIA 220-1201 Exam Objectives v4.0, Objective 4.2
- Professor Messer 220-1201 v1.70 pp.47-48
