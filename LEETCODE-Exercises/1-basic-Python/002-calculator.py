firstNumber = float(input("Enter the first number: "))
secondNumber = float(input("Enter the second number: "))
enterOperation = input("Enter the Operation you want to calculate :))))) : ")


if enterOperation == "+":
    print("The sum is : ", firstNumber + secondNumber)
elif enterOperation == "=":
    print("The difference is : ", firstNumber - secondNumber)
elif enterOperation == "*":
    print("The product is : ", firstNumber * secondNumber)

elif enterOperation == "/":
    if secondNumber == 0:
        print("can not possible to calculate")
    else:
        print("The division is : ", firstNumber / secondNumber)

elif enterOperation == "%":
    if secondNumber == 0:
        print("can not possible to calculate")
    else:
        print("The remainder is : ", firstNumber % secondNumber)

else:
    print("Invalid operation")
