# Network Diagram – Chapter 1

## Logical Design

```text
                 Home Network / Internet
                         |
                         |
              [OPNsense Adapter 1]
                Bridged Adapter / WAN
                         |
                    OPNsense
                 LAN: 192.168.1.1
              [OPNsense Adapter 2]
              Internal Network: Internal LAN
                         |
        ------------------------------------------------
        |                       |                      |
      Kali                Metasploitable             Ubuntu
  192.168.1.188           192.168.1.121          DHCP / later use
```

## Security Boundary

The OPNsense VM is the boundary between the real network and the lab network.

The vulnerable machines stay behind OPNsense on the VirtualBox internal network.

## VirtualBox Network Rules

| VM | Bridged Adapter | Internal Network |
|---|---:|---:|
| OPNsense | Yes, WAN only | Yes, LAN only |
| Kali | No | Yes |
| Metasploitable | No | Yes |
| Ubuntu | No | Yes |
