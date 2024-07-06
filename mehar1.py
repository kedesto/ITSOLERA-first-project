import socket
import dns.resolver
import whois
import requests

def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except Exception as e:
        return str(e)

def get_dns_records(domain):
    records = {}
    try:
        answers = dns.resolver.resolve(domain, 'A')
        records['A'] = [answer.to_text() for answer in answers]
    except Exception as e:
        records['A'] = str(e)

    try:
        answers = dns.resolver.resolve(domain, 'MX')
        records['MX'] = [answer.to_text() for answer in answers]
    except Exception as e:
        records['MX'] = str(e)

    try:
        answers = dns.resolver.resolve(domain, 'NS')
        records['NS'] = [answer.to_text() for answer in answers]
    except Exception as e:
        records['NS'] = str(e)

    try:
        answers = dns.resolver.resolve(domain, 'TXT')
        records['TXT'] = [answer.to_text() for answer in answers]
    except Exception as e:
        records['TXT'] = str(e)
        
    return records

def get_whois_info(domain):
    try:
        whois_info = whois.whois(domain)
        return whois_info
    except Exception as e:
        return str(e)

def get_server_details(ip_address):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        return response.json()
    except Exception as e:
        return str(e)

def gather_domain_info(domain):
    domain_info = {}

    print(f"Gathering information for domain: {domain}")

    # Get IP address
    ip_address = get_ip_address(domain)
    domain_info['IP Address'] = ip_address
    print(f"IP Address: {ip_address}")

    # Get DNS records
    dns_records = get_dns_records(domain)
    domain_info['DNS Records'] = dns_records
    print(f"DNS Records: {dns_records}")

    # Get WHOIS information
    whois_info = get_whois_info(domain)
    domain_info['WHOIS Information'] = whois_info
    print(f"WHOIS Information: {whois_info}")

    # Get server details
    server_details = get_server_details(ip_address)
    domain_info['Server Details'] = server_details
    print(f"Server Details: {server_details}")

    return domain_info

# Example usage
if __name__ == "__main__":
    domain = input("Enter a domain: ")
    domain_info = gather_domain_info(domain)
    print("\nDomain Information:")
    for key, value in domain_info.items():
        print(f"{key}: {value}")
