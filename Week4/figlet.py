import sys
import random
from pyfiglet import Figlet


def main():
    # Creating an object of "Figlet()" so we can use it later
    figlet = Figlet()

    # Name of all fonts
    fonts = figlet.getFonts()

    # Random font choice if there was no argument command line input
    if len(sys.argv) == 1:
        random_font = random.choice(fonts)
        figlet.setFont(font=random_font)

    # In case of User picks a font
    elif len(sys.argv) == 3:
        flag = sys.argv[1]
        font_name = sys.argv[2]

        # Check if it start with a "-f" or "--font" and entered a valid font
        if flag in ["-f", "--font"] and font_name in fonts:
            figlet.setFont(font=font_name)
        else:
            sys.exit("Invalid usage")

    # Give an error and exit of program if user input is not right
    else:
        sys.exit("Invalid usage")

    text = input("Input: ")

    # Printing the result
    print("Output:")
    print(figlet.renderText(text))


main()
