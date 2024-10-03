#!/usr/bin/python3
"""
Purpose: Demonstration of Palindrome check

    palindrome strings
        dad
        mom

Algorithms:
-----------
Step 1: Take the string in run-time and store in a variable


"""

# To Take the string in run-time and store in a variable
input_string = input("Enter a string to check if it is a palindrome: ")

# To Print the result directly using a ternary expression
print(f"'{input_string}' is a palindrome." if input_string == input_string[::-1] else f"'{input_string}' is not a palindrome.")