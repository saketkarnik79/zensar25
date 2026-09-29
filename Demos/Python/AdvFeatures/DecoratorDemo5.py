def log_function(func):
    def wrapper(*args, **kwargs):
        print("Calling function:", func.__name__)
        result = func(*args, **kwargs)
        print("Function execution completed")
        return result
    return wrapper


@log_function
def calculate_salary(basic_salary, bonus):
    return basic_salary + bonus

salary = calculate_salary(30000, 5000)
print("Total Salary:", salary)