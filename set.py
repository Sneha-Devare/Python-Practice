# Python Set Theory and Code

"""
A set is an unordered collection of unique elements. Unlike lists or tuples, sets do not store duplicate elements and are mutable.
Sets are used to perform mathematical set operations like union, intersection, difference, and symmetric difference.

Properties of Sets:
1. **Unordered:** Sets do not maintain any order for their elements.
2. **Mutable:** Sets are mutable, which means elements can be added or removed.
3. **Unique Elements:** Sets do not allow duplicate elements.
4. **No Indexing, Slicing, or Concatenation:** You cannot access set elements by index.
5. **Heterogeneous:** Sets can contain elements of different data types (but only immutable types like numbers, strings, and tuples).

"""
# Creating a Set
my_set = {1, 2, 3, 4, 5}
empty_set = set()  # You cannot use {} to create an empty set as it creates an empty dictionary
string_set = {"apple", "banana", "cherry"}
mixed_set = {1, "apple", 3.14, (1, 2)}

print("Creating Sets:")
print(my_set)
print(empty_set)
print(string_set)
print(mixed_set)

"""
# Accessing Elements in a Set:

You cannot access elements by index or key as sets are unordered. You must use iteration to access elements.
"""

# Iterating through the set
print("\nIterating Through Set:")
for item in my_set:
    print(item)

"""
# Adding Elements:

You can add elements to a set using the `add()` method.
"""

# Adding an element
my_set.add(6)
print("\nAdding an Element:")
print(my_set)

"""
# Removing Elements:

You can remove elements from a set using the `remove()` method or the `discard()` method. The `remove()` method raises an error if the element is not found, while `discard()` does not.
You can also use the `pop()` method to remove and return an arbitrary element.
"""

# Removing an element
my_set.remove(3)
print("\nRemoving an Element using remove():")
print(my_set)

# Discarding an element (no error if element does not exist)
my_set.discard(10)  # 10 is not in the set
print("\nRemoving an Element using discard():")
print(my_set)

# Popping an arbitrary element
popped_item = my_set.pop()
print("\nPopping an Arbitrary Element:")
print(f"Popped Item: {popped_item}")
print(my_set)

"""
# Set Operations:

Python sets support various set operations that are used to perform mathematical operations on sets.
These operations include union, intersection, difference, and symmetric difference.
"""

# Union of two sets (all elements from both sets)
set2 = {4, 5, 6, 7}
union_set = my_set.union(set2)
print("\nUnion of Two Sets:")
print(union_set)

# Intersection of two sets (common elements)
intersection_set = my_set.intersection(set2)
print("\nIntersection of Two Sets:")
print(intersection_set)

# Difference of two sets (elements in my_set but not in set2)
difference_set = my_set.difference(set2)
print("\nDifference of Two Sets:")
print(difference_set)

# Symmetric Difference of two sets (elements in either set, but not in both)
symmetric_difference_set = my_set.symmetric_difference(set2)
print("\nSymmetric Difference of Two Sets:")
print(symmetric_difference_set)

"""
# Set Methods:

Python sets have a variety of built-in methods that allow you to perform operations on sets. Here are a few common ones:
1. `add()` - Adds an element to the set.
2. `remove()` - Removes an element from the set (raises an error if the element doesn't exist).
3. `discard()` - Removes an element from the set (does not raise an error if the element doesn't exist).
4. `pop()` - Removes and returns an arbitrary element.
5. `clear()` - Removes all elements from the set.
6. `copy()` - Returns a shallow copy of the set.
7. `difference()`, `intersection()`, `union()`, `symmetric_difference()` - Perform set operations.
"""

# Using clear() to remove all items from a set
my_set.clear()
print("\nClearing a Set:")
print(my_set)

# Copying a set
my_set = {1, 2, 3}
copied_set = my_set.copy()
print("\nCopying a Set:")
print(copied_set)

"""
# Set Comprehension:

Set comprehension is a concise way to create a set from an iterable. It is similar to list comprehension but produces a set.
"""

# Set Comprehension
squared_set = {x**2 for x in range(5)}
print("\nSet Comprehension:")
print(squared_set)  # Output: {0, 1, 4, 9, 16}

"""
# Performance:

Sets are generally faster than lists for membership testing. This is because sets are implemented using hash tables.
"""

# Code Block Ends Here
