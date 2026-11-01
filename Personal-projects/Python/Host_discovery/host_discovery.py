import socket
import ipaddress
from concurrent.futures import ThreadPoolExecutor
import subprocess

# ============================================
# FUNCTIONS
# ============================================

def get_local_ip(): #gets your own ip
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    my_ip = s.getsockname()[0]
    s.close()
    return my_ip

def get_network(my_ip): #gets the network ip
    broken_ip = my_ip.split('.')
    broken_ip = broken_ip[0:3]
    net_ip = ".".join(broken_ip)
    net_ip = (f"{net_ip}.0/24")
    return net_ip

def get_hosts(network): #list with all possible ips
    hosts = []
    for h in ipaddress.ip_network(network).hosts():
        hosts.append(str(h))
    return hosts

def poke(ip): #test if the ip responses
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.3)
    s.connect_ex((ip,80))
    s.close()

def poke_all(hosts): #loops 100 at the same time the poke()
    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(poke, hosts)

def read_arp(): #lists all IPS and MACs that responded
    result = subprocess.run(["arp", "-a"], capture_output=True, text=True)
    return result.stdout

def parse_arp(result, prefix): #removes broadcast and 255
    devices = []
    for line in result.splitlines():
        parts = line.split()
        if len(parts) == 3 and parts[0].startswith(prefix) and parts[1] != 'ff-ff-ff-ff-ff-ff':
            devices.append((parts[0], parts[1]))
    return devices

def get_prefix(my_ip): #creates filter for the connected network
    broken_ip = my_ip.split('.')
    broken_ip = broken_ip[0:3]
    prefix = ".".join(broken_ip)
    return prefix + "."



# ============================================
# MAIN
# ============================================

if __name__ == '__main__':
    my_ip = get_local_ip()
    hosts = get_hosts(get_network(my_ip))
    poke_all(hosts)
    print (parse_arp(read_arp(), get_prefix(my_ip)))