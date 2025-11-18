def main():
    # Getting numbers and operation from user
    n1, op, n2 = input("Enter your calculation: ").split()
    n1, n2 = float(n1), float(n2)
    print(calculator(n1, op, n2))

# Calculator
def calculator(x, y, z):
    if (y == "+"):
        result = str(x + z)
        return result
    elif (y == "-"):
        result = str(x - z)
        return result
    elif (y == "*"):
        result = str(x * z)
        return result
    elif (y == "/"):
        if z == 0:
            return "Divided by zero"
        else:
             result = str(x / z)
             return result


main()
