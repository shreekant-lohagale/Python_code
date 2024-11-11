def linear_search(arr, target):
    # Loop through each element in the array
    for i in range(len(arr)):
        # Check if the current element is equal to the target
        if arr[i] == target:
            return i  # Return the index if found
    return -1  # Return -1 if the target is not in the array

# Input: Number of elements
n = int(input("Enter the number of elements in the list: "))

# Input: Elements of the list
arr = []
print("Enter the elements:")
for i in range(n):
    element = int(input(f"Element {i + 1}: "))
    arr.append(element)

# Input: Target element to search for
target = int(input("Enter the target number to search for: "))

# Perform the linear search
result = linear_search(arr, target)

# Output the result
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")
