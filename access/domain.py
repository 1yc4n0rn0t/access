# Python 

import socket

def get_ip_address(domain_name):
    try:
        ip_address = socket.gethostbyname(domain_name)
        return ip_address
    except socket.gaierror:
        return "Could not resolve domain name"

# Input domain name
domain_name = input("Enter domain name: ")

# Get IP address
ip_address = get_ip_address(domain_name)

print(f"The IP address of {domain_name} is {ip_address}")
