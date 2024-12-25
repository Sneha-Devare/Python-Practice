#1. Definition
#A list is a collection of ordered, mutable, and heterogeneous elements.
#Defined using square brackets [].
#2. Creating Lists
#Empty list: 
my_list = []
#With elements: 
my_list = [1, 2, 3]
#Mixed data types: 
my_list = [1, "hello", 3.14, True]
#3. Accessing Elements
#Indexing:
#Positive index: Starts from 0
(my_list[0])
#Negative index: Starts from -1 
(my_list[-1])
#Slicing:

my_list = [1, 2, 3, 4, 5,"x",10]
print(my_list[1:4])  # [2, 3, 4]
print(my_list[::-1])  # [5, 4, 3, 2, 1] (reverse list)
#4. Modifying Lists
#Mutable: Elements can be changed.

my_list[1] = 10
#5. Adding Elements
#append(): Adds an element to the end.

my_list.append(6)
#insert(): Inserts an element at a specific index.

my_list.insert(1, "new")
#extend(): Combines two lists.

my_list.extend([7, 8])
#6. Removing Elements
#pop(): Removes an element by index and returns it.

my_list.pop(2)
#remove(): Removes the first occurrence of a value.

my_list.remove(10)
#clear(): Removes all elements from the list.

my_list.clear()
#7. List Operations
#Concatenation:
list1=[1,2,3]
list2=[2,5,6]
l=list1 + list2
#Repetition:

list1 * 3
#Membership:

3 in my_list  
# True or False

#8. Common Methods

#sort(): Sorts the list in ascending order.
my_list.sort()

#reverse(): Reverses the list.
my_list.reverse()

#count(): Counts the occurrences of an element.
my_list.count(2)

#index(): Returns the index of the first occurrence of an element.
my_list.index(10)

#9. Iterating Through a List
#Using for Loop:

for item in my_list:
    print(item)

#Using while Loop:

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

#10. List Comprehensions
#Concise way to create lists.

squares = [x**2 for x in range(5)]

#11. Nested Lists
#A list can contain other lists.

nested_list = [[1, 2], [3, 4]]
print(nested_list[0][1])  # 2

#12. Copying Lists
#Shallow Copy:
old_list=[1,6,8]
new_list = old_list[:]

#Using copy():

new_list = old_list.copy()
#13. Length of a List
#Use len() to find the number of elements.

len(my_list)
#14. Deleting Elements
#Using del statement:

del my_list[1]
#15. Advanced Operations
#List slicing:
#my_list[start:end:step]
#Using enumerate():

for index, value in enumerate(my_list):
    print(index, value)
#Zipping lists:

list1 = [1, 2]
list2 = ["a", "b"]
zipped = list(zip(list1, list2))