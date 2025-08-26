class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)

try:
    value = int(input("Enter a positive number: "))
    if value < 0:
        raise CustomError("CustomError: Negative numbers are not allowed.")
    print("You entered:", value)
except CustomError as ce:
    print(ce)
except ValueError:
    print("Invalid input! Please enter a valid integer.")