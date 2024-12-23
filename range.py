#range function in python
#The range() function is used to generate a sequence of numbers. It's commonly used in loops like for loops. You can specify the start, stop, and step values.

r = range(5)
print(r)  # Output: range(0, 5)

r = range(5)  # 0 to 4
print(list(r))

for i in range(5):
    print(i)


#print only odd numbers
for i in range(1,30,2):
    print(i)

#print even numbers
for i in range(0,30,2):
    print(i)


#counting backwards
for i in range(20,0,-1):
    print(i)
print("\n")

for i in range(20,0,-2):
    print(i)
print("\n")

r = range(5, 15, 3)  # Start at 5, increment by 3
for i in r:
    print(i)

#converting range to iterative items like list,tuple
r = range(5,10)
print(list(r))  #convert to list
print(tuple(r))  #convert to tuple
print("\n")


#the underscore is used when you not want to use variables
for _ in range(1,6):
    print("sneha")

#The start value is inclusive (part of the range).
#The stop value is exclusive (not part of the range).

#access indices in list
my_list = ["a", "b", "c"]
for i in range(len(my_list)):
    print(f"Index {i} has value {my_list[i]}")

#printing stars
for i in range(1,7):
    print("*"*i)
print("\n")

#print all numbers of 50 to 100
for numbers in range(50,101):
    print(numbers)
print("\n")


#print all multiples of 3 from (0 to 30)
for num in range(3,30,3):
    print(num)

#print countdown from 20 to 0
for i in range(20,-1,-1):
    print(i)
print("\n")

#Create a list of squares (e.g., [1, 4, 9, 16, 25]) for numbers 1 to 5 using range
for i in range(1,6):
    print(list(i*i))

    