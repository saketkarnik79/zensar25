def calculate(a, b):
    """Function to calculate the sum and product of two numbers."""
    sum_result = a + b
    subtract_result = a - b
    product_result = a * b
    divide_result = a / b if b != 0 else None  # Avoid division by zero
    return sum_result, product_result, subtract_result, divide_result

# Example usage
sum, prod, sub, div = calculate(10, 5)

print(f"Sum: {sum}, Product: {prod}, Subtract: {sub}, Divide: {div}")
