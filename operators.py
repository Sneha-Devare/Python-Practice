#1. Operators
#Arithmetic operators (+, -, *, /, %, //, **)
#Comparison operators (==, !=, <, >, <=, >=)
#Logical operators (and, or, not)
#Assignment operators (=, +=, -=, etc.)


#calculator using input for two numbers
n1=float(input("Enter First Number:"))
n2=float(input("Enter Second Number:"))

print("Choose an operation:")
print("1.Addition(+):")
print("2.Subtraction(-):")
print("3.Multiplication(*):")
print("4.Division:(/)")

operation=input("Enter Any Operation From Above:")

if(operation=="1" or operation=="+"):
    print("Addition is :",n1+n2)
elif (operation=="2" or operation=="-"):
    print("Subtraction is :",n1-n2)
elif (operation=="3" or operation=="*"):
    print("Multiplication is :",n1*n2)
elif (operation=="4" or operation=="/"):
    if(n2 !=0):
        print("Division is :",n1/n2)
    else:
        print("Number cannot divisible by 0.")
else:
    print("Choose any valid operation please....")


