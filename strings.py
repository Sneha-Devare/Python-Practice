# String in Python

# A string is a sequence of characters enclosed in quotes, either single quotes (' ') or double quotes (" ").
# In Python, strings are immutable, which means once they are created, their content cannot be changed.

# Syntax:
# Strings can be created using single quotes, double quotes, or triple quotes for multi-line strings.
# Example:
my_string = "Hello, World!"
another_string = 'Python is awesome!'
multi_line_string = """This is a
multi-line
string."""

# String Characteristics:
# 1. Immutable: The content of a string cannot be modified after it is created.
# 2. Ordered: Strings maintain the order of characters.
# 3. Iterable: Strings can be iterated over character by character.
# 4. Support indexing and slicing.

# String Operations:
# 1. Concatenation: Joining two strings together using the `+` operator.
string1 = "Hello"
string2 = "World"
greeting = string1 + " " + string2  # Output: "Hello World"

# 2. Repetition: Repeating a string multiple times using the `*` operator.
repeated_string = "Python " * 3  # Output: "Python Python Python "

# 3. Membership Testing: Using `in` to check if a substring exists in a string.
print("Python" in "Python programming")  # Output: True

# 4. Indexing: Accessing individual characters using indices (starting from 0).
print(greeting[0])  # Output: "H"
print(greeting[-1])  # Output: "d" (negative indexing starts from the end)

# 5. Slicing: Extracting a part of the string using `:` syntax.
print(greeting[0:5])  # Output: "Hello"
print(greeting[:5])   # Output: "Hello"
print(greeting[6:])   # Output: "World"
print(greeting[::2])  # Output: "Hoo"

# Modifying Strings:
# Strings are immutable, so we cannot modify a string directly.
# However, we can create a new string based on the modification.

# Converting Strings:
# 1. `lower()`: Converts all characters to lowercase.
print("HELLO".lower())  # Output: "hello"

# 2. `upper()`: Converts all characters to uppercase.
print("hello".upper())  # Output: "HELLO"

# 3. `capitalize()`: Capitalizes the first letter of the string.
print("hello".capitalize())  # Output: "Hello"

# 4. `title()`: Capitalizes the first letter of each word.
print("hello world".title())  # Output: "Hello World"

# 5. `swapcase()`: Swaps the case of each character (lower to upper and vice versa).
print("Hello World".swapcase())  # Output: "hELLO wORLD"

# 6. `strip()`: Removes leading and trailing whitespace from the string.
print("  Hello World  ".strip())  # Output: "Hello World"

# 7. `replace()`: Replaces a substring with another substring.
print("Hello World".replace("World", "Python"))  # Output: "Hello Python"

# 8. `split()`: Splits a string into a list based on a delimiter (default is space).
words = "Hello World".split()  # Output: ['Hello', 'World']

# String Methods:
# 1. `find()`: Returns the index of the first occurrence of a substring (returns -1 if not found).
print("Hello World".find("World"))  # Output: 6

# 2. `count()`: Returns the number of occurrences of a substring in the string.
print("Hello World".count("o"))  # Output: 2

# 3. `startswith()`: Checks if the string starts with a given substring.
print("Hello World".startswith("Hello"))  # Output: True

# 4. `endswith()`: Checks if the string ends with a given substring.
print("Hello World".endswith("World"))  # Output: True

# 5. `join()`: Joins elements of an iterable with the string as a separator.
separator = "-"
joined_string = separator.join(["Python", "is", "awesome"])  # Output: "Python-is-awesome"

# 6. `isalpha()`: Checks if all characters in the string are alphabetic.
print("Hello".isalpha())  # Output: True

# 7. `isdigit()`: Checks if all characters in the string are digits.
print("12345".isdigit())  # Output: True

# 8. `isspace()`: Checks if the string contains only whitespace characters.
print("   ".isspace())  # Output: True

# String Formatting:
# 1. Using `+` for concatenation:
name = "John"
age = 30
formatted_string = "My name is " + name + " and I am " + str(age) + " years old."
print(formatted_string)  # Output: "My name is John and I am 30 years old."

# 2. Using f-strings (Python 3.6+):
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)  # Output: "My name is John and I am 30 years old."

# 3. Using `format()` method:
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)  # Output: "My name is John and I am 30 years old."

# Multiline Strings:
# Multiline strings can be created using triple quotes (single or double).
multi_line_string = """This is a string
that spans across
multiple lines."""
print(multi_line_string)

# Escape Characters:
# 1. `\n`: Newline
# 2. `\t`: Tab
# 3. `\\`: Backslash
# 4. `\'`: Single quote
# 5. `\"`: Double quote

escaped_string = "Hello\nWorld\tPython"
print(escaped_string)
# Output:
# Hello
# World   Python

# Conclusion:
# Strings are one of the most commonly used data types in Python.
# They are immutable, ordered, and support many operations and methods for manipulation.
# Mastery of strings is essential for text processing, formatting, and manipulation in Python.
