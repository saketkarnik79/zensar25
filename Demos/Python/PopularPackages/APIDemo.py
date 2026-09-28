import requests

# API URL
url = "https://jsonplaceholder.typicode.com/users/1"

# Send GET request
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    data = response.json()

    print("User Details")
    print("------------")
    print("Name:", data["name"])
    print("Username:", data["username"])
    print("Email:", data["email"])
    print("City:", data["address"]["city"])

else:
    print("Failed to retrieve data.")