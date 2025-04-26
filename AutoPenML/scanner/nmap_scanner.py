import nmap

def run_nmap_scan(target_ip):
    nm = nmap.PortScanner()
    print(f"[+] Scanning target: {target_ip}")
    nm.scan(hosts=target_ip, arguments='-sV -O')
    return nm[target_ip]