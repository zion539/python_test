import requests

def check_proxy_and_access_website(proxy_file, website_url):
    with open(proxy_file, 'r') as file:
        proxies = file.readlines()

    valid_proxies = []

    for proxy in proxies:
        proxy = proxy.strip()
        proxies_dict = {
            'http': f'http://{proxy}',
            'https': f'https://{proxy}'
        }

        try:
            response = requests.get(website_url, proxies=proxies_dict, timeout=5)
            if response.status_code == 200:
                valid_proxies.append(proxy)
                print(f"Proxy {proxy} is functional.")
                # Access the website via the proxy
                website_response = requests.get(website_url, proxies=proxies_dict, timeout=5)
                if website_response.status_code == 200:
                    print(f"Accessing {website_url} via proxy {proxy} successful.")
                else:
                    print(f"Failed to access {website_url} via proxy {proxy}.")
            else:
                print(f"Proxy {proxy} is not functional.")
        except:
            print(f"Proxy {proxy} is not functional.")

    return valid_proxies

# Example usage
proxy_file = r'C:\Users\Zion5\PycharmProjects\python_test\dop\proxy.txt'  # Replace with the actual file path
website_url = 'https://2ip.ru/'  # Replace with the website URL you want to access
valid_proxies = check_proxy_and_access_website(proxy_file, website_url)
print("Valid Proxies:")
print(valid_proxies)
