# Method Overloading (using default arguments)
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()
print("Add two numbers:", calc.add(5, 3))
print("Add three numbers:", calc.add(5, 3, 2))

print("\n--- Method Overriding ---")
# Method Overriding
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

a = Animal()
a.speak()

d = Dog()
d.speak()