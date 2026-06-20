# Chapter 1 – Setting Up

## Objective

Build the foundational virtual lab environment for the Ethical Hacking book using VirtualBox and OPNsense, then complete the first controlled exploit against Metasploitable 2.

## Source Material

Based on Chapter 1, "Setting Up," from:

*Ethical Hacking: A Hands-on Introduction to Breaking In*  
Daniel G. Graham  
No Starch Press

## Implementation Notes

The book uses pfSense as the firewall/router. This lab uses OPNsense as a modern equivalent because pfSense setup and distribution have changed since the book was published, while OPNsense preserves the same basic architecture for this lab.

## Current Chapter 1 VM Status

| VM | Status |
|---|---|
| OPNsense | Installed and running |
| Metasploitable 2 | Installed, reachable, and exploited in the lab |
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
| Ubuntu Desktop | 192.168.1.165 |

These IP addresses are DHCP-assigned and may change after reboot unless static DHCP leases are configured later.

## Chapter 1 Outcome

The first exploit was completed successfully.

Kali connected to the vulnerable vsFTPd 2.3.4 service on Metasploitable, triggered the backdoor behavior, connected to the shell on port 6200, confirmed root access with `whoami`, and rebooted the Metasploitable VM to prove command execution.
