class Animal:
    def eat(self):
        print("Animal eats")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

class Pet(Dog, Cat):
    def play(self):
        print("Pet plays")

p = Pet()
p.eat()  
p.bark() 
p.meow() 
p.play() 