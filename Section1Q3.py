class father:
    def property(self):
        print("Father owns a house")

    def business(self):
        print("father run a  business")

       
class Son(father):
    def study(self):
        print("son studing")

class Daughter(father):
    def dance(self):
        print("dancinng")

class GrandChild(Son, Daughter): 
     def gaming(self):
        print("play games")



g = GrandChild()

g.property()
g.business()
g. study()
g.dance()
g.gaming()


