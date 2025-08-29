student_name = input("Enter the student's name: ")
course1 = int(input("Enter the grade for course1: "))
course2 = int(input("Enter the grade for course2: "))
course3 = int(input("Enter the grade for course3: "))
course4 = int(input("Enter the grade for course4: "))
course5 = int(input("Enter the grade for course5: "))

total = course1 + course2 + course3 + course4 + course5
print("Your total points is: ", total)

average = total/5
print("Your average score is: ", average)

wages = int(input("Enter the wages: "))
hours = int(input("Enter the hours: "))
days = int(input("Enter the days: "))
monthly_wages = wages*hours*days
print(monthly_wages)