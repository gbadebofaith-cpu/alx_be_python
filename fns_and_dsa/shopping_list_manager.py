# arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform basic arithmetic operations.

    Parameters:
        num1 (float): The first number
        num2 (float): The second number
        operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide')

    Returns:
        float or str: The result of the operation, or an error message for invalid cases
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero is not allowed"
        return num1 / num2
    else:
        return "Error: Enter the correct operation"
 
 # Example usage:
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input(
    "Enter the operation (add, subtract, multiply, divide): ").strip().lower()

result = perform_operation(num1, num2, operation)
print(f"Result: {result}")
