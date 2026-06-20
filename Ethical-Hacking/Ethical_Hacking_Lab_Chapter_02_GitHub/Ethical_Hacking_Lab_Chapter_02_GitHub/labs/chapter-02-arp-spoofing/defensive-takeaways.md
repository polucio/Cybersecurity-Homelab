# Defensive Takeaways – Chapter 2

## Main Lesson

ARP spoofing can allow an attacker on the same local network to position themselves between a victim and a gateway.

Once on-path, the attacker may be able to observe or manipulate unencrypted traffic.

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

## SecurityX-Style Summary

| Category | Takeaway |
|---|---|
| Attack Type | On-path / man-in-the-middle |
| Technique | ARP spoofing / ARP poisoning |
| Weakness | ARP lacks built-in authentication |
| Impact | Traffic interception or manipulation |
| Best Protection | Encryption, segmentation, switch protections, monitoring |
