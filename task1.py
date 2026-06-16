class Person:
    def walk(self):
        print("Walking")

class Student(Person):   
    def study(self):
        print("Studying")

s = Student()

s.walk()   
s.study()   