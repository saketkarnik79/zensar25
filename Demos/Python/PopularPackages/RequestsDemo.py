import requests

response = requests.get("https://example.com")

print("Status Code:", response.status_code)

if response.status_code == 200:
    print("Website accessed successfully!")
else:
    print("Unable to access website.")