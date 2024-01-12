def calculator():
    """Provides a simple calculator with basic arithmetic operations."""

    while True:
        try:
            operation = input("""Please select an operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exponentiation
6. Modulus (remainder of division)
7. Exit
Enter choice(1/2/3/4/5/6/7): """)

            if operation in ('1', '2', '3', '4', '5', '6'):
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if operation == '1':
                    print(num1, "+", num2, "=", add(num1, num2))
                elif operation == '2':
                    print(num1, "-", num2, "=", subtract(num1, num2))
                elif operation == '3':
                    print(num1, "*", num2, "=", multiply(num1, num2))
                elif operation == '4':
                    print(num1, "/", num2, "=", divide(num1, num2))
                elif operation == '5':
                    print(num1, "**", num2, "=", exponentiate(num1, num2))
                elif operation == '6':
                    print(num1, "%", num2, "=", modulus(num1, num2))
            elif operation == '7':
                print("Exiting calculator...")
                break
            else:
                print("Invalid input. Please enter a valid choice (1-7).")

        except ValueError:
            print("Invalid input. Please enter numbers only.")

def add(x, y):
    """Adds two numbers."""
    return x + y

def subtract(x, y):
    """Subtracts two numbers."""
    return x - y

def multiply(x, y):
    """Multiplies two numbers."""
    return x * y

def divide(x, y):
    """Divides two numbers."""
    if y == 0:
        return "Division by zero is not allowed."
    else:
        return x / y

def exponentiate(x, y):
    """Raises a number to a power."""
    return x ** y

def modulus(x, y):
    """Returns the remainder of division."""
    return x % y

if __name__ == "__main__":
    calculator()
