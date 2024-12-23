#1.Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5
for number in range(0,100):
    if(number%7==0 and number%5!=0):
        print(number)


#reversed string without using built in function
def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

input_string = "Sneha"
print("Original String:", input_string)
print("Reversed String:", reverse_string(input_string))


#2.Rotate the elements of a list (e.g., [1,2,3,4] becomes [4,1,2,3])
def rotate_list(lst):
    if not lst:  
        return lst
    last_element = lst[-1]  
    rotated_list = [last_element] + lst[:-1]  
    return rotated_list

input_list = [1, 2, 3, 4]
print("Original List:", input_list)
print("Rotated List:", rotate_list(input_list))


#1. Generate the Fibonacci sequence up to n terms.
def fibonacci_sequence(n):
    if n <= 0:
        return []  # Return an empty list for non-positive input
    elif n == 1:
        return [0]  # The first Fibonacci term is 0
    elif n == 2:
        return [0, 1]  # The first two Fibonacci terms are 0 and 1
    
    # Start the sequence with the first two terms
    fib_sequence = [0, 1]
    for i in range(2, n):
        # Add the sum of the last two terms to the sequence
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    return fib_sequence

# Example usage
n = 10  # Change this value for different numbers of terms
print("Fibonacci sequence up to", n, "terms:", fibonacci_sequence(n))


