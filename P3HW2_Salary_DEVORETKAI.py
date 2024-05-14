#Tkai DeVore
#21Apr
#P3HW2
#Salary


def calculate_pay(hours_worked, pay_rate):
    regular_hours = min(hours_worked, 40)
    overtime_hours = max(hours_worked - 40, 0)
    overtime_pay = 0
    if overtime_hours > 0:
        overtime_pay = overtime_hours * pay_rate * 1.5
    regular_pay = regular_hours * pay_rate
    gross_pay = regular_pay + overtime_pay
    return regular_hours, overtime_hours, overtime_pay, regular_pay, gross_pay

if __name__ == "__main__":
    # Input from the user
    employee_name = input("Enter the name of the employee: ")
    hours_worked = float(input("Enter the number of hours the employee worked this week: "))
    pay_rate = float(input("Enter the employee's pay rate: "))

    # Calculate pay
    regular_hours, overtime_hours, overtime_pay, regular_pay, gross_pay = calculate_pay(hours_worked, pay_rate)

    # Display results
    print("\nEmployee name:", employee_name)
    print("Pay rate:", pay_rate)
    print("Number of hours worked:", hours_worked)
    print("Overtime hours:", overtime_hours)
    print("Overtime pay:", overtime_pay)
    print("Pay for regular hours:", regular_pay)
    print("Gross pay:", gross_pay)
