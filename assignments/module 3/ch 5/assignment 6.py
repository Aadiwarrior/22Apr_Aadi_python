def calc():
    try:
        def add(a, b):
            return a + b
        def subtract(a, b):
            return a - b
        def multiply(a, b):
            return a * b
        def divide(a, b):
            return a / b
        def choice():
            print("Select operation:")
            print("1.Add")
            print("2.Subtract")
            print("3.Multiply")
            print("4.Divide")
            choi=int(input("Enter choice(1/2/3/4):"))
            if choi in (1, 2, 3, 4):
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if choi == 1:
                    add(num1, num2)
                elif choi == 2:
                    subtract(num1, num2)
                elif choi == 3:
                    multiply(num1, num2)
                elif choi == 4:
                    divide(num1, num2)
            else:
                print("Invalid input")
        choice()
    except Exception as e:
        print(e)
calc()