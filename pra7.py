def describe_person(name, age=25, *hobbies, **additional_info):
    # Positional argument: 'name'
    print(f"Name: {name}")
    
    # Default argument: 'age'
    print(f"Age: {age}")
    
    # Non-keyword variable-length argument: *hobbies
    if hobbies:
        print(f"Hobbies: {', '.join(hobbies)}")
    
    # Keyword variable-length argument: **additional_info
    if additional_info:
        print("Additional Information:")
        for key, value in additional_info.items():
            print(f"  {key}: {value}")

# Call the function using different argument types

# 1. Positional arguments and default argument
describe_person("Alice")

# 2. Positional arguments, default argument, and variable-length positional arguments
describe_person("Bob", 30, "Reading", "Cycling", "Gaming")

# 3. Positional arguments, default argument, and keyword arguments
describe_person("Charlie", 22, city="New York", job="Engineer")

# 4. All types of arguments
describe_person("David", 40, "Photography", "Travelling", city="Paris", job="Artist")
