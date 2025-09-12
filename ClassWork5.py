myList = []

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
        element = int(input("What is the element you wish to add: "))
        myList.append(element)
    elif option == '2':
        if len(myList) == 0:
            print("The list is empty.")
        else:
            element = int(input("What is the element you wish to remove: "))
            myList.remove(element)
    elif option == '3':
        x = int(input("What is the index of the element to be replace: "))
        new_element = int(input("What is the new value of the element: "))
        myList[x] = new_element
    elif option =='4':
        myList.sort()
    elif option == '5':
        myList.reverse()
    elif option == '6':
        print(myList)
    elif option == '7':
        break
    else:
        print("Error")
