try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
    lst = [1, 2, 3]
    print(lst[5])
except ValueError:
    print("Invalid input! Please enter a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except IndexError:
    print("List index out of range.")
except Exception as e:
    print("An unexpected error occurred:", e)