def main():
    # Getting user greeting
    greeting = input("Enter your greeting: ").strip().casefold()
    print(valuation(greeting))


def valuation(input):
    # If the greeting starts with "hello", the user will receive $0
    if input.startswith("hello"):
        return "$0"
    # If the greeting starts with "h", the user will receive $20
    elif input.startswith("h"):
        return "$20"
    # If the greeting starts with anyting else, the user will receive $100
    else:
        return "$100"


main()
