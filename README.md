# Lab 01 – OPNsense Firewall Deployment

## Objective
Build the foundational network infrastructure for a cybersecurity and SecurityX (CAS-005) home lab environment using VirtualBox and OPNsense.

## Environment

### Virtual Machine
- OPNsense 26.1.6
- FreeBSD 64-bit
- 2 vCPUs
- 2 GB RAM
- 20 GB Virtual Disk (ZFS)

## Project Goals
- Learn hypervisor deployment and management
- Deploy a virtual firewall appliance
- Configure WAN and LAN interfaces
- Create a foundation for future cybersecurity labs
- Gain hands-on experience with network segmentation and routing concepts

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
- Hypervisor Management
- FreeBSD Administration
- Firewall Deployment
- Network Segmentation
- Routing Concepts
- Infrastructure Security

## Next Steps
- Deploy Kali Linux
- Connect Kali to OPNsense
- Configure DHCP
- Explore OPNsense Web UI
- Begin ethical hacking labs
