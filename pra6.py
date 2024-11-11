import math
import random

# Generate a random number between 1 and 100
num = random.randint(1, 100)
print(f"Random number generated: {num}")

# Use math functions on the random number
print(f"Square root of {num}: {math.sqrt(num)}")
print(f"Ceiling of {num}: {math.ceil(num)}")
print(f"Floor of {num}: {math.floor(num)}")
print(f"Cosine of {num}: {math.cos(num)}")

# Calculate the logarithm (base 10) of the number
# Add a small check to avoid errors if num is 0
if num > 0:
    print(f"Logarithm (base 10) of {num}: {math.log10(num)}")
else:
    print("Cannot calculate logarithm for zero.")
