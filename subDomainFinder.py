import requests
def find_subdomains(domain):
    subdomain_list = []

    # Read all subdomains from the file
    with open("subdomain.txt") as file:
        # Read all content
        content = file.read()
        # Split by new lines to get individual subdomains
        subdomains = content.splitlines()
        subdomain_list.extend(subdomains)

    # A list to store discovered subdomains
    discovered_subdomains = []

    # Iterate over each subdomain and try to access it
    for subdomain in subdomain_list:
        # Construct the URL
        url = f"http://{subdomain}.{domain}"

        try:
            # Attempt to connect to the URL
            response = requests.get(url)
            
        except requests.ConnectionError:
            # If the subdomain does not exist, move to the next one
            pass
        
        else:
            # If the subdomain exists, print it and add it to the discovered_subdomains list
            print("[+] Discovered subdomain:", url)
            discovered_subdomains.append(url)

    # Print the list of discovered subdomains
    # print(f'Discovered subdomains: {discovered_subdomains}')

    # Save the discovered subdomains into a file
    with open("discovered_subdomains.txt", "w") as f:
        for subdomain in discovered_subdomains:
            print(subdomain, file=f)

    return discovered_subdomains