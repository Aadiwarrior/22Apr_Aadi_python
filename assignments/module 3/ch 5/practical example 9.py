filename = input("Enter filename: ")
file = None
try:
    file = open(filename, "r")
    data = file.read()
    print("File contents:", data)
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("An unexpected error occurred:", e)
finally:
    if file:
        file.close()
        print("File closed.")