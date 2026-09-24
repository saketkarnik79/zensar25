def calculate_total(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# example usage
result = calculate_total(1, 2, 3, 4, 5)
print(f"Total: {result}")
result2 = calculate_total(10, 20, 30)
print(f"Total: {result2}")
result3 = calculate_total(200,100)
print(f"Total: {result3}")