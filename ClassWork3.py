#Looping statements
#for
#while (condition):
#for variable in range(initial, <n, stepwise):
#for number in range(1,20):
#   if number%2 == 0:
 #      print("The number ", number, " is even.")
 #  else:
 #       print("The number ", number, "is odd.")

#number = int(input("Input the number you wish to find the multiplication table of."))
#for i in range(1,11):
#    print(i, " * ", number, " = ", i*number)

#number = int(input("Input the number you wish to be the max of the multiplication table"))
#for i in range(1,number):
 #   for n in range(1, number):
 #       print(i, " * ", n, " = ", i*n)

p = int(input("Principle: "))
n = int(input("Number of months: "))
R = int(input("Rate: "))

r = R/ (12*100)
EMI = p * r * ((1+r)**n)/((1+r)**n - 1)
Balance = p - EMI

for month in range(1, n+1):
    print("EMI: ", EMI)
    print("Balance: ", Balance)
    print("------")
    Balance = Balance - EMI

