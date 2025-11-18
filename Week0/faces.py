# Getting the text from user & printing output
def main():
    Sentence = input("Enter Your Text: ")
    print(convert(Sentence))

def convert(Text):
    """Convert method that replaces faces with emojis"""
    Text = Text.replace(":)", "🙂")
    Text = Text.replace(":(", "🙁")
    return Text

main()
