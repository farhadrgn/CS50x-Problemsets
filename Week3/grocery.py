def main():

    count = {}

    # Loop over user input items
    for i in getting_input():
        # It will count the repeated time
        if i in count:
            count[i] += 1
        # For items with only one repeat
        else:
            count[i] = 1

    # Sorting items base of alphabet
    sort_items = sorted(count.keys())

    for j in sort_items:
        print(count[j], j)


def getting_input():

    items = []

    # Getting input until user pres ctrl + d
    while True:
        try:
            user_input = input().upper()
            items.append(user_input)
        except EOFError:
            return items


main()
