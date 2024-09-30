#!/usr/bin/python3
"""
Purpose: Feet to centimetres conversion

    1 foot = 12 inches
    1 inch = 2.54 centimetres

Algorithm:
----------
Step 1: Get feet values in runtime
Step 2: Compute from feet to cms
            feet to inches, then
            inches to centimeters conversion
Step 3: Display the results
"""

# Step 1: Get feet values in runtime
feet = float(input("Enter the value in feet: "))

# Step 2: Convert feet to inches, then inches to centimeters
inches = feet * 12  # 1 foot = 12 inches
centimeters = inches * 2.54  # 1 inch = 2.54 centimeters

# Step 3: Display the results
print("Value in feet: ", feet)
print("Value in inches: %.2f" % inches)
print("Value in centimeters: %.2f" % centimeters)
