#DeVore, Tkai
#7APR24
#P1HW2
#Budget



# Get the user's budget
budget = int(input("Enter your budget: $"))

# Get the travel destination from the user
destination = input("Enter your travel destination: ")

# Get the amount the user will spend on gas
gas_expense = int(input("Enter the amount you will spend on gas: $"))

# Get the amount the user will spend on accommodation
accommodation_expense = int(input("Enter the amount you will spend on accommodation: $"))

# Get the amount the user will spend on food
food_expense = int(input("Enter the amount you will spend on food: $"))

# Add up all the expenses
total_expenses = gas_expense + accommodation_expense + food_expense

# Subtract expenses from the budget
remaining_budget = budget - total_expenses# Display the results

#Display the results
print("\nTravel Expenses:")
print(f"Initial Budget: ${budget:.2f}")
print(f"Destination: {destination}")
print(f"Fuel Amount: ${gas_expense:.2f}")
print(f"Accommodation Amount: ${accommodation_expense:.2f}")
print(f"Food Amount: ${food_expense:.2f}")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Budget: ${remaining_budget:.2f}")
