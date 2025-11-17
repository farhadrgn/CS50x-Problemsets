def main():
    result = int(error_handling())
    if result >= 99:
        print("F")
    elif result <= 1:
        print("E")
    else:
        print(f"{result}%")


def error_handling():
    while True:
        try:
            # Getting the input and seperated by / to two part
            fuel = (input("Enter x/y: ")).split("/")
            x = int(fuel[0])
            y = int(fuel[1])

            # The program should not accept any negative numbers and x can not be bigger than y
            if x < 0 or y < 0 or x > y:
                continue
            return round((x / y * 100))
        except ValueError:
            print("Please enter an integer")
        except ZeroDivisionError:
            print("Divide by zero is not possible")


main()
