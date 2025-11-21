import emoji


def main():
    user_input = input("Input: ")

    # Converting user input to emoji via emojize mothode from emoji library
    output = emoji.emojize(user_input, language="alias")
    print(output)


main()
