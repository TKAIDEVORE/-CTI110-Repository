#TKAI DEVORE
#28APR24
#P4HW1
#INTEGERS

def calculate_letter_grade(average):
    if average >= 90:
        return "A"
    elif 80 <= average < 90:
        return "B"
    elif 70 <= average < 80:
        return "C"
    elif 60 <= average < 70:
        return "D"
    else:
        return "F"

def main():
    while True:
        num_scores = int(input("Enter the number of scores you want to enter: "))
        score_list = []

        for i in range(num_scores):
            while True:
                score = int(input(f"Enter score {i+1}: "))
                if 0 <= score <= 100:
                    score_list.append(score)
                    break
                else:
                    print("Invalid score. Please enter a valid score between 0 and 100.")

        lowest_score = min(score_list)
        print(f"Lowest score entered: {lowest_score}")

        score_list.remove(lowest_score)
        print("Score list after dropping lowest score:", score_list)

        average = sum(score_list) / len(score_list)
        print("Average of scores in modified list:", average)

        letter_grade = calculate_letter_grade(average)
        print("Letter grade:", letter_grade)

        repeat = input("Do you want to run the program again? (yes/no): ")
        if repeat.lower() != "yes":
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
