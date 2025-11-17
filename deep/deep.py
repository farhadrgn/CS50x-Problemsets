def main():
    # Getting the input from user
    code = input("Enter the code: ").casefold()
    # Printing the result
    print(findCode(code))


def findCode(txt):
    # Finding specified code
    if "42" in txt or "forty-two" in txt or "forty two" in txt:
        return "yes"
    else:
        return "No"


main()
