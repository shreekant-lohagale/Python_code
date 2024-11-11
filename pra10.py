def divide_numbers():
    try:
        # Input two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Try to divide
        result = num1 / num2
    except ZeroDivisionError:
        # Handle division by zero error
        print("Error: Cannot divide by zero.")
    except ValueError:
        # Handle invalid input (e.g., non-numeric input)
        print("Error: Please enter valid numbers.")
    else:
        # This block runs if no exception occurs
        print(f"The result of dividing {num1} by {num2} is: {result}")
    finally:
        # This block always runs, regardless of whether an exception occurred or not
        print("Execution completed.")

# Call the function
divide_numbers()
