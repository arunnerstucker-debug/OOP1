# list.append()
# list.remove() or list.pop()
#
# dictionary.update("sid":
#                         {"name":
#
#                         })
#del
# dictionary[s1].update("name":"newname")
#dictionary[s1]["name"] = "Justus"
#for n in dictionary.items():
#   print(n.items())

#initialize empty lists before dictionary
mang = []
tech = []
team = []
Projects = {}
while True:

    option = input("Choose one of the following options\n"
                    "1. Project initialization\n"
                    "2. Project Closure\n"
                    "3. Print all Projects\n"
                    "4. Quit Application: ")

    if option == '1':
        PID = input("Input the Project ID: ")
        projectTitle = input("Input the Project Title: ")
        n = int(input("Enter the number of Managers you wish to enter: "))
        for i in range(0, n):
            MName = input("Input the name of the Manager: ")
            mang.append(MName)
        sDate = input("Input the Start Date of the Project: ")
        eDate = input("Input the End Date of the Project: ")
        spons = input("Input the Name of the Sponsor for the Project: ")
        budget = input("Input the budget of the Project: ")
        n1 = int(input("Enter the number of Technologies you wish to enter: "))
        for i in range(0, n1):
            TName = input("Input the name of the Technology: ")
            tech.append(TName)
        n2 = int(input("Enter the number of Team Members you wish to enter: "))
        for i in range(0, n1):
            TMName = input("Input the name of the Team Member: ")
            team.append(TMName)

        Projects.update({PID:
                    {"Project Title": projectTitle, "Manager(s)": mang, "Start Date": sDate, "End Date": eDate,
                     "Sponsor": spons, "Budget": budget, "technologies": tech, "Team member(s)": team}})
    elif option == '2':
        if len(Projects) == 0:
            print("Error: No elements in the Dictionary")
        else:
            toDel = input("Input the Project ID of the project you wish to terminate: ")
            del Projects[toDel]
    elif option == '3':
        for i in Projects.items():
            print(i)
            print("--------------------")
    elif option == '4':
        break
    else:
        print("Error: Please reenter choice.")