#Tkai DeVore
#21APR
#PLAB3
#If/Else Statments


def calculate_change(amount):
    dollars = int(amount)
    cents = round((amount - dollars) * 100)
    
    quarters = cents // 25
    cents %= 25
    
    dimes = cents // 10
    cents %= 10
    
    nickels = cents // 5
    cents %= 5
    
    pennies = cents
    
    change = []
    
    if dollars:
        change.append(f"{dollars} {'dollar' if dollars == 1 else 'dollars'}")
    if quarters:
        change.append(f"{quarters} {'quarter' if quarters == 1 else 'quarters'}")
    if dimes:
        change.append(f"{dimes} {'dime' if dimes == 1 else 'dimes'}")
    if nickels:
        change.append(f"{nickels} {'nickel' if nickels == 1 else 'nickels'}")
    if pennies:
        change.append(f"{pennies} {'penny' if pennies == 1 else 'pennies'}")
    
    return ', '.join(change)

if __name__ == "__main__":
    while True:
        try:
            amount = float(input("Enter the amount of money: "))
            if amount < 0:
                print("Please enter a non-negative amount.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    print(calculate_change(amount))
