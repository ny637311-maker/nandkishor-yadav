class Animal:
    def __init__(self,name):
        self.name = name

        def eat(self):
            print(f"{self.name} is eating")

class Dog(Animal):
    def bark(self):
         print(f"{self.name} say woof")

# object 
d = Dog("Bruno")
d.eat()
d.bark()