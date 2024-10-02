#!/usr/bin/python
"""
Purpose: Operator precedence in python

    Python Execution Flow:
        left to right, and top to bottom

    It follows PEMDAS rule, and execution flow
        P - Paranthesis
        E - Exponent
        M - Multiplication
        D - Division
        A - Addition
        S - Subtraction

    Every type of braces has importance in python
    {}  - used for dictionaries and sets
    []  - used for lists
    ()  - used of tuples; also used in arithmetic operations
"""

result = (22 + 2 / 2 * 4 // 4 - 89) + 67 - 10e7
# result = (22 + 2 / 8 // 4 - 89) + 67 - 10e7
print(result)

expression = 40 / 2
print(result)   

expression = 40 / 2 / 2
print(result)    #  Python evaluates the division from left to right.The first operation that takes place is 40 / 2, which equals 20. Then the second operation is 20 / 2, which equals 10.

expression = 120 / 3 / 4
print(result)  # The first operation is 120 / 3, which equals 40. Then, the second operation is 40 / 4, which equals 10.


expression = 120 / 4 / 3
print(result)   #   First, 120 / 4 is calculated, which equals 30. Then, 30 / 3 is calculated, which equals 10.

expression = 120 / 3 / 4 / 10
print(result)   
# First, 120 / 3 is calculated, which equals 40 - Then, 40 / 4 is calculated, which equals 10 - Finally, 10 / 10 is calculated, which equals 1


expression = 40 / 10 // 3.0
print(result)    # First, 40 / 10 is calculated, which equals 4.0 (since / always results in a float). 
                 # Next, 4.0 // 3.0 is performed. The // operator performs floor division, meaning it returns the largest integer less than or equal to the result. 
                 # In this case, 4.0 // 3.0 equals 1.0.


expression = 40 // 10 / 3.0
print(result)     # First, 40 // 10 is calculated. The // operator performs floor division, so 40 // 10 equals 4 (an integer) Next, 4 / 3.0 is performed.
                  # The / operator performs floating-point division, so 4 / 3.0 equals 1.3333333333333333.


expression = 40 / 10 // 3.0  # + 23e45 - 23 + 56 * 67
print(result)

result = (True == False) in (False,) == False
print(result)