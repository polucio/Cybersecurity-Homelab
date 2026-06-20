# Attack Summary – Chapter 2

## Summary

Chapter 2 introduced ARP spoofing as an on-path/man-in-the-middle attack.

In this lab, Kali Linux was positioned between Metasploitable and the OPNsense gateway using ARP spoofing. IP forwarding was enabled on Kali so traffic could continue passing between the victim and gateway while Kali observed the traffic.

The chapter also covered MAC flooding, which differs from ARP spoofing because it targets a switch's MAC address table rather than poisoning IP-to-MAC mappings.

## Why ARP Spoofing Is an On-Path Attack

ARP spoofing abuses trust in ARP replies on a local network.

The attacker sends false ARP replies so systems update their ARP tables with the attacker's MAC address.

In this lab:

```text
Metasploitable was told: "Kali is the gateway."
OPNsense was told: "Kali is Metasploitable."
```

This placed Kali in the communication path.

## What Was Captured

Kali observed a request from Metasploitable to the OPNsense web interface:

```text
192.168.1.121 -> OPNsense.internal.http
HTTP: GET / HTTP/1.0
```

`urlsnarf` also displayed the HTTP request:

```text
192.168.1.121 - - [20/Jun/2026:13:59:51 -0400] "GET http://192.168.1.1/ HTTP/1.0" - - "-" "Wget/1.10.2"
```

## Key Lesson

Unencrypted HTTP traffic can be observed during an on-path attack.

HTTPS helps protect the contents of web traffic because the application data is encrypted, although metadata such as IP addresses, ports, timing, and traffic volume may still be visible.
