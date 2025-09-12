#Collections -Lists, (Sets, Tuples,) Dictionary (self study)
# Lists & Dictionaries
myList = []

while True:
    option = input("Input 1 to add an element to the list, 2 to remove an element from the list, 3 to remove the last element from the list, 4 to display the list, and 5 to quit: ")
    element = input("Input the element you wish to add or remove from the list, or input 0 if you wish to do make no changes: ")
    if option == '1':
        myList.append(element)
    elif option == '2':
        if len(myList) == 0:
            print("The list is empty.")
        else:
            myList.remove(element)
    elif option == '3':
        if len(myList) == 0:
            print("The list is empty.")
        else:
            myList.pop()
    elif option =='4':
        print(myList)
    else:
        print("Error")

