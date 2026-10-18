# Port Scanner

A simple multithreaded TCP port scanner written in Python. It resolves a hostname to an IP address and checks which ports in the range 1-1023 (the "well-known" ports) are open.

> **Disclaimer:** This is an educational tool. Only scan systems that you own or have explicit permission to test. Scanning other people's systems without permission may be illegal.

## Features

- Resolves a domain name to an IP address (or put the ip you want)
- Scans ports 1-1023 using 100 threads for speed
- Colored terminal output
- No external dependencies (standard library only)

## Requirements

- Python 3.6+

## Usage

```bash
python port_scanner.py
```

Then enter the host you want to scan when prompted:

```
Enter the site you want to scan: scanme.nmap.org
```

`scanme.nmap.org` is a host the Nmap project provides specifically for testing scanners.

### Example output

```
[+] IP found: 45.33.32.156

[+] Open ports found: [22, 80]
```

## How it works

1. `get_ip_web()` resolves the hostname with `socket.gethostbyname()`.
2. `is_port_open()` tries a TCP connection to a port using `socket.connect_ex()` with a 0.2 second timeout. A return value of `0` means the port is open.
3. `scan_ports()` runs the check for every port in the range using a `ThreadPoolExecutor` with 100 workers.

## Configuration

To scan a different range, change the arguments in the last lines of `port_scanner.py`:

```python
open_ports = scan_ports(ip, 1, 1023)
```

To make the scan more reliable on slow connections, increase the timeout in `is_port_open()`:

```python
s.settimeout(0.2)
```

## Limitations

- Only scans TCP ports (no UDP)
- Uses a full TCP connect scan, which is easy to detect and may be logged by the target
- Only IPv4 is supported
