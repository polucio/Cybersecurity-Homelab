# Chapter 2 – ARP Spoofing, Traffic Capture, and MAC Flooding

## Objective

Complete the Chapter 2 lab from *Ethical Hacking: A Hands-on Introduction to Breaking In* by exploring Layer 2 attacks inside an isolated VirtualBox lab network.

This chapter focused on ARP spoofing as an on-path/man-in-the-middle attack, observing unencrypted HTTP traffic, inspecting ARP tables, writing Python tools with Scapy, detecting possible ARP spoofing, and testing MAC flooding with `macof`.

## Attack Types Covered

| Attack | Category | Layer | Purpose |
|---|---|---:|---|
| ARP spoofing / ARP poisoning | On-path / man-in-the-middle | Layer 2 | Position attacker between victim and gateway |
| MAC flooding | Switch table flooding | Layer 2 | Send many spoofed source MAC addresses |
| HTTP sniffing | Traffic capture | Layer 3/4/7 visibility | Observe unencrypted traffic after becoming on-path |

## Lab Roles

| Device | Role | IP Address |
|---|---|---:|
| Kali Linux | Attacker / on-path machine | 192.168.1.188 |
| Metasploitable 2 | Victim | 192.168.1.121 |
| OPNsense | Router / gateway | 192.168.1.1 |

## High-Level ARP Spoofing Concept

Normal traffic path:

```text
Metasploitable -> OPNsense
```

Spoofed traffic path:

```text
Metasploitable -> Kali -> OPNsense
```

Kali sends forged ARP replies in both directions so that:

- Metasploitable believes Kali is the gateway.
- OPNsense believes Kali is Metasploitable.
- Kali forwards traffic so the connection does not break.
- Kali can observe unencrypted traffic crossing the path.

## Chapter Outcome

Chapter 2 was completed successfully.

Validation included:

- `urlsnarf` captured HTTP GET requests from Metasploitable.
- `tcpdump` confirmed HTTP traffic was visible to Kali.
- Metasploitable's ARP table showed the gateway IP mapped to Kali's MAC address.
- The Python Scapy ARP spoofer successfully poisoned the victim's ARP table.
- The Python ARP detector identified suspicious IP-to-MAC changes.
- `macof` generated MAC flooding traffic and `tcpdump` captured the resulting burst.
