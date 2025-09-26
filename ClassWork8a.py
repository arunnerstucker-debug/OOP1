#Queue - First in first out FIFO
#Stack -

#myqueue = []

#def enqueue():
#def dequeue():
#display

myQueue = []

def enqueue():
    add = input("Enter the value to be added to the list: ")
    myQueue.append(add)

def dequeue():
    if len(myQueue) == 0:
        print("There are no elements left to be removed.")
    else:
        myQueue.pop(0)

while 1:
    option = input("Choose one of the following:\n"
                   "1. Add a value to the queue:\n"
                   "2. Remove a value from the queue:\n"
                   "3. Display the queue:\n"
                   "4. Quit the program: ")
    if option == '1':
        enqueue()
    elif option == '2':
        dequeue()
    elif option == '3':
        print(myQueue)
    elif option == '4':
        break
    else:
        print("Error: Invalid Input. Please try again: ")