import requests
import sys
import os

# Use link for endpoint information.
# https://docs.coingecko.com/v3.0.1/reference/endpoint-overview
# Requests Manual: https://requests.readthedocs.io/en/latest/

def get_bitcoin_data():

    url = "https://api.coingecko.com/api/v3/simple/price"

    # Parameters for the request
    params = {
        "ids": "bitcoin",  # Add the cryptocurrency ID(s) you want to fetch
        "vs_currencies": "usd"  # Specify the currency to get the price in
    }

    headers = {
        "accept": "application/json",
        "x-cg-demo-api-key": "CG-unzV2e5tfpB4bhmLgzExK7Gu"
    }

    response = requests.get(url, headers=headers, params=params)

    print(response.text)



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

def print_menu():
    print("Please select an option from below: ")
    print("1. Ping CoinGecko Server.")
    print("2. Check BitCoin Price")
    

def main():
    print(ping())
    get_bitcoin_data()
    print_menu()
    choice = input("Choice: ")
    if choice == 1:
        print(ping())
    elif choice == 2:
        get_bitcoin_data()
    

if __name__ == "__main__":
    main()