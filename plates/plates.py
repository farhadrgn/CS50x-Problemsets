def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check if input contains only alphanumeric letters
    if s.isidentifier():
        # Check if input length is between 2 and 6
        if 2 <= len(s) <= 6:
            # Check if the two first letters is string
            if s[1].isalpha():
                # Check if there is no "_"
                if "_" not in s:
                    # Check if there is no string is middle of number part of plate and the number part won't start with a zero
                    if numberPart(s):
                        return True


def numberPart(x):
    m = []
    # If all letters in user input contains alphabet return True
    if x.isalpha():
        return True

    # Loop over letters
    for j in x:
        #check if the letter is a number and if it was, if will tell index of it
        if j.isdecimal():
            k = x.index(j)
            m.append(k)

    # First number in text
    u = m[0]
    # Number part of the text
    g = x[u:]

    # Check if the fist number is not zero and there is not any string after or middle of numbers
    if x[u] != "0" and g.isdecimal() :
        return True


main()
