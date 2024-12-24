#print numbers from 1 to 10
for i in range(1,11):   #with for loop
    print(i)

num=1             #with while loop
while num<=10:
    print(num)
    num+=1

#Print even and odd numbers in a given range
for i in range (1,30):
    if (i%2==0):
        print("even",i)
    elif(i%2!=0):
        print("odd",i)
    num+=1

#Print the sum of numbers from 1 to 20
sum = 0
for i in range(1, 21):
    sum = sum + i
print(sum)


#write a program to reverse any number
number1=int(input("Enter Any Number:"))
for i in number1:
    print(number1.__reversed__)