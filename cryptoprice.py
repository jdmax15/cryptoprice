import requests
import sys
import os

# Use link for endpoint information.
# https://docs.coingecko.com/v3.0.1/reference/endpoint-overview 

def get_data():
    api_key = "CG-unzV2e5tfpB4bhmLgzExK7Gu"
    url = "https://api.coingecko.com/api/v3/"
    # TO DO: Finish this

# Pings CoinGecko, will respond "To the Moon!" if successfull.
def ping():
    api_header = "?x_cg_demo_api_key="
    key = "CG-unzV2e5tfpB4bhmLgzExK7Gu"
    url = f"https://api.coingecko.com/api/v3/ping{api_header}{key}"
        
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        sys.exit("Cannot connect to CoinGecko Server")
    

def main():
    print(ping())

if __name__ == "__main__":
    main()