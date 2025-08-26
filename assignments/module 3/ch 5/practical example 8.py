try:
    filename = input("Enter filename: ")
    with open(filename, "r") as file:
        data = file.read()
        print("File contents:", data)
    num = int(input("Enter a number to divide 100 by: "))
    result = 100 / num
    print("Result:", result)
except FileNotFoundError:
    print("Error: File not found.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
except Exception as e:
    print("An unexpected error occurred:", e)