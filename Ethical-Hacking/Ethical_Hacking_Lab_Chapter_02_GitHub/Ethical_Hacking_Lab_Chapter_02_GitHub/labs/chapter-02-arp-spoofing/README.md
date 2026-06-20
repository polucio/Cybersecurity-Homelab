# Chapter 2 – ARP Spoofing / On-Path Traffic Capture

## Objective

Complete the Chapter 2 lab from *Ethical Hacking: A Hands-on Introduction to Breaking In* by using ARP spoofing to place Kali Linux on-path between Metasploitable and the gateway.

The goal was to observe unencrypted HTTP traffic from the victim machine while keeping the lab isolated inside VirtualBox.

## Attack Type

| Item | Description |
|---|---|
| Attack | ARP spoofing / ARP poisoning |
| Category | On-path / man-in-the-middle |
| Layer | Layer 2 local network attack |
| Attacker | Kali Linux |
| Victim | Metasploitable 2 |
| Gateway | OPNsense |

## Lab Roles

| Device | Role | IP Address |
|---|---|---:|
| Kali Linux | Attacker / on-path machine | DHCP assigned |
| Metasploitable 2 | Victim | 192.168.1.121 |
| OPNsense | Router / gateway | 192.168.1.1 |

## High-Level Concept

Normal traffic path:

```text
Metasploitable -> OPNsense
```

Spoofed traffic path:

```text
Metasploitable -> Kali -> OPNsense
```

Kali sends ARP replies in both directions so that:

- Metasploitable believes Kali is the gateway.
- OPNsense believes Kali is Metasploitable.
- Kali forwards traffic so the connection does not break.
- Kali can observe unencrypted traffic crossing the path.

## Outcome

The lab was successful.

`urlsnarf` did not display the expected output from the book, so traffic visibility was validated with `tcpdump`.

Kali captured HTTP traffic from Metasploitable to the OPNsense gateway, including:

```text
HTTP: GET / HTTP/1.0
```

This confirmed that Kali was able to observe HTTP traffic during the ARP spoofing/on-path lab.
