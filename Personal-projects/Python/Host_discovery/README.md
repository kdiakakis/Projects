# Host Discovery

A small Python tool that finds the devices connected to your local network and lists their IP and MAC addresses. It uses only the Python standard library and needs **no administrator rights**.

> **Legal notice:** this tool is for education and for networks **you own or have written permission to test**. Don't run it on networks that aren't yours (school, cafe, hotel, a neighbour's WiFi), even if you know the password. You are responsible for how you use it.

## Usage

```
python host_discovery.py
```

Example output:

```
[('192.168.1.1', 'aa-bb-cc-dd-ee-ff'), ('192.168.1.15', '11-22-33-44-55-66')]
```

Each pair is `(IP address, MAC address)` for one device.

## How it works

1. **Find your own IP** (`get_local_ip`): opens a UDP socket towards `8.8.8.8` and reads which local address the operating system chose. Nothing is actually sent.
2. **Work out the network** (`get_network`): turns `192.168.1.23` into `192.168.1.0/24`.
3. **List every address** (`get_hosts`): builds the 254 possible addresses from `.1` to `.254`.
4. **Wake up the ARP table** (`poke`, `poke_all`): tries to connect to each address on port 80, 100 at a time using threads. The result of the connection doesn't matter. The attempt makes the operating system ask the network "who has this IP?" (ARP), and every real device answers, even if it has a firewall.
5. **Read the answers** (`read_arp`): runs `arp -a` and gets the operating system's ARP table.
6. **Clean the list** (`parse_arp`, `get_prefix`): keeps only entries from your own network and removes the broadcast address.

## Why ARP and not ping?

Many devices ignore ping or block it with a firewall. ARP can't be blocked on a local network, because devices need it to communicate at all, so it finds more devices.

## Requirements

- Python 3.7 or newer
- Windows (the parser is written for the Windows `arp -a` output)
- Connected to the network you want to scan

## Limitations

- Linux and macOS print `arp -a` in a different format, so `parse_arp` would need changes.
- Assumes a `/24` network (like `192.168.1.x`), the most common home setup.
- Devices that are asleep may not appear until they wake up.
- Phones using a private/random MAC address show a different MAC per network, so the manufacturer can't be identified from it.
- Only finds devices on your own network segment.

## Planned

- Show the manufacturer from the MAC address
- Print the results as a formatted table
- Port scan each device found
- Save results to a file
