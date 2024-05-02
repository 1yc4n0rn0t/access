import socket

def scan_ports(hostname):
    open_ports = []
    ports_to_scan = [21, 22, 80, 443]  # Add more ports if needed
    
    for port in ports_to_scan:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)  # Timeout for connection
            s.connect((hostname, port))
            open_ports.append(port)
            s.close()
        except:
            pass
    
    return open_ports

if __name__ == "__main__":
    domain = input("Enter the domain name or IP address to scan: ")
    open_ports = scan_ports(domain)
    
    if open_ports:
        print(f"The following ports are open on {domain}: {', '.join(map(str, open_ports))}")
    else:
        print("No open ports found.")
