# Validation Notes – Chapter 1

## OPNsense Interface Assignment

OPNsense initially showed no assigned interfaces after installation. Interfaces were assigned manually:

| Interface | Role |
|---|---|
| em0 | WAN |
| em1 | LAN |

After assignment, OPNsense showed:

```text
LAN (em1) -> 192.168.1.1/24
WAN (em0) -> DHCP address
```

## Kali DHCP Validation

Kali initially had only an IPv6 link-local address and no IPv4 address.

NetworkManager was used instead of dhclient because dhclient was not installed:

```bash
nmcli device status
sudo nmcli device connect eth0
ip addr
```

Confirmed Kali IPv4 address:

```text
192.168.1.188/24
```

## Discovery Test

From Kali:

```bash
sudo netdiscover -i eth0 -r 192.168.1.0/24
```

Discovered hosts:

```text
192.168.1.1      OPNsense LAN gateway
192.168.1.121    Metasploitable 2
```

## Web Reachability Test

From Kali browser:

```text
http://192.168.1.121
```

Result:

Metasploitable web page loaded successfully.

## Result

Chapter 1 internal lab networking is validated.
