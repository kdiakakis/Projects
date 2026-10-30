# -*- coding: utf-8 -*-
import time
import socket
from concurrent.futures import ThreadPoolExecutor

# ============================================
# TERMINAL OUTPUT HELPERS
# ============================================

class C:
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

def print_banner():
    banner = f"""{C.CYAN}{C.BOLD}
    ██████╗  ██████╗ ██████╗ ████████╗
    ██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝
    ██████╔╝██║   ██║██████╔╝   ██║
    ██╔═══╝ ██║   ██║██╔══██╗   ██║
    ██║     ╚██████╔╝██║  ██║   ██║
    ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝
    S C A N N E R{C.RESET}
    {C.YELLOW}Educational tool - use only on systems you own or have permission to test{C.RESET}
    """
    print(banner)

def print_ok(msg):
    print(f"{C.GREEN}[+]{C.RESET} {msg}")

def print_fail(msg):
    print(f"{C.RED}[-]{C.RESET} {msg}")

def print_info(msg):
    print(f"{C.CYAN}[*]{C.RESET} {msg}")

# ============================================
# FUNCTIONS
# ============================================

def get_ip_web(web):
    try:
        host_ip = socket.gethostbyname(web)
        print_ok(f"IP found: {host_ip} \n")
        return host_ip
    except socket.gaierror:
        print_fail("Failed to resolve the host \n")
        return False


def is_port_open(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.2)
    port_situation = s.connect_ex((ip, port))
    if port_situation == 0:
        s.close()
        return True
    else:
        s.close()
        return False


def scan_ports(ip, start_loop, end_loop):
    def check(port):
        if is_port_open(ip, port):
            return port
        return None

    open_ports = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        results = list(executor.map(check, range(start_loop, end_loop + 1)))
    for i in results:
        if i is not None:
            open_ports.append(i)
    return open_ports

# ============================================
# MAIN
# ============================================

if __name__ == '__main__':
    print_banner()

    target = input('Enter the site you want to scan: ')
    ip = get_ip_web(target)
    if ip != False:
        open_ports = scan_ports(ip, 1, 1023)
        if not open_ports:
            print_info('No open ports found')
        else:
            print_ok(f'Open ports found: {open_ports}')
