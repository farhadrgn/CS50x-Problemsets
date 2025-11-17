def main():
    temp = 0
    while temp < 50:
        coin = int(input("Insert Coin: "))

        # If user input was 5 or 10 or 25, machine will accept the money
        if coin == 5 or coin == 10 or coin == 25:
            temp = temp + coin

            # Until user did not payed 50, print his amount of due
            if temp < 50:
                print("Amount Due:", 50 - temp)
            # If user payed more than his due, print amount of change owed
            elif temp > 50:
                print("Change Owed:", temp - 50)
            # If user payed 50, print that he dose not have any due
            elif 50 - temp == 0:
                print("Change Owed: 0")
                
        # If user insert any coin ather than defined coins, don't accept the coin and print his amount of due
        elif 50 - temp > 0:
            print("Amount Due:", 50 - temp)



main()
