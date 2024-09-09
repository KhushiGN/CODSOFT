def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    while True:
        print("\nWelcome to the simple calculator!")
        
        try:
            # Input the first number
            num1 = float(input("Enter the first number: "))
            
            # Input the second number
            num2 = float(input("Enter the second number: "))
            
            # Input the operation choice
            print("\nSelect operation:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Exit")
            operation = input("Enter the operation (1/2/3/4/5): ")
            
            if operation == '5':
                print("Exiting the calculator. Goodbye!")
                break
            
            # Perform the operation and display the result
            if operation == '1':
                result = add(num1, num2)
                print(f"The result of {num1} + {num2} is {result}.")
            elif operation == '2':
                result = subtract(num1, num2)
                print(f"The result of {num1} - {num2} is {result}.")
            elif operation == '3':
                result = multiply(num1, num2)
                print(f"The result of {num1} * {num2} is {result}.")
            elif operation == '4':
                result = divide(num1, num2)
                print(f"The result of {num1} / {num2} is {result}.")
            else:
                print("Invalid operation choice. Please choose 1, 2, 3, 4, or 5.")
        
        except ValueError:
            print("Invalid input! Please enter numeric values for the numbers.")

if __name__ == "__main__":
    calculator()
