with open("created_file.txt", "w") as file:
    file.write("This is a string written to created_file.txt.")

with open("created_file", "r") as aa:
    content = aa.read()
    print("Contents of example.txt:")
    print(content)