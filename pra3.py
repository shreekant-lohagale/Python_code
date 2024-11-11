# Initialize variables for sum of even and odd numbers
even_sum = 0
odd_sum = 0

# Input: Number of elements in the list
n = int(input("Enter the number of elements in the list: "))

# Loop to get all numbers from the user and categorize them as even or odd
for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    
    # Decision making to check if the number is even or odd
    if num % 2 == 0:
        even_sum += num  # Add to even sum if number is even
    else:
        odd_sum += num   # Add to odd sum if number is odd

# Output the results
print("\nResults:")
print(f"Sum of even numbers: {even_sum}")
print(f"Sum of odd numbers: {odd_sum}")
