class Grandparent:
    def show(self):
        print("Grandparent")

class Parent(Grandparent):
    pass

class Child2(Parent):
    pass

ch = Child2()
ch.show()