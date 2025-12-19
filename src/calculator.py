def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculate(operation, num1, num2):
    if operation == "add":
        return add(num1, num2)
    elif operation == "subtract":
        return subtract(num1, num2)
    elif operation == "multiply":
        return multiply(num1, num2)
    elif operation == "divide":
        return divide(num1, num2)

if __name__ == "__main__":
    print("=== Magic Calculator ===")
    operation = input("Enter operation (add, subtract, multiply, divide): ")
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    
    result = calculate(operation, num1, num2)
    print(f"Result: {result}")
