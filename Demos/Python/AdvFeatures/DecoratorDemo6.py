def check_login(func):
    def wrapper(is_logged_in):
        if is_logged_in:
            func(is_logged_in)
        else:
            print("Access Denied. Please login.")
    return wrapper

@check_login
def dashboard(is_logged_in):
    print("Welcome to Dashboard")

dashboard(False)