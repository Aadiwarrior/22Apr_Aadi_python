class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()
print("Add two numbers:", calc.add(5, 3))
print("Add three numbers:", calc.add(5, 3, 2))