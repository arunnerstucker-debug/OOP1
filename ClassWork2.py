#Condtional Statements
#if <condition>:
#   print(...
#   block of statements
#elif <opposing condition>:
#   print(...
#else:
#   print(...

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
if a > b and a > c:
    print("a is the greatest")
elif b > c:
    print("b is the greatest")
elif a == b and b == c:
    print("They are equal")
else:
    print("c is the greatest")