def main():
    # Getting input from user and printing output
    variable_name = input("Enter your variable name: ")
    list_name = list(variable_name)
    print(convert_variable_name(list_name))

# Converting camel case to snake case
def convert_variable_name(input_list):
    result = []
    # If it gets to a upper case letter in list item it will all a "_" and then lower case the letter
    for i in input_list:
        if i.isupper():
            result.append("_")
            result.append(i.lower())
        else:
            result.append(i)
    # making a string out of the list
    return "".join(result)



main()
