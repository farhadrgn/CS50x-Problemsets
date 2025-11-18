def main():
    # Getting user file name
    extension = input("Enter your file name: ").strip().casefold()
    print(evaluate(extension))

# Recognizing file extension
def evaluate(txt):
    if txt.endswith(".gif"):
        return "image/gif"
    elif txt.endswith(".jpg") or txt.endswith(".jpeg"):
        return "image/jpeg"
    elif txt.endswith(".png"):
        return "image/png"
    elif txt.endswith(".txt"):
        return "text/plain"
    elif txt.endswith(".pdf"):
        return "application/pdf"
    elif txt.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"


main()
