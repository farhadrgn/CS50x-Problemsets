def main():

    inText = input("Enter the time: ")

    # Recongizing the format that user insert
    if "a.m." in inText or "p.m." in inText:
        time, format = inText.split(" ")
    else:
        time = inText
        format = None


    # Recognizing breakfast time whether in 12 hour format or 24 hour format
    match format:
        case "a.m." | "" if 7<= convert(time) <= 8:
            print("breakfast time")
        case None if 12 <= convert(time) <= 13:
            print("lunch time")
        case None if 18 <= convert(time) <= 19:
            print("dinner time")
        case "p.m." if 0 <= convert(time) <= 1:
            print("lunch time")
        case "p.m." if 6 <= convert(time) <= 7:
            print("dinner time")
        case _:
            print(None)


# Convert hour format to float
def convert(inp):
    hour, minute = inp.split(":")
    return float(hour) + float(minute) / 60


if __name__ == "__main__":
    main()
