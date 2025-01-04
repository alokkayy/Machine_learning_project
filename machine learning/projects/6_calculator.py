try:
    num1 = int(input("Enter the 1st number: "))
    num2 = int(input("enter the 2nd number: "))
    operator = input("Enter the operator you want to work with (+, -, *, /, //) ")
    if operator == "+":
        print(num1+num2)
    elif operator == "-":
        print(num1-num2)
    elif operator == "*":
        print(num1*num2)
    elif operator == "/":
        print(num1/ num2)
    elif operator == "//":
        print(num1 // num2)
    else:
        print("its is a wrong operator or out of my reach! ")
except ValueError:
    print("U need to provide a number")
except ZeroDivisionError:
    print("you cannot have 0 in the denominator")
except Exception as e:
    print("Error is :- ",e)