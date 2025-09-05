#while (condition):
#   break

while 1:

    print("1. Addition (n1 + n2)")
    print("2. Subtraction (n1 - n2)")
    print("3. Multiplication (n1 * n2)")
    print("4. Division (n1 / n2)")
    print("5. Quit")

    option = input("Enter your choice: ")

    if option == "5":
        break
    else:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        if option == "1":
            print(num1, " + ", num2, " = ", num1 + num2)
        elif option == "2":
            print(num1, " - ", num2, " = ", num1 - num2)
        elif option == "3":
            print(num1, " * ", num2, " = ", num1 * num2)
        elif option == "4":
            print(num1, " / ", num2, " = ", num1 / num2)
        else:
            print("Error: Invalid input for choice. No operation performed. Please try again or quit the program.")