import os

if not os.path.exists("data"):
    os.mkdir("data")
    print("Directory created.")
else:
    print("Directory already exists.")
os.makedirs("data/students/2026", exist_ok = True)
