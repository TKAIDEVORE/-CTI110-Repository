#Tkai DeVore
#14 APR24
#P2HW2
#HW Assignmnets 

# Pseudocode:
# 1. Prompt the user to enter grades for each module separately.
# 2. Store the grades entered by the user in a list.
# 3. Calculate the lowest grade in the list using the min() function.
# 4. Calculate the highest grade in the list using the max() function.
# 5. Calculate the sum of grades in the list using the sum() function.
# 6. Calculate the average of grades in the list by dividing the sum of grades by the number of grades.
# 7. Display the lowest grade, highest grade, sum of grades, and average of grades.

# Get grades for each module
module_1_grade = float(input("Enter grade for Module 1: "))
module_2_grade = float(input("Enter grade for Module 2: "))
module_3_grade = float(input("Enter grade for Module 3: "))
module_4_grade = float(input("Enter grade for Module 4: "))
module_5_grade = float(input("Enter grade for Module 5: "))
module_6_grade = float(input("Enter grade for Module 6: "))

# Store grades in a list
grades_list = [module_1_grade, module_2_grade, module_3_grade, module_4_grade, module_5_grade, module_6_grade]

# Calculate lowest grade
lowest_grade = min(grades_list)

# Calculate highest grade
highest_grade = max(grades_list)

# Calculate sum of grades
sum_of_grades = sum(grades_list)

# Calculate average of grades
average_grade = sum_of_grades / len(grades_list)

# Display results
print("\nResults:")
print("Lowest Grade:", lowest_grade)
print("Highest Grade:", highest_grade)
print("Sum of Grades:", sum_of_grades)
print("Average Grade: {:.2f}".format(average_grade))
