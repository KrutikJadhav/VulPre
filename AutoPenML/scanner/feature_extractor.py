def extract_features(nmap_scan_data):
    ports = []
    if 'tcp' in nmap_scan_data:
        ports = [port for port in nmap_scan_data['tcp'].keys()]

    os_guess = "Unknown"
    if 'osmatch' in nmap_scan_data and nmap_scan_data['osmatch']:
        os_guess = nmap_scan_data['osmatch'][0]['name']

    features = {
        "open_ports_count": len(ports),
        "common_ports_open": int(80 in ports or 443 in ports or 22 in ports),
        "os_type": os_guess
    }
    return features