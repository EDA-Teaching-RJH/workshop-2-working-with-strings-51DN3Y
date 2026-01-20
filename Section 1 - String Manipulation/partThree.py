def main():
    pounds = pounds_to_float(input("How much was the meal? £"))
    percent = percent_to_float(input("What percentage would you like to charge? "))
    charge = float(pounds * percent)
    print(f"Charge £{charge:.2f}")


def pounds_to_float(d):
    return float(d)

def percent_to_float(p):
    return float(p)/100 

main()
