with open("source.png", "rb") as source:
    data = source.read()

with open("copy.png", "wb") as destination:
    destination.write(data)