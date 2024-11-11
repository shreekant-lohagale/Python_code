# List Operations
print("=== List Operations ===")
my_list = [1, 2, 3, 4, 5]  # Creation
print("Original List:", my_list)

# Indexing
print("Element at index 2:", my_list[2])

# Slicing
print("Sliced List (1:4):", my_list[1:4])

# Concatenation
list2 = [6, 7, 8]
concatenated_list = my_list + list2
print("Concatenated List:", concatenated_list)

# Repetition
repeated_list = my_list * 2
print("Repeated List:", repeated_list)


# Tuple Operations
print("\n=== Tuple Operations ===")
my_tuple = (10, 20, 30, 40, 50)  # Creation
print("Original Tuple:", my_tuple)

# Indexing
print("Element at index 3:", my_tuple[3])

# Slicing
print("Sliced Tuple (1:3):", my_tuple[1:3])

# Concatenation
tuple2 = (60, 70, 80)
concatenated_tuple = my_tuple + tuple2
print("Concatenated Tuple:", concatenated_tuple)

# Repetition
repeated_tuple = my_tuple * 2
print("Repeated Tuple:", repeated_tuple)


# Dictionary Operations
print("\n=== Dictionary Operations ===")
my_dict = {'a': 1, 'b': 2, 'c': 3}  # Creation
print("Original Dictionary:", my_dict)

# Indexing (Accessing value by key)
print("Value for key 'b':", my_dict['b'])

# Adding new key-value pair
my_dict['d'] = 4
print("Dictionary after adding new key-value pair:", my_dict)

# Concatenation (Updating a dictionary with another dictionary)
dict2 = {'e': 5, 'f': 6}
my_dict.update(dict2)
print("Concatenated Dictionary:", my_dict)

# Dictionary does not support repetition or slicing directly.


# Set Operations
print("\n=== Set Operations ===")
my_set = {1, 2, 3, 4, 5}  # Creation
print("Original Set:", my_set)

# Adding an element
my_set.add(6)
print("Set after adding element:", my_set)

# Concatenation (Union of two sets)
set2 = {4, 5, 6, 7, 8}
concatenated_set = my_set | set2
print("Union of Sets (Concatenation):", concatenated_set)

# Repetition (Not supported in sets as they are unordered and unique)

# Slicing and indexing are not supported in sets as they are unordered.
