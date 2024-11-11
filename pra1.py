import sys

def main():
    # Check if arguments are provided
    if len(sys.argv) > 1:
        # Attempt to convert the arguments to numbers and add them
        try:
            # Get the first and second arguments as numbers
            num1 = float(sys.argv[1])
            num2 = float(sys.argv[2])
            # Perform addition
            result = num1 + num2
            print(f"The sum of {num1} and {num2} is {result}.")
        except ValueError:
            print("Please provide two numbers as arguments.")
    else:
        print("No arguments provided. Please enter two numbers.")

if __name__ == "__main__":
    main()
