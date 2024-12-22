#if,if-else,if-elif-else

#if
num = 10
if (num > 5):
    print("Number is Greater than 5.")

#if-else
n1 = 2
if (n1 > 5):
    print("Number is Greater than 5.")
else:
    print("Number is Less than 5.")

#number odd or even
number=int(input("Enter Any Number: "))
if (number%2==0):
    print("Number is Even.")
else:
    print("Number is Odd.")

#number positive, negative or zero
num=int(input("Enter Any Number:"))
if (num==0):
    print("Number is Zero.")
elif (num<0):
    print("Number is Negative.")
else:
    print("Number is Positive.")


#You can vote or not
age=int(input("Enter Your Age:"))
if (age>=18):
    print("You are eligible for voting.")
else:
    print("You are not eligible for voting.")


#find the largest of three numbers
a=int(input("Enter num1:"))
b=int(input("Enter num2:"))
c=int(input("Enter num3:"))

if (a>c) and (a>b):
    print("a is greater than b and c.")
elif (b>c) and (b>a):
    print("b is greater than a and c.")
elif(a==c):
    print("a is equal to c.")
elif(a==b):
    print("a is equal to b.")
elif(b==c):
    print("b is equal to c.")
else:
    print("c is greater.")


#check leap year
year=int(input("Enter Year:"))
if (year%4==0 and year%100==0) or (year%400==0):
    print("Year is Leap Year.")
else:
    print("Year is not Leap Year.")


#Create a program to determine if a character is a vowel or consonant
Character=input("Enter Any Character:")
if (len(Character)==1):
    if Character in "aeiouAEIOU":
        print(f"character {Character} is vowel")
    else :
        print(f"character {Character} is consonent.")
else:
    print("Enter Character with only of length one.")


#password strength checker

    