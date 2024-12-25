# Python Tuple Theory and Code

"""
A tuple is a collection of ordered, immutable elements. Tuples are similar to lists, 
but unlike lists, tuples are immutable, meaning that their elements cannot be changed 
after creation.

Properties of Tuples:
1. **Ordered:** The elements in a tuple are stored in a defined order, and this order will not change.
2. **Immutable:** Once a tuple is created, its contents cannot be changed, added, or removed.
3. **Indexed:** You can access elements of a tuple using indices (starting from 0).
4. **Can contain multiple data types:** A tuple can store different data types such as integers, floats, strings, lists, and even other tuples.
5. **Allow duplicates:** Tuples can have duplicate elements.

# Tuple Creation:

Tuples can be created using parentheses `()` or without them (comma separated values).
"""

# Creating Tuples
my_tuple = (1, 2, 3, "apple", 5.6)
single_element_tuple = (4,)  # A tuple with a single element requires a comma after the element
empty_tuple = ()  # An empty tuple
tuple_no_parentheses = 1, 2, 3, "banana"  # Tuple can be created without parentheses

print("Tuple Creation:")
print(my_tuple)
print(single_element_tuple)
print(empty_tuple)
print(tuple_no_parentheses)

"""
# Accessing Tuple Elements:

Elements of a tuple can be accessed by using indexing, where the first element has index 0.
Negative indexing starts from -1 for the last element of the tuple.
"""

# Accessing Tuple Elements
print("\nAccessing Elements:")
print(my_tuple[0])  # Output: 1
print(my_tuple[3])  # Output: apple
print(my_tuple[-1])  # Output: 5.6  (Negative index starts from -1 for the last element)

"""
# Slicing Tuples:

Tuples can be sliced just like lists to extract a part of the tuple. 
Slicing is done using the syntax: tuple[start:stop:step]
"""

# Slicing Tuples
print("\nSlicing Tuples:")
print(my_tuple[1:4])  # Output: (2, 3, 'apple')  (Slices from index 1 to index 3)
print(my_tuple[::2])  # Output: (1, 3, 5.6)  (Every second element starting from the first)

"""
# Concatenating and Repeating Tuples:

You can concatenate two tuples using the `+` operator and repeat a tuple using the `*` operator.
"""

# Concatenating and Repeating Tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5)
combined_tuple = tuple1 + tuple2
repeated_tuple = (1, 2) * 3
print("\nConcatenating and Repeating Tuples:")
print(combined_tuple)  # Output: (1, 2, 3, 4, 5)
print(repeated_tuple)  # Output: (1, 2, 1, 2, 1, 2)

"""
# Tuple Length:

You can find the length of a tuple (the number of elements) using the built-in function `len()`.
"""

# Tuple Length
print("\nTuple Length:")
print(len(my_tuple))  # Output: 5

"""
# Checking Membership:

You can check whether a specific element exists in a tuple using the `in` keyword.
"""

# Checking Membership
print("\nChecking Membership:")
print(3 in my_tuple)  # Output: True
print("orange" in my_tuple)  # Output: False

"""
# Iterating Through a Tuple:

You can loop through all the elements of a tuple using a `for` loop.
"""

# Iterating Through a Tuple
print("\nIterating Through a Tuple:")
for item in my_tuple:
    print(item)

"""
# Nested Tuples:

Tuples can also contain other tuples as elements, creating a nested structure.
"""

# Nested Tuples
nested_tuple = (1, 2, (3, 4), "apple")
print("\nNested Tuples:")
print(nested_tuple[2])  # Output: (3, 4)  (Accessing nested tuple)
print(nested_tuple[2][1])  # Output: 4  (Accessing an element within the nested tuple)

"""
# Tuple Unpacking:

You can unpack a tuple into individual variables, which allows you to assign each element of a tuple to a separate variable.
"""

# Corrected Tuple Unpacking (matching the number of elements with the variables)
print("\nTuple Unpacking:")
a, b, c, d, e = my_tuple  # Now matches the number of elements in my_tuple (5 elements)
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
print(d)  # Output: apple
print(e)  # Output: 5.6

# Tuple Unpacking with a wildcard (*rest) for extra values
print("\nTuple Unpacking with Rest:")
a, b, *rest = my_tuple  # The *rest catches all remaining elements into a list
print(a)  # Output: 1
print(b)  # Output: 2
print(rest)  # Output: [3, 'apple', 5.6]

"""
# Tuple Methods:

Tuples support two built-in methods:
1. `count()` - Returns the number of times an element appears in the tuple.
2. `index()` - Returns the index of the first occurrence of a specified element.
"""

# Tuple Methods
print("\nTuple Methods:")
print(my_tuple.count(2))  # Output: 1  (Number of times 2 appears)
print(my_tuple.index(3))  # Output: 2  (Index of the first occurrence of 3)

"""
# Converting Other Data Types to Tuples:

You can convert other data types like lists and strings into tuples using the `tuple()` function.
"""

# Converting List to Tuple
my_list = [1, 2, 3]
my_tuple_from_list = tuple(my_list)
print("\nConverting List to Tuple:")
print(my_tuple_from_list)  # Output: (1, 2, 3)

# Converting String to Tuple
string = "apple"
my_tuple_from_string = tuple(string)
print("\nConverting String to Tuple:")
print(my_tuple_from_string)  # Output: ('a', 'p', 'p', 'l', 'e')

"""
# Immutability of Tuples:

Tuples are immutable, meaning their elements cannot be changed after creation. 
If you try to modify a tuple, you will get a `TypeError`.
"""

# Uncommenting the line below will raise an error:
# my_tuple[1] = 4  # TypeError: 'tuple' object does not support item assignment

"""
# Performance:

Tuples are faster than lists in terms of iteration and element access because of their immutability. 
They also use less memory and can be used as keys in dictionaries (lists cannot).
"""

# Code Block Ends Here
