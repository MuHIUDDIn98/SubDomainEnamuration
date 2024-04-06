import dns.resolver

def recorded_data(target_domain):
    record_types = [ "A" , "AAAA" , "CNAME" , "MX" , "NS" ,
    "SOA" , "TXT" ]
    resolver = dns . resolver . Resolver ()
    
    for record_type in record_types :
        # Perform DNS lookup for the target domain and record type
        try :

            answers = resolver . resolve ( target_domain , record_type )

        except dns . resolver . NoAnswer :

            continue
        
        # Print the DNS records found
        print (f'DNS records for { target_domain } ( { record_type }):' )
        for rdata in answers :
            print ( rdata )

    
    return answers
                
    