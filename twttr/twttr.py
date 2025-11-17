def main():
    txt = input("Enter yor text: ")
    # Defining a variable containing vowels
    vowels = "aAeEiIoOuU"

    # Makink a loop over the vowels
    for vowel in vowels:

        # Detecting if there is a vowel in user text
        if vowel in txt:
            # Removing vowel from text
            txt = txt.replace(vowel, "")
    print(txt)

main()
