

import whois
from domain_validator import *
def get_whois_info(domain_name):
    if is_registered(domain_name):
        whois_info = whois.whois(domain_name)
        
        # print the registrar
        print("Domain registrar:", whois_info.registrar)

        # print the WHOIS server
        print("WHOIS server:", whois_info.whois_server)

        # get the creation time
        print("Domain creation date:", whois_info.creation_date)

        # get expiration date
        print("Expiration date:", whois_info.expiration_date)

        # # print all other info
        # print("======Printing the all info=========")
        # print(whois_info)
        
    else:
        print("The domain", domain_name, "is not registered.")