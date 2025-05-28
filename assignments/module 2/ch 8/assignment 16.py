i=4
while i>=2:
    def sum(a, b):
        print( a + b)
    def sub(a, b):
        print( a - b)
    def mul(a, b):
        print( a * b)
    def div(a, b):
        print( a / b)
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print('choose:' + '\n1. Sum' + '\n2. Subtraction' + '\n3. Multiplication' + '\n4. Division')
    c=int(input("Enter your choice: "))
    if c==1:
        sum(a, b)
    elif c==2:
        sub(a, b)
    elif c==3:
        mul(a, b)
    elif c==4:
        div(a, b)
    else:
        print("Invalid choice")
    i=int(input("Enter 0 to exit or 1 to continue: "))
if i == 0:
    print("Exiting the program")
else:
    print("Invalid input, exiting the program")
