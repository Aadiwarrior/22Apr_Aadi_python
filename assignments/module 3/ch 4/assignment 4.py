with open("example.txt", "w") as file:
    file.write("First line.\n")
    file.write("Second line.\n")
    file.write("Third line.\n")

with open("created_file.txt", "w") as file:
    file.write("This is a string written to created_file.txt.")

with open("example.txt", "r") as file:
    content = file.read()
    print("Contents of example.txt:")
    print(content)

with open("created_file.txt", "r") as file:
    data = file.read()
    print("Contents of created_file.txt:")
    print(data)

with open("example.txt", "r") as file:
    print("Initial cursor position:", file.tell())
    file.read(5)
    print("Cursor position after reading 5 characters:", file.tell())
