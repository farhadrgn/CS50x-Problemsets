def main():
    import inflect

    # Calling inflect engine so we can use join
    p = inflect.engine()
    names = []

    try:
        while True:
            name = input("Name: ")
            names.append(name)
    except EOFError:
        print("")
        pass

    # It will automaticlly put a "," between names and "and" before last entered name
    result = p.join(names)
    print(f"Adieu, adieu, to {result}")


main()
