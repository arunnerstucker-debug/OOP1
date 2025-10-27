#Processor
#Memory
#In/Output
#RAM - helps processor to execute values
#Permanent storage??? Files & Databases
#Files:
# in_s = open("test1.txt", "w") # opens or creates test1.txt, w = input file (write only).
# in_s.writelines("Hello World!\n")
# in_s.writelines("Welcome to the OOP Class!\n")
# in_s.writelines("Hope you are enjoying it!\n")
# in_s.close() # so you can use it elsewhere afterwords.
#
# a_s = open("test1.txt", "a") # "a" = append only mode.
# a_s.writelines("Hello World!\n")
# a_s.writelines("Welcome to the OOP Class!\n")
# a_s.writelines("Hope you are enjoying it!\n")
# a_s.close()
#
# out_s = open("test1.txt", "r") # read (output) only mode.
# for line in out_s:
#    print(line)
#
# out_s.close()

import pickle
# d = {"stu1": {"Name":"John", "Age":"21", "ID": 28},
#       "stu2": {"Name":"Bob", "Age":"99", "ID": 28},
#       "stu3": {"Name":"Js", "Age":"70", "ID": 28}}
#
# with open("students.dat", "wb") as file1: #wb = write binary
#     pickle.dump(d, file1)
#     file1.close()
#
# with open("students.dat", "rb") as file2: #rb = read binary
#     myDictionary = pickle.load(file2)
#
# print(myDictionary["stu1"]["Name"])
# i = 1
# for x in myDictionary:
#     var = "stu" + str(i)
#     print(myDictionary[var]["Name"])
#     i+=1
#
# file2.close()

# create a file of user credentials in a dictionary, follow the path in the dictionary to evaluate if pwd is true??

users = {
        "usr1":{"uid": "jselwyn", "pwd":"123"},
        "usr2":{"uid": "bjoe", "pwd":"321"},
        "usr3":{"uid": "jbilly", "pwd":"567"},
        "usr4":{"uid": "mjim", "pwd":"877"}}
with open("users.dat", "wb") as filea:
    pickle.dump(users, filea)
    filea.close()

with open("users.dat", "rb") as fileb:
    user_dict = pickle.load(fileb)

#get username and pass

username = input("Input you UID here: ")
password = input("Input your password here: ")

b = 0
n = 1
for x in user_dict:
    var = "usr" + str(n)
    if user_dict[var]["uid"] == username and user_dict[var]["pwd"] == password:
        print("Login successful")
        b+= 1
        break
if b == 0:
    print("Login Unsuccessful")






