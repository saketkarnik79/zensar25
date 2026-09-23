# Employee Salary Calculator

print("===== Employee Salary Calculator =====")

employee_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))

# Calculate allowances
hra = basic_salary * 0.20       # 20% HRA
da = basic_salary * 0.10        # 10% DA
ta = basic_salary * 0.05        # 5% TA

# Calculate gross salary
gross_salary = basic_salary + hra + da + ta

# Calculate deductions
pf = basic_salary * 0.12        # 12% PF
tax = gross_salary * 0.05       # 5% Tax

total_deductions = pf + tax

# Calculate net salary
net_salary = gross_salary - total_deductions

# Display salary details
print("\n===== Salary Details =====")
print("Employee Name:", employee_name)
print("Basic Salary:", basic_salary)
print("HRA:", hra)
print("DA:", da)
print("TA:", ta)
print("Gross Salary:", gross_salary)
print("PF:", pf)
print("Tax:", tax)
print("Total Deductions:", total_deductions)
print("Net Salary:", net_salary)