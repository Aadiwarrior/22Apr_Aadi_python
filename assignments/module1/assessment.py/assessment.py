i=2
while i>=1:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    c=input("Enter operation (+, -, *, /): ")
    if c == '+':
        print("The sum is:", a + b)
    elif c == '-':
        print("The difference is:", a - b)
    elif c == '*':
        print("The product is:", a * b)
    elif c == '/':
        if b != 0:
            print("The quotient is:", a / b)
        else:
            print("Error: Division by zero")
    else:
        print("Invalid operation")
    i = int(input("Enter 0 to exit or 1 to continue: "))
if i == 0:
    print("Exiting the program")
else:
    print("Invalid input, exiting the program")
