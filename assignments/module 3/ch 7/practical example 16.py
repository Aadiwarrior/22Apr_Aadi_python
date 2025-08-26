# Hierarchical Inheritance Example

class Animal:
    def eat(self):
        print("Animal eats")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

d = Dog()
d.eat()
d.bark()

c = Cat()
c.eat()
c.meow()