#!/usr/bin/python3
"""
Purpose: Saving Bank

    Initial Balance 0

Algorithm
----------
Step 1: Create an variable 'balance' with initial value 0
Step 2: Initial Despoit of min balance 1500
Step 3: Salary credited of 3300
Step 4: Online Purchase of 33.33
Step 5: House Rent paid of 1500
Step 6: Display Balance
"""

# Step 1: Create a variable 'balance' with initial value 0
balance = 0
print("Initial Balance:", balance)

# Step 2: Initial Deposit of minimum balance 1500
initial_deposit = 1500
balance += initial_deposit
print("After Initial Deposit of 1500: Balance =", balance)

# Step 3: Salary credited of 3300
salary = 3300
balance += salary
print("After Salary Credited of 3300: Balance =", balance)

# Step 4: Online Purchase of 33.33
online_purchase = 33.33
balance -= online_purchase
print("After Online Purchase of 33.33: Balance =", balance)

# Step 5: House Rent paid of 1500
house_rent = 1500
balance -= house_rent
print("After House Rent Paid of 1500: Balance =", balance)

# Step 6: Display the final balance
print("Final Balance:", balance)
