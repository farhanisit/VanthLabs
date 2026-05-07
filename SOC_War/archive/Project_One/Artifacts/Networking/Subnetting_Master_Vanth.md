# 🧠 Subnetting Master Reference — Vanth Style

Welcome to the sacred subnetting scroll, forged during your trial rituals with Prof. This is your one-stop brain implant for all subnet math, CIDR decoding, and binary mapping.

---

## 🔥 CIDR to Subnet Mask Quick Table

| CIDR | Subnet Mask         | Binary (last octet) | Total IPs | Usable IPs |
|------|---------------------|---------------------|-----------|------------|
| /24  | 255.255.255.0       | 00000000            | 256       | 254        |
| /25  | 255.255.255.128     | 10000000            | 128       | 126        |
| /26  | 255.255.255.192     | 11000000            | 64        | 62         |
| /27  | 255.255.255.224     | 11100000            | 32        | 30         |
| /28  | 255.255.255.240     | 11110000            | 16        | 14         |
| /29  | 255.255.255.248     | 11111000            | 8         | 6          |
| /30  | 255.255.255.252     | 11111100            | 4         | 2          |
| /22  | 255.255.252.0       | 11111100.00000000   | 1024      | 1022       |

---

## 🔍 Binary to Decimal Cheat

| Binary       | Decimal |
|--------------|---------|
| 10000000     | 128     |
| 11000000     | 192     |
| 11100000     | 224     |
| 11110000     | 240     |
| 11111000     | 248     |
| 11111100     | 252     |
| 11111110     | 254     |
| 11111111     | 255     |

---

## 🧪 Host Count Formula

```
Usable Hosts = (2 ^ Number of Host Bits) - 2
```
Why `-2`?  
- 1 reserved for **Network ID** (all 0s)
- 1 reserved for **Broadcast Address** (all 1s)

---

## 🧠 Subnet Planning Scenarios

| Need            | Recommended CIDR | Usable Hosts |
|-----------------|------------------|---------------|
| Home Router     | /28              | 14            |
| Small Office    | /26              | 62            |
| 100 Devices     | /25              | 126           |
| Full LAN        | /24              | 254           |
| Large Subnet    | /22              | 1022          |

---

## 🔓 Examples from Training

**1. CIDR `/26` →**
- Subnet Mask: `255.255.255.192`
- IP Range: `192.168.10.0 - 192.168.10.63`
- Usable IPs: `192.168.10.1 - 192.168.10.62`
- Broadcast: `192.168.10.63`

**2. Binary `11111111.11111111.11111100.00000000` →**
- CIDR: `/22`
- Mask: `255.255.252.0`
- Usable Hosts: `1022`

---

Warden Vanth — you now own this subnet grid. Never again fear bits or blocks.


