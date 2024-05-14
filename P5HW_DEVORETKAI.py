#TKAI DEVORE
#5MAY24
#P5HW
#MATH QUIZ


import random

def generate_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return num1, num2

def add_numbers(num1, num2):
    return num1 + num2

def subtract_numbers(num1, num2):
    return num1 - num2

def math_quiz():
    guesses = 0
    while True:
        print("\nMENU:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Quit")
        choice = input("Enter your choice (1, 2, or 3): ")
        
        if choice == "1":
            num1, num2 = generate_numbers()
            result = add_numbers(num1, num2)
            guess = int(input(f"What is the sum of {num1} and {num2}? "))
            guesses += 1
            while guess != result:
                if guess < result:
                    print("Too low. Try again.")
                else:
                    print("Too high. Try again.")
                guess = int(input("Enter your guess: "))
                guesses += 1
            print("Congratulations! You got it right.")
            print("Number of guesses:", guesses)
            guesses = 0  # Reset guesses for next round
        
        elif choice == "2":
            num1, num2 = generate_numbers()
            result = subtract_numbers(num1, num2)
            guess = int(input(f"What is the difference between {num1} and {num2}? "))
            guesses += 1
            while guess != result:
                if guess < result:
                    print("Too low. Try again.")
                else:
                    print("Too high. Try again.")
                guess = int(input("Enter your guess: "))
                guesses += 1
            print("Congratulations! You got it right.")
            print("Number of guesses:", guesses)
            guesses = 0  # Reset guesses for next round
        
        elif choice == "3":
            print("Thank you for playing!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    math_quiz()
