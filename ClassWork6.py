#Dictionaries like lists for different types of data
#Dictionary = {"d1":"string", "d2":"String"}

myStudents = {"s1": {
    "name":"Justus", "major":"CS", "Year":"Freshman", "TCredits":15, "GPA":0.0
}, "s2":{
    "name":"Jemi", "major":"EE", "Year":"Sophmore", "TCredits":50, "GPA":3.9
}}
#myStudents.update({"s3": {"name":"Melba","major":"Biology", "Year":"Senior", "TCredits":110, "GPA":3.2}})
#print(myStudents)

#del myStudents["s2"]
# print(myStudents)
#
# sid = input("Input the Student ID: ")
# name = input("Input the Student name: ")
# major = input("Input the Student Major: ")
# year = input("Input the Student year: ")
# tc = int(input("Input the Student total credit hours: "))
# gpa = float(input("Input the Student GPA: "))
#
# myStudents.update({sid:{"name":name, "major":major, "year":year, "tCredits":tc, "GPA":gpa}})
# print(myStudents)
#
# for Student_record in myStudents.items():
#     print(Student_record)
#     print("------------------------------------")

while True:
    option = input("Choose one of the following:\n"
                   "1. Add an element to the dictionary,\n"
                   "2. Remove an element from the dictionary,\n"
                   "3. Replace an element from the dictionary,\n"
                   "4. Print the dictionary of elements,\n"
                   "5. Exit: ")

    if option == '1':
        sid = input("Input the Student ID: ")
        name = input("Input the Student name: ")
        major = input("Input the Student Major: ")
        year = input("Input the Student year: ")
        tc = int(input("Input the Student total credit hours: "))
        gpa = float(input("Input the Student GPA: "))

        myStudents.update({sid: {"name": name, "major": major, "year": year, "tCredits": tc, "GPA": gpa}})
    elif option == '2':
        if len(myStudents) == 0:
            print("Error: No elements in the Dictionary")
        else:
            toDel = input("Input the Student ID of the student you wish to delete: ")
            del myStudents[toDel]
    elif option == '3':
        sid = input("Input the Student ID: ")
        name = input("Input the Student name: ")
        major = input("Input the Student Major: ")
        year = input("Input the Student year: ")
        tc = int(input("Input the Student total credit hours: "))
        gpa = float(input("Input the Student GPA: "))

        myStudents.update({sid: {"name": name, "major": major, "year": year, "tCredits": tc, "GPA": gpa}})
    elif option =='4':
        for Student_record in myStudents.items():
            print(Student_record)
            print("------------------------------------")
    elif option == '5':
        break
    else:
        print("Error")