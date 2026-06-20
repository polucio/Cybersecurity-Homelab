# Troubleshooting Notes – Chapter 2

## Issue: arpspoof Was Run on Metasploitable

### Symptom

```text
The program 'arpspoof' is currently not installed.
```

### Cause

`arpspoof` was run on the victim machine instead of the attacker machine.

### Fix

Run `arpspoof` from Kali, not Metasploitable.

## Issue: arpspoof Permission Error

### Symptom

```text
arpspoof: libnet_open_link(): UID/EUID 0 or capability CAP_NET_RAW required
```

### Fix

Run with `sudo`.

## Issue: urlsnarf Permission Error

### Symptom

```text
urlsnarf: eth0: You don't have permission to perform this capture on that device
Attempt to create packet socket failed - CAP_NET_RAW may be required
```

### Fix

Run:

```bash
sudo urlsnarf -i eth0
```

## Issue: Metasploitable DNS Failure

### Symptom

```text
Resolving www.google.com... failed: Name or service not known.
Resolving example.com... failed: Name or service not known.
```

### Fix

Generate HTTP traffic by IP address instead:

```bash
wget http://192.168.1.1
```

## Issue: OPNsense Redirected HTTP to HTTPS

### Symptom

```text
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://192.168.1.1/
```

### Meaning

This was not a failure. The initial HTTP request worked and then the gateway redirected the client to HTTPS.

## Issue: Old TLS / SSL Failure on Metasploitable

### Symptom

```text
OpenSSL: error:... tlsv1 alert protocol version
Unable to establish SSL connection.
```

### Meaning

This did not invalidate the lab. The relevant HTTP request occurred before the HTTPS redirect failed.

## Issue: wget Did Not Support --max-redirect

### Symptom

```text
wget: unrecognized option `--max-redirect=0'
```

### Cause

Metasploitable uses an older version of `wget`.

### Fix

Use:

```bash
wget http://192.168.1.1
```

## Issue: urlsnarf Did Not Show Output at First

### Symptom

`urlsnarf` entered listening mode but initially did not display the expected book output.

### Workaround

Use `tcpdump` to verify traffic visibility.

## Issue: Scapy ARP Warning

### Symptom

```text
WARNING: You should be providing the Ethernet destination MAC address when sending an is-at ARP.
```

### Cause

The first Python script used `send()` with only an ARP packet.

### Fix

Use an Ethernet frame with `sendp()`.

## Issue: tcpdump MAC Flooding Filter Error

### Symptom

```text
tcpdump: link layer applied in wrong context
```

### Cause

The command used an invalid filter:

```bash
sudo tcpdump -i eth0 ether
```

### Fix

Use:

```bash
sudo tcpdump -i eth0 -e -n
```

## Lesson

Tool output may differ from the book due to software versions, redirects, TLS behavior, Scapy behavior, or lab differences. Validation can still be completed by confirming the underlying network traffic with lower-level tools like `tcpdump`.
