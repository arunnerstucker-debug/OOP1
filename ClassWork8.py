#Function calls & function definition
#print() printf() System.out.println()
#
#myList.append("Justus")
#myList.sort()
#myDict.update()
# myList = []
# #def function:
# def addition():
#     myList.append()
# #Main code
# while 1:
#     addition()
#     addition()

def area_rectangle():
    l = int(input("Input the length of the rectangle: "))
    w = int(input("Input the width of the rectangle: "))
    print(f'The area is: {l * w}')

def volume_cube():
    l = int(input("Input the length of the cube: "))
    w = int(input("Input the width of the cube: "))
    h = int(input("Input the height of the cube: "))
    print(f'The area is: {l * w * h}')

def area_circle():
    r = int(input("Input the radius of the circle: "))
    print(f'The area is: {3.14 * r * r}')

def circumference_circle():
    r = int(input("Input the radius of the circle: "))
    print(f'The circumference is: {3.14 * r * 2}')

def volume_sphere():
    r = int(input("Input the radius of the sphere: "))
    print(f'The volume of the sphere is: {(4/3) * 3.14 * r * r * r}')

#Main code
while 1:
    option = input("Choose one of the following:\n"
                   "1. Find the area of a rectangle:\n"
                   "2. Find the volume of a cube:\n"
                   "3. Find the area of a circle:\n"
                   "4. Find the circumference of a circle:\n"
                   "5. Find the volume of a sphere:\n"
                   "6. Quit the program: ")
    if option == '1':
        area_rectangle()
    elif option == '2':
        volume_cube()
    elif option == '3':
        area_circle()
    elif option == '4':
        circumference_circle()
    elif option =='5':
        volume_sphere()
    elif option == '6':
        break
    else:
        print("Error: Invalid input. Please try again.")
