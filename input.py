variable=input("Enter Something:")
print("you entered",variable)

#to take integer as input
var2=int(input("Enter only an integer here:"))
print("you entered an integer :",var2)

#to take multiple string inputs at one time
num1,num2=input("Enter any two numbers separated by space: ").split()
print("number 1 is",num1)
print("number 2 is",num2)
print(num1+num2)

#to take multiple integer inputs at one time
a,b=map(int,input("Enter two numbers separated by the space:").split())
print("a:",a)
print("b:",b)
print("a+b:",a+b)


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
    if(num2 !=0):
        print("Division is :",n1/n2)
    else:
        print("Number cannot divisible by 0.")
else:
    print("Choose any valid operation please....")


