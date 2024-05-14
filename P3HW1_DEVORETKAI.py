#Tkai DeVore
#21APR
#P3HW1
#Debug



# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules
mod_1 = int(input("Enter grade for Module 1: "))
mod_2 = int(input("Enter grade for Module 2: "))
mod_3 = int(input("Enter grade for Module 3: "))
mod_4 = int(input("Enter grade for Module 4: "))
mod_5 = int(input("Enter grade for Module 5: "))
mod_6 = int(input("Enter grade for Module 6: "))

# add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# TO DO: determine lowest, highest , sum and average for grades
lowest = min(grades)
highest = max(grades)
sum_of_grades = sum(grades)


# determine letter grade for average
avg = sum_of_grades / len(grades)

print("\nResults:")
print("Lowest Grade:", lowest)
print("Highest Grade:", highest)
print("Sum of Grades:", sum_of_grades)
print("Average Grade: {:.2f}".format(avg))

if avg >= 90:
 print("Your grade is: A")

elif avg >= 80:
 print("Your grade is: B")

elif avg >= 70:
 print("Your grade is: C")
 
elif avg >= 60:
 print("Your grade is: D")    

elif avg >= 50:    
 print('Your grade is: F') # TO DO: finish this





