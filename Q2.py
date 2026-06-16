class Person:
    def walk(self):
        print("Person is walking")

    def talk(self):
        print("Person is talking")


class Teacher(Person):
    def teach(self):
        print("Teacher is teaching")


class Student(Person):
    def study(self):
        print("Student is studying")



t1 = Teacher()
s1 = Student()


print("Teacher Object:")
t1.walk()    
t1.talk()    
t1.teach()   


print("\nStudent Object:")
s1.walk()    
s1.talk()    
s1.study()   