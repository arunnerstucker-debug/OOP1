myStack = []

def enstack():
    add = input("Enter the value to be added to the list: ")
    myStack.append(add)

def destack():
    if len(myStack) == 0:
        print("There are no elements left to be removed.")
    else:
        myStack.pop((len(myStack) - 1))

while 1:
    option = input("Choose one of the following:\n"
                   "1. Add a value to the stack:\n"
                   "2. Remove a value from the stack:\n"
                   "3. Display the stack:\n"
                   "4. Quit the program: ")
    if option == '1':
        enstack()
    elif option == '2':
        destack()
    elif option == '3':
        print(myStack)
    elif option == '4':
        break
    else:
        print("Error: Invalid Input. Please try again: ")

