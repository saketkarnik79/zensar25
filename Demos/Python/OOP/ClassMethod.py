class Employee:
    company = "Zensar Technologies"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_company(cls, company_name):
        cls.company = company_name

employee1 = Employee("Amit")
employee2 = Employee("Priya")

Employee.change_company("Zensar Technologies Pvt. Ltd.")
print(employee1.company)
print(employee2.company)