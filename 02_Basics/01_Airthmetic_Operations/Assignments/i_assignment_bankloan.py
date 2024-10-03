#!/usr/bin/python3
"""
Purpose: Bank Loan

    Simple Interest : A = P (1 + rt)

                        A	=	final amount
                        P	=	initial principal balance
                        r	=	annual interest rate
                        t	=	time (in years)

Ref :https://www.calculatorsoup.com/calculators/financial/simple-interest-plus-principal-calculator.php

Get all values in runtime
Algorithm
---------
Step 1: Get the principal amount (P), annual interest rate (r), and time in years (t) from the user.
Step 2: Calculate the simple interest
Step 3: Calculate the compound interest
Step 4: Display both the final amounts for simple and compound interest.
"""


# Step 1: Get the principal amount, interest rate, and time from the user
P = float(input("Enter the principal amount (P): "))
r = float(input("Enter the annual interest rate (r) in decimal (e.g., 0.05 for 5%): "))
t = float(input("Enter the time (t) in years: "))

# Step 2: Calculate Simple Interest
A_simple = P * (1 + r * t)
print("Simple Interest Final Amount (A): %.2f" % A_simple)

# Step 3: Get number of times interest is compounded per year for compound interest
n = int(input("Enter the number of times the interest is compounded per year (n): "))

# Calculate Compound Interest
A_compound = P * (1 + r / n) ** (n * t)
print("Compound Interest Final Amount (A): %.2f" % A_compound)
