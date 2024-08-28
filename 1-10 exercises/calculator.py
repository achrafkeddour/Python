import math

print("\n\twelcome to our simple calculator !\n")

num1 = input("please entre your first num : ")
op = input("which operation do you wanna make (+ or - or * or /) : ")
num2 = input("please entre your second num : ")

if bool(num1) and bool(num2) and bool(op):
    num1 = float(num1)
    num2 = float(num2)
    if op == "+":
        result = num1 + num2
        print(f"the result is {round(result,2)}")
    elif op == "-":
        result = num1 - num2
        print(f"the result is {round(result,2)}")
    elif op == "*":
        result = num1 * num2
        print(f"the result is {round(result,2)}")
    elif op == "/":
        result = num1 / num2
        print(f"the result is {round(result,2)}")
    else :
        print("the operator must be + or - or * or / only")

else :
    print("you missed the operator or an number ")

