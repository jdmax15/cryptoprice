import requests
import sys
import os

# Use link for endpoint information.
# https://docs.coingecko.com/v3.0.1/reference/endpoint-overview
# Requests Manual: https://requests.readthedocs.io/en/latest/

def get_bitcoin_data():
    while True:    
        try:
            coin = input("What coin to get? ").lower()
            currency = "aud"

            url = "https://api.coingecko.com/api/v3/simple/price"

            # Parameters for the request
            params = {
                "ids": f"{coin}",  # Add the cryptocurrency ID(s) you want to fetch
                "vs_currencies": f"{currency}"  # Specify the currency to get the price in
            }

            headers = {
                "accept": "application/json",
                "x-cg-demo-api-key": "CG-unzV2e5tfpB4bhmLgzExK7Gu"
            }

            response = requests.get(url, headers=headers, params=params)

            if response.status_code == 200:
                data = response.json()
                if coin in data and currency in data[coin]:
                    return f"The currenct price of {coin.upper()} in {currency.upper()} is ${data[coin][currency]}."
                else:
                    print("Invalid coin or curerncy. Please try again.")
            else:
                print("Error fetching data. Please try again.")
        except Exception as e:
            print(f"{e}: Can't find coin")

def get_historical_price():

    url = "https://api.coingecko.com/api/v3/coins/bitcoin/history?date=30-12-2023"

    headers = {
        "accept": "application/json",
        "x-cg-demo-api-key": "CG-unzV2e5tfpB4bhmLgzExK7Gu"
    }

    response = requests.get(url, headers=headers)

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
    print_menu()
    choice = int(input("Choice: "))
    if choice == 1:
        print(ping())
    elif choice == 2:
        print(get_bitcoin_data())
    elif choice == 3:
        get_historical_price()

if __name__ == "__main__":
    main()