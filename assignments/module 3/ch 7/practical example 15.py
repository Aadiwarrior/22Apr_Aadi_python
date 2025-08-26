class Father:
    def skills(self):
        print("Father: Gardening")

class Mother:
    def tech(self):
        print("Mother: Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skills()
c.tech()  