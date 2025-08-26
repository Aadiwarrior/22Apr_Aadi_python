# Single Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()
d.bark()

print("\n--- Multiple Inheritance ---")
# Multiple Inheritance
class Father:
    def skills(self):
        print("Father: Gardening")

class Mother:
    def skills(self):
        print("Mother: Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skills()  

print("\n--- Multilevel Inheritance ---")
# Multilevel Inheritance
class Grandparent:
    def show(self):
        print("Grandparent")

class Parent(Grandparent):
    pass

class Child2(Parent):
    pass

ch = Child2()
ch.show()