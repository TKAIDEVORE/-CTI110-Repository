#TKAI DEVORE
#28APR24
#P4HW2
#INSTRUCTIONS

def main():
    overtime_total = 0
    regular_pay_total = 0
    gross_pay_total = 0
    num_employees = 0

    while True:
        employee_name = input("Enter employee name (or 'Done' to terminate): ")
        if employee_name.lower() == "done":
            break

        pay_rate = float(input("Enter pay rate for employee: "))
        hours_worked = float(input("Enter hours worked by employee: "))

        if hours_worked > 40:
            overtime_hours = hours_worked - 40
            overtime_pay = overtime_hours * 1.5 * pay_rate
            regular_pay = 40 * pay_rate
            gross_pay = regular_pay + overtime_pay
        else:
            regular_pay = hours_worked * pay_rate
            gross_pay = regular_pay

        regular_pay_total += regular_pay
        overtime_total += overtime_pay if hours_worked > 40 else 0
        gross_pay_total += gross_pay
        num_employees += 1

    print("Number of employees entered:", num_employees)
    print("Total amount paid for overtime:", overtime_total)
    print("Total amount paid for regular pay:", regular_pay_total)
    print("Total amount paid for all employees (gross pay total):", gross_pay_total)

if __name__ == "__main__":
    main()
