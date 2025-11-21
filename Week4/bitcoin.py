import sys
import requests


def main():

    # Check for if ther is only 1 input, not less and not more
    if len(sys.argv) != 2:
        print("Please enter number of bitcoin price you want")
        sys.exit(1)

    # Converting user input to float
    try:
        amount = float(sys.argv[1])
    except ValueError:
        print("Input is not a number")
        sys.exit(1)

    # Getting bitcoin price data from capcoin API
    try:
        url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=Your_API_Key"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        sys.exit("Request error")

    # Converting JSON to python format
    data = response.json()
    price = float(data["data"]["priceUsd"])

    # Calculate number of bitcoin that user wants it's price
    total = amount * price
    print(f"${total:,.4f}")


main()
