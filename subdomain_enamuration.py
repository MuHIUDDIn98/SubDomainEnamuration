import argparse
from domain_validator import *
from subDomainFinder import *
from who_is import *


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Domain Information Tool')
    parser.add_argument('domain', type=str, help='Domain name to analyze')
    args = parser.parse_args()
    domain_name = args.domain
    
    
    if is_registered(domain_name):
        #Print WHOIS information if the domain is registered
        get_whois_info(domain_name)
        # Find and print subdomains
        subdomains = find_subdomains(domain_name)
        print(subdomains)
    else:
        print("not regesterd")
    

    
