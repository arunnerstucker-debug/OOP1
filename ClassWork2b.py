number1 = int(input("Enter the value of number1: "))
number2 = int(input("Enter the value of number2: "))
operator =  input("Enter the operator: ")

if operator == "+":
    print("The sum is: ", number1 + number2)
elif operator == "-":
    print("The difference is: ", number1 - number2)
elif operator == "*":
    print("The product is: ", number1 * number2)
elif operator == "/":
    print("The quotient is: ", number1 / number2)
else:
    print("Error invalid operator input.")