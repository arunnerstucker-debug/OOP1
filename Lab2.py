myEmployees = {}

while True:
    option = input("Choose one of the following options:\n"
                   "1. Add an Employee\n"
                   "2. Delete a Employee\n"
                   "3. Modify a Employee\n"
                   "4. Display all the Employees\n"
                   "5. Exit the program: ")
    if option == '1':
        empid = input("Input the employee ID: ")
        employeeName = input("Input the name of the employee: ")
        basicPay = int(input("Input the basic pay of the employee: "))
        allowance = int(input("Input the allowance of the employee: "))
        deductions = int(input("Input the deductions of the employee: "))
        taxes = int(input("Input the taxes of the employee: "))
        netPay = basicPay + allowance
        grossPay = netPay - (deductions + taxes)

        myEmployees.update({empid:
                                {"EmployeeName":{employeeName}, "BasicPay": {basicPay}, "Allowance":{allowance},
                                 "Deductions":{deductions}, "Taxes":{taxes}, "NetPay":{netPay}, "GrossPay":{grossPay}}})
    elif option == '2':
        if len(myEmployees) == 0:
            print("Error: There are no elements to remove")
        else:
            toDel = input("Input the Name of the employee you wish to remove: ")
            del myEmployees[toDel]
    elif option == '3':
        empid = input("Input the employee ID: ")
        employeeName = input("Input the name of the employee: ")
        basicPay = int(input("Input the basic pay of the employee: "))
        allowance = int(input("Input the allowance of the employee: "))
        deductions = int(input("Input the deductions of the employee: "))
        taxes = int(input("Input the taxes of the employee: "))
        netPay = basicPay + allowance
        grossPay = netPay - (deductions + taxes)

        myEmployees.update({empid:
                                {"EmployeeName":{employeeName}, "BasicPay": {basicPay}, "Allowance": {allowance},
                                "Deductions": {deductions}, "Taxes": {taxes}, "NetPay": {netPay}, "GrossPay": {grossPay}}})
    elif option == '4':
        for Employee_Record in myEmployees.items():
            print(Employee_Record)
            print("----------------------")
    elif option == '5':
        break
    else:
        print("Error: Invalid input for choice. Please try again. Choose a number 1 - 5")
