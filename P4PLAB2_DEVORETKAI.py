#TKAI DEVORE
#28APR24
#P4LAB2
#Multiplication Table

def display_multiplication_table(number):
    print(f"Multiplication table for {number}:")
    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}")

def main():
    while True:
        user_input = input("Enter an integer (or type 'no' to leave program): ")

        if user_input.lower() == 'no':
            print("Exiting the program.")
            break

        try:
            number = int(user_input)
            if number < 0:
                print("Sorry, the program cannot accept negative values.")
            else:
                display_multiplication_table(number)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
if __name__ == "__main__":
    main()
