class Grandfather:
    def click_photos(self,name):
        self.name = name
    
    def property(self):
        print(f"{self.name} owns a house")


class Father(Grandfather):
    def businness(self):
        print(f"{self.name} runs a shop")

class Son(Father):
    def study(self):
        print(f"{self.name} study")

s = Son("Rahul")
s.property() 
s.businness()
s.study()

