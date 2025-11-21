import random


def main():
    # Getting level of game from user
    level = get_level()

    score = 0

    # A loop for creating 10 math problems
    for _ in range(10):
        # Generating random numbers
        x = generate_integer(level)
        y = generate_integer(level)

        answer = x + y
        solved = False

        # Giving three chance to user to answer correctly
        for _ in range(3):
            try:
                # Asking the question
                user_input = input(f"{x} + {y} = ")
                user_answer = int(user_input)

                if user_answer == answer:
                    score += 1
                    solved = True
                    break
                else:
                    # If user was not correct
                    print("EEE")
            except ValueError:
                # If user entered anything other than answer
                print("EEE")

        # If user answer is not correct for 3 time, it will show the answer
        if not solved:
            print(f"{x} + {y} = {answer}")

    print(f"Score: {score}")


def get_level():
    """Getting a level from user and if is not 1,2 or 3 it will ask again"""

    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:
                return n
        except ValueError:
            pass


def generate_integer(l):
    """It will return a positive random number in range of inputed level"""

    if l == 1:
        # One digit number
        return random.randint(0, 9)
    elif l == 2:
        # Two digit number
        return random.randint(10, 99)
    elif l == 3:
        # Three digit number
        return random.randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()
