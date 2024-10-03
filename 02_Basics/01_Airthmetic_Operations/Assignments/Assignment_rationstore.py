#!/usr/bin/python3
"""
Purpose: Ration Store

    -----------------------------------------------
    item    cost        quantity        Amount
    -----------------------------------------------
    wheat   25/kg       30 kgs      25 * 30 = 750/-
    Rice    12/kg       50 kgs      12 * 50 = 600/-
                                -------------------
                                              1350/-
                                subsidy 20%   -270/-
                                --------------------
                                BillableAmount:1080/-

Algorithm
---------
Step 1:  Get the cost of items into variables
Step 2:  Get the quantity of items into variables
Step 3:  Compute the selling price to each item,
         and add them
Step 4:  Compute the subsidy amount and subtract
         from the selling price
Step 5:  Display the Billable Amount

"""

# Item Details

wheat_cost_per_kg = 25
wheat_quantity = 30
rice_cost_per_kg = 12
rice_quantity = 50

# To Calculate amount for each item
wheat_amount = wheat_cost_per_kg * wheat_quantity
rice_amount = rice_cost_per_kg * rice_quantity

# Calculate total amount
total_amount = wheat_amount + rice_amount
print("Total Amount  : ",total_amount)

# Calculate subsidy and billable amount
subsidy_percent = 20
subsidy_amount = (subsidy_percent / 100) * total_amount
print("subsidy_amount  : ",subsidy_amount)

billable_amount = total_amount - subsidy_amount
print("billable_amount : ",billable_amount)


###################

# cost of Items
cost_of_wheat = 25 # per kg
cost_of_rice = 12 # per kg

# Quantities of Items
qty_of_wheat = 30  # kgs
qty_of_rice = 50  # kgs


# Selling Price Computation
sp_of_wheat = cost_of_wheat * qty_of_wheat
sp_of_rice = cost_of_rice * qty_of_rice

total_sp = sp_of_wheat + sp_of_rice
print("Total Selling Price:", total_sp)

# Subsidy calculation at 20 % subsidy
subsidy_amount  = total_sp * (20/ 100) # PEMDAS
print("Subsidy Amount     :", subsidy_amount)

billable_amount = total_sp - subsidy_amount
print("Billable Amount    :", billable_amount)


