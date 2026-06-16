class parent:
    def property(self):
        print("Father owns a house")

class Son(parent):
    def money(self):
        print("Sonn plays cricket")

class Daughter(parent):
    def dance(self):
        print("dancinng")

s = Daughter()
s.dance()
s.property()

s = Son()
s.money()
s.property()