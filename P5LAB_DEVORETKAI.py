#TKAI DEVORE
#5MAY24
#P5LAB
#CHANGE

import random

def disperse_change(change_owed):
    dollars = int(change_owed)
    change_owed -= dollars
    quarters = int(change_owed / 0.25)
    change_owed -= quarters * 0.25
    dimes = int(change_owed / 0.10)
    change_owed -= dimes * 0.10
    nickels = int(change_owed / 0.05)
    change_owed -= nickels * 0.05
    pennies = round(change_owed / 0.01)
    
    print("Change breakdown:")
    print("Dollars:", dollars)
    print("Quarters:", quarters)
    print("Dimes:", dimes)
    print("Nickels:", nickels)
    print("Pennies:", pennies)

def main():
    # Generate a random float value as the amount owed
    amount_owed = round(random.uniform(1.0, 100.0), 2)
    print("Amount owed: $", amount_owed)
    
    # Prompt the user to enter the amount of cash they will put into the self-checkout
    amount_paid = float(input("Enter the amount of cash you will put into the self-checkout: $"))
    
    # Calculate the amount of change owed to the customer
    change_owed = amount_paid - amount_owed
    
    if change_owed < 0:
        print("Not enough cash provided. Please try again.")
    else:
        print("Change owed: $", round(change_owed, 2))
        disperse_change(change_owed)

if __name__ == "__main__":
    main()
