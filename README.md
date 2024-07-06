requirement is
pip install dnspython python-whois requests
Description is
This script gathers information about a domain by:

Resolving the domain's IP address using the socket library.
Fetching DNS records (A, MX, NS, TXT) using the dnspython library.
Retrieving WHOIS information using the whois library.
Obtaining server details based on the IP address using the ip-api.com API with the requests library.
