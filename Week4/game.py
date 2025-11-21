import random


def main():
    # Pick a random number from 1 to number that user entered
    secret_number = random.randint(1, deter_level())
    guess(secret_number)


def deter_level():
    # Getting the number range that user want to guess
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
        except ValueError:
            pass


def guess(i):
    # Let the user guess the random number
    while True:
        try:
            guess = int(input("Guess: "))

            if guess > 0:
                if guess < i:
                    print("Too small!")
                elif guess > i:
                    print("Too large!")
                else:
                    print("Just right!")
                    break
        except ValueError:
            pass


if __name__ == "__main__":
    main()
