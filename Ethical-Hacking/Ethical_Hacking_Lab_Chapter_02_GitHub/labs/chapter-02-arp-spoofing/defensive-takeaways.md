# Defensive Takeaways – Chapter 2

## Main Lesson

Layer 2 attacks can allow an attacker on the same local network to observe or disrupt traffic.

ARP spoofing can place an attacker on-path between a victim and gateway.

MAC flooding can create noisy Layer 2 traffic and may affect switching behavior depending on the environment.

## Why HTTP Was Visible

HTTP traffic is not encrypted.

During the lab, Kali was able to observe:

```text
HTTP: GET / HTTP/1.0
```

This shows that unencrypted requests can be visible to an on-path attacker.

## Why HTTPS Matters

HTTPS encrypts the contents of web traffic.

An on-path attacker may still observe metadata such as:

- Source IP
- Destination IP
- Port numbers
- Timing
- Amount of traffic

But HTTPS helps protect the actual page contents, credentials, session cookies, and other sensitive application data.

## Defensive Controls

Possible defenses include:

- Prefer HTTPS over HTTP.
- Avoid sending credentials over unencrypted protocols.
- Use network segmentation to limit who can reach sensitive systems.
- Use managed-switch protections where available, such as DHCP snooping and Dynamic ARP Inspection.
- Monitor for duplicate or suspicious ARP replies.
- Avoid placing untrusted systems on the same local network as sensitive devices.
- Keep systems updated and remove unnecessary services.
- Use switch port security where appropriate.
- Alert on unusual volumes of new source MAC addresses.

## SecurityX-Style Summary

| Category | Takeaway |
|---|---|
| Attack Type | On-path / man-in-the-middle |
| Technique | ARP spoofing / ARP poisoning |
| Related Layer 2 Attack | MAC flooding |
| Weakness | ARP lacks built-in authentication |
| Impact | Traffic interception, manipulation, or disruption |
| Best Protection | Encryption, segmentation, switch protections, monitoring |
