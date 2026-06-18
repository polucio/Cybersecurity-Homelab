# Chapter 1 – Setting Up

## Objective

Build the foundational virtual lab environment for the Ethical Hacking book using VirtualBox and OPNsense.

## Source Material

Based on Chapter 1, "Setting Up," from:

*Ethical Hacking: A Hands-on Introduction to Breaking In*  
Daniel G. Graham  
No Starch Press

## Lab Design

The book's lab uses five virtual machines:

1. Firewall/router
2. Kali Linux
3. Metasploitable
4. Ubuntu Desktop
5. A second Ubuntu Desktop for later private-network work

For this implementation:

- OPNsense replaces pfSense.
- Metasploitable 2 is used as the vulnerable Linux server.
- Kali is used as the attacker/testing machine.
- Ubuntu Desktop is installed but parked until later chapters.
- The second Ubuntu/private-network VM is deferred until Chapter 14.

## Current Chapter 1 VM Status

| VM | Status |
|---|---|
| OPNsense | Installed and running |
| Metasploitable 2 | Installed and reachable |
| Kali Linux | Installed and reachable |
| Ubuntu Desktop | Installed for later use |

## Network Summary

| VM | Adapter | VirtualBox Network Mode | Network Name | Purpose |
|---|---:|---|---|---|
| OPNsense | Adapter 1 | Bridged Adapter | Physical Wi-Fi/Ethernet | WAN |
| OPNsense | Adapter 2 | Internal Network | Internal LAN | Lab LAN gateway |
| Kali | Adapter 1 | Internal Network | Internal LAN | Attacker/test machine |
| Metasploitable | Adapter 1 | Internal Network | Internal LAN | Vulnerable target |
| Ubuntu | Adapter 1 | Internal Network | Internal LAN | Desktop victim/utility VM |

## Confirmed IP Addresses

| Device | IP Address |
|---|---:|
| OPNsense LAN gateway | 192.168.1.1 |
| Kali Linux | 192.168.1.188 |
| Metasploitable 2 | 192.168.1.121 |

These IP addresses are DHCP-assigned and may change after reboot unless static DHCP leases are configured later.

## Important Notes

- Only OPNsense uses Bridged Adapter.
- Kali, Metasploitable, and Ubuntu stay on the internal LAN.
- Metasploitable must not be exposed directly to the home network or internet.
