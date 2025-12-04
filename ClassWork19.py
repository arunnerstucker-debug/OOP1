#CLasses Again
#Abstraction - Information hiding
#Encapsulation - designers - both variables and functions working together in the class
#Inheritance - Reusability
#Polymorphism - (many forms)
#Parents (base) class, child (derived) classes
#multiple inheritance
#multilevel inheritance
from jinja2.filters import do_default

#parameter = "", - polymorphism

#class Class_Name(Parent_Class_Parameter):
#   def init (self, parameters):
#       Parent_Class_Parameter.Parent_Class_Function
#       self.class_Variable


class Person():
    def __init__(self, nn, dd, gg):
        self.name = nn
        self.DOB = dd
        self.gender = gg
    def Display_Person(self):
        print("Name: ", self.name)
        print("Date Of Birth: ", self.DOB)
        print("Gender: ", self.gender)

class Student(Person):
    def __init__(self,x,y,z,a="",b=""):
        Person.__init__(self, x,y,z)
        self.dept = a
        self.id = b
    def Display_Student(self):
        Person.Display_Person(self)
        print("Department: ", self.dept)
        print("ID: ", self.id)

class Faculty(Person):
    def __init__(self,x,y,z,a="",b="",c="",d=""):
        Person.__init__(self,x,y,z)
        self.dept = a
        self.id = b
        self.role = c
        self.office = d
        if a != "":
            print("Within Polymorphisim", a)
    def Display_Faculty(self):
        Person.Display_Person(self)
        print("Department: ", self.dept)
        print("ID: ", self.id)
        print('Role', self.role)
        print("Office Room: ", self.office)

s1 = Student("Jeremy", "11/17/2005", "Male", "Computer Science", "1")
s1.Display_Student()


f1 = Faculty("Sarah", "11/17/1996", "Female", "Math", "1", "Professor", "BTC 121")
f1.Display_Faculty()
