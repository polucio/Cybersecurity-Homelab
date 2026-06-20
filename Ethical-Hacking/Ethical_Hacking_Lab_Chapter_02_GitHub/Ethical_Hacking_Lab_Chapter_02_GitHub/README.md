# Ethical Hacking Home Lab

This repository documents a local cybersecurity lab built while working through *Ethical Hacking: A Hands-on Introduction to Breaking In* by Daniel G. Graham.

The lab is built in VirtualBox using OPNsense as the firewall/router, Kali Linux as the attacker/testing machine, Metasploitable 2 as the intentionally vulnerable target, and Ubuntu Desktop for later labs.

## Current Lab Progress

| Chapter | Lab | Status |
|---|---|---|
| Chapter 1 | Lab setup and first exploit | Complete |
| Chapter 2 | ARP spoofing / on-path traffic capture | Complete |

## Current Network

| Device | Role | IP Address |
|---|---|---:|
| OPNsense | Gateway / firewall / router | 192.168.1.1 |
| Kali Linux | Attacker / on-path machine | DHCP assigned |
| Metasploitable 2 | Victim / vulnerable target | 192.168.1.121 |
| Ubuntu Desktop | Later lab VM | DHCP assigned |

## Safety Notice

This lab is for authorized local cybersecurity practice only.

Metasploitable is intentionally vulnerable and must remain isolated on the VirtualBox internal lab network. Do not run these techniques against systems you do not own or have explicit permission to test.
