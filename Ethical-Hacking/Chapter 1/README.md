# Lab 01 – OPNsense Firewall Deployment

## Objective

Build the foundational network infrastructure for a cybersecurity and SecurityX (CAS-005) home lab environment using VirtualBox and OPNsense.

## Source Material

This lab is based on the virtual lab architecture presented in:

*Ethical Hacking: A Hands-on Introduction to Breaking In* by Daniel G. Graham.

The original lab environment utilizes pfSense as the perimeter firewall. OPNsense 26.1.6 was selected as a modern equivalent due to changes in the pfSense distribution and installation process since publication.

The objective of this project is to recreate and expand the book's cybersecurity lab environment using current technologies and industry practices.
## Environment

### Virtualization Platform
- Oracle VirtualBox 7.2.10

### Firewall Platform
- OPNsense 26.1.6
- FreeBSD 64-bit

### Virtual Machine Configuration
- 2 vCPUs
- 2 GB RAM
- 20 GB Virtual Disk (ZFS)

## Project Goals

- Learn hypervisor deployment and management
- Deploy a virtual firewall appliance
- Configure WAN and LAN interfaces
- Create a foundation for future cybersecurity labs
- Gain hands-on experience with network segmentation and routing concepts

## Lab Adaptation

The original lab design used pfSense as the perimeter firewall. Due to changes in the pfSense distribution and installation process since the book was published, OPNsense 26.1.6 was selected as a modern equivalent firewall platform.

OPNsense provides comparable functionality for:

- Firewall administration
- Routing and NAT
- Network segmentation
- DHCP and DNS services
- Packet capture and traffic analysis

This substitution preserves the learning objectives of the original lab while using a currently maintained platform suitable for modern home lab and enterprise-style environments.

## Installation Summary

- Installed VirtualBox 7.2.10 and Extension Pack
- Enabled AMD-V/SVM virtualization in BIOS
- Installed OPNsense 26.1.6
- Configured WAN (NAT) and LAN (Internal Network)

## Interface Assignment

- WAN -> le0
- LAN -> le1

## Final Network Configuration

### LAN
- 192.168.1.1/24

### WAN
- DHCP: 10.0.2.15/24

## Skills Practiced

- Virtualization
- Hypervisor management
- FreeBSD administration
- Firewall deployment
- Network segmentation
- Routing concepts
- Infrastructure security
- Troubleshooting virtualized network appliances

## Challenges Encountered

- VirtualBox initially failed to start the VM because AMD-V/SVM was disabled in BIOS.
- The VM was initially configured as Other/Unknown and required reconfiguration to FreeBSD (64-bit).
- Network interfaces had to be manually assigned to establish WAN and LAN connectivity.
- The original pfSense-based book instructions no longer matched the current pfSense distribution workflow.

## Resolution

- Enabled AMD-V/SVM in BIOS.
- Reconfigured the guest OS profile to FreeBSD (64-bit).
- Assigned WAN and LAN interfaces through the OPNsense console.
- Selected OPNsense as a modern equivalent to preserve the firewall, routing, and segmentation goals of the original lab.

## Next Steps

- Deploy Kali Linux
- Connect Kali to the OPNsense LAN
- Configure DHCP
- Explore OPNsense Web UI
- Begin ethical hacking labs
