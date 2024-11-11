import shutil

# 1. Open a file and write some data to it
with open("example.txt", "w") as file:
    file.write("This is a sample text.\n")
    file.write("We will perform file operations like read, write, append, and copy.")

# 2. Open the file to read its contents
with open("example.txt", "r") as file:
    content = file.read()
    print("File content after writing:")
    print(content)

# 3. Append more data to the file
with open("example.txt", "a") as file:
    file.write("\nAppended text: File operations are useful in many scenarios.")

# 4. Open the file to read the updated content
with open("example.txt", "r") as file:
    content = file.read()
    print("\nFile content after appending:")
    print(content)

# 5. Copy the contents of "example.txt" to another file "copy_example.txt"
shutil.copy("example.txt", "copy_example.txt")

# 6. Read the content of the new copied file
with open("copy_example.txt", "r") as file:
    copied_content = file.read()
    print("\nContent of the copied file:")
    print(copied_content)
