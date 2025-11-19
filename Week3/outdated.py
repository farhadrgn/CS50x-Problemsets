def main():
    # Getting year, month and day
    year, month, day = date_val()
    print(f"{year:04}-{month:02}-{day:02}")


def date_val():
    while True:
        date = input("Enter your date: ")

        # First date format
        if "/" in date:
            try:
                # split month, day and year by "/"
                month, day, year = date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)

                if 1 <= month <= 12 and 1 <= day <= 31:
                    return year, month, day
            except:
                pass

        # Second date format
        else:
            try:
                # Split month name part and number part of the date
                month_name, rest = date.split(" ", 1)
                day, year = rest.split(",")
                day = int(day)
                year = int(year.strip())

                # Check if the entered month name is valid or not
                if month_name in months():
                    # Calculating the number order of month in year
                    month = months().index(month_name) + 1

                    if 1 <= day <= 31:
                        return year, month, day
            except:
                pass
        # If the input was out of format ask for input again
        continue


# Months names
def months():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    return months


main()
