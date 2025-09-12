stu_name = []
stu_age = []

while True:
    option = input("Input a number to choose one of the following options:\n"
                   "1. Add an element to the list,\n"
                   "2. Remove an element from the list,\n"
                   "3. Replace an element from the list,\n"
                   "4. Sort the elements in the list,\n"
                   "5. Reverse the elements in the list,\n"
                   "6. Print the list elements,\n"
                   "7. Exit: ")

    if option == '1':
        name = input("What is the name of the student you wish to add: ")
        stu_name.append(name)
        age = int(input("How old is the student: "))
        stu_age.append(age)
    elif option == '2':
        if len(stu_name) == 0:
            print("The list is empty.")
        else:
            name = input("Which student do you wish to remove from the list: ")
            stu_name.remove(name)
            age = int(input("How old was the student: "))
            stu_age.remove(age)
    elif option == '3':
        x = int(input("What is the index of the age to be replace: "))
        new_age = int(input("What is the new value of the age: "))
        stu_age[x] = new_age
        x = int(input("What is the index of the student to be replaced: "))
        new_name = input("What is the new name: ")
        stu_age[x] = new_name
    elif option =='4':
        stu_name.sort()
        stu_age.sort()
    elif option == '5':
        stu_name.reverse()
        stu_age.sort()
    elif option == '6':
        print(stu_name)
        print(stu_age)
    elif option == '7':
        break
    else:
        print("Error")