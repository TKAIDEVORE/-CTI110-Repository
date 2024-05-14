# Tkai DeVore
# 14APR24
# P2LAB2
# Dicitionary Keys

def main():
    # Create the dictionary
    mpg_dict = {
        "Camaro": 18.21,
        "Prius": 52.36,
        "Model S": 110,
        "Silverado": 26
    }

    # Print all the keys in the dictionary
    print("Available vehicles:", *mpg_dict.keys(), sep=", ")

    # Prompt the user to enter a vehicle
    chosen_vehicle = input("Enter a vehicle from the list: ")

    # Check if the entered vehicle exists in the dictionary
    if chosen_vehicle in mpg_dict:
        # Display the MPG for the chosen vehicle
        print(f"MPG for {chosen_vehicle}: {mpg_dict[chosen_vehicle]}")

        # Prompt the user to enter the number of miles
        miles = float(input("Enter the number of miles you will drive the vehicle: "))

        # Calculate gallons of gas needed
        gallons_needed = miles / mpg_dict[chosen_vehicle]

        # Display the gallons of gas needed
        print(f"Gallons of gas needed: {gallons_needed:.2f}")
    else:
        print("Invalid vehicle entered. Please choose from the list.")

if __name__ == "__main__":
    main()
