# Grade-Based Employee Salary Calculator

print("===== Employee Salary Calculator =====")

employee_name = input("Enter employee name: ")
grade = input("Enter employee grade (A/B/C): ").upper()
basic_salary = float(input("Enter basic salary: "))

# Salary calculation based on employee grade

if grade == "A":
    hra_rate = 0.30       # 30% HRA
    da_rate = 0.15        # 15% DA
    ta_rate = 0.10        # 10% TA
    bonus_rate = 0.10     # 10% Bonus
    pf_rate = 0.12        # 12% PF
    tax_rate = 0.10       # 10% Tax

elif grade == "B":
    hra_rate = 0.25       # 25% HRA
    da_rate = 0.12        # 12% DA
    ta_rate = 0.08        # 8% TA
    bonus_rate = 0.08     # 8% Bonus
    pf_rate = 0.12        # 12% PF
    tax_rate = 0.08       # 8% Tax

elif grade == "C":
    hra_rate = 0.20       # 20% HRA
    da_rate = 0.10        # 10% DA
    ta_rate = 0.05        # 5% TA
    bonus_rate = 0.05     # 5% Bonus
    pf_rate = 0.12        # 12% PF
    tax_rate = 0.05       # 5% Tax

else:
    print("Invalid employee grade.")
    exit()

# Calculate allowances

hra = basic_salary * hra_rate
da = basic_salary * da_rate
ta = basic_salary * ta_rate
bonus = basic_salary * bonus_rate

# Calculate gross salary

gross_salary = basic_salary + hra + da + ta + bonus

# Calculate deductions

pf = basic_salary * pf_rate
tax = gross_salary * tax_rate

total_deductions = pf + tax

# Calculate net salary

net_salary = gross_salary - total_deductions

# Display salary details

print("\n===== Salary Details =====")

print("Employee Name :", employee_name)
print("Employee Grade:", grade)

print("\n--- Earnings ---")
print("Basic Salary  :", basic_salary)
print("HRA           :", hra)
print("DA            :", da)
print("TA            :", ta)
print("Bonus         :", bonus)
print("Gross Salary  :", gross_salary)

print("\n--- Deductions ---")
print("PF            :", pf)
print("Tax           :", tax)
print("Total Deduction:", total_deductions)

print("\nNet Salary    :", net_salary)