with open("example.txt", "r") as file:
    print("Initial cursor position:", file.tell())
    file.read(5)
    print("Cursor position after reading 5 characters:", file.tell())