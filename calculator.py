def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

# Example usage:
print(add(10, 5))
print(subtract(10, 50))
print(multiply(100, 5))
print(divide(10, 50))