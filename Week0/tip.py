# Getting the meal prize and the percentage that customer would like to tip weiter
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# Converting meal prize format that customer enterned
def dollars_to_float(d):
    # Converting to float
    d = float(d.replace("$", ""))
    return d

# Converting percentage format that customer enterned
def percent_to_float(p):
    # Converting to float
    pToFloat = float(p.replace("%", ""))
    # برای بدست آوردن درصد باید عددمون رو تقسیم بر صد بکنیم
    p = pToFloat / 100
    return p

main()
