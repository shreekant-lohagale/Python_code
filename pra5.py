def binary_search_string(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Input list and target
arr = sorted(input("Enter sorted list of words (separated by spaces): ").split())
target = input("Enter the word to search for: ")

# Perform binary search
result = binary_search_string(arr, target)

# Output result
if result != -1:
    print(f"'{target}' found at index {result}")
else:
    print(f"'{target}' not found in the list")
