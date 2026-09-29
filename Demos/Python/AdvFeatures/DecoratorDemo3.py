def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

# def greet():
#     print("Hello, Welcome to Python!")


# greet = my_decorator(greet)
@my_decorator
def greet():
    print("Hello, Welcome to Python!")

greet()