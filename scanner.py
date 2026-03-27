import nmap

def run_scan(target):
    scanner = nmap.PortScanner()
    print(f"[*] Starting scan on {target} ...")
    print("[*] This may take 1-2 minutes, please wait...")
    
    scanner.scan(hosts=target, arguments='-sV')
    
    results = []

    for host in scanner.all_hosts():
        host_info = {
            "ip": host,
            "hostname": scanner[host].hostname(),
            "state": scanner[host].state(),
            "open_ports": []
        }

        for proto in scanner[host].all_protocols():
            ports = scanner[host][proto].keys()
            for port in ports:
                service = scanner[host][proto][port]
                if service['state'] == 'open':
                    host_info["open_ports"].append({
                        "port": port,
                        "protocol": proto,
                        "service": service.get('name', 'unknown'),
                        "version": service.get('version', ''),
                        "product": service.get('product', '')
                    })

        results.append(host_info)

    return results