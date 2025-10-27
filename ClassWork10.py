#class Student:
#   def ___ init ___ (self) #Constructor function
#       define member variables
#       self.SID =
#       self.stu_Name =
#   def add_student(self):
#       self.SID = input("Enter the SID: ")
#   def edit_student(self)




#Main code:
#s1 = Student() #Calling the constructor
#s1.add_student()

class Student:
    def __intit__(self):
        self.SID = ""
        self.stu_name = ""
        self.dob = ""
        self.major = ""
        self.gpa = ""
        self.courses = []
    def add_student(self):
        self.SID = input("Enter the SID: ")
        self.stu_name = input("Enter the student Name: ")
        self.dob = input("Enter the student Date of Birth: ")
        self.major = input("Enter the student Major: ")
        self.gpa = input("Enter the student GPA: ")
    def edit_student(self):
        while True:
            option = input("Choose one of the following:\n"
                           "1. Edit the SID:\n"
                           "2. Edit the student Name:\n"
                           "3. Edit the Date of Birth:\n"
                           "4. Edit the student Major:\n"
                           "5. Edit the student GPA:\n"
                           "6. Quit editing: ")
            if option == '1':
                self.SID = input("Enter the new SID: ")
            elif option == '2':
                self.stu_name = input("Enter the student Name: ")
            elif option == '3':
                self.dob = input("Enter the student Date of Birth: ")
            elif option =='4':
                self.major = input("Enter the student Major: ")
            elif option == '5':
                self.gpa = input("Enter the student GPA: ")
            elif option == '6':
                break
            else:
                print("Error: Invalid Input, please try again.")
    def register_courses(self, cc1):
        self.courses.append(cc1)
    def display_student(self):
        print("Student ID:", self.SID)
        print("Student Name:", self.stu_name)
        print("Student Date of Birth: ", self.dob)
        print("Student major: ", self.major)
        print("Student gpa: ", self.gpa)
        for x in self.courses:
            print(f"Courses: {x.cid}, {x.cname}")

class Course:
    def __init__(self, x, y):
        self.cid = x
        self.cname = y
    def add_course(self):
        self.cid = input("Input course ID: ")
        self.cname = input("Input the course name: ")
    def display_course(self):
        print("Course ID: ", self.cid)
        print("Course Name: ", self.cname)

s1 = Student()

s1.add_student()

s2 = Student()
s2.add_student()

s3 = Student()
s3.add_student()

c1 = Course()
c2 = Course()
c1.add_course()
c2.add_course()
c3 = Course("CS1233", "OOP")
c4 = Course("CS2423", "Web App")

s1.register_courses(c1)
s2.register_courses(c2)
s1.register_courses(c2)

s1.display_student()
s3.display_student()