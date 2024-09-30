#!/usr/bin/python3
"""
Purpose: Fruit Store

    Items   price       qty                         amount
    -----------------------------------------------------------
    Apples   12/piece   5 dozens = 5 * 12 = 60      12 * 60
    Mangos   34/piece   3 dozens = 3 * 12 = 36      34 * 36
                                                ---------------
                                                      1944   /-
                                discount     -2 %     - 38.88/-
                                                ---------------
                                                      1905.12/-
                                GST         +12.5 %   +238.14/-
                                                ---------------
                                                      2143.26/-
                                                ---------------

                                                
                                                
   Algorithm
---------                                     

Step 1: Item Details
Step 2: To Convert quantity from dozens to pieces
Step 3: To Calculate the amount for each item
Step 4: To Calculate the total amount
Step 5: To Calculate discount
Step 6: To Calculate GST 
Step 7: To Display the final billable amount
"""

# Item Details
apple_price_per_piece = 12
apple_qty_dozens = 5  # in dozens
mango_price_per_piece = 34
mango_qty_dozens = 3  # in dozens

# To Convert quantity from dozens to pieces
apple_qty_pieces = apple_qty_dozens * 12  # 1 dozen = 12 pieces
mango_qty_pieces = mango_qty_dozens * 12  # 1 dozen = 12 pieces

# To Calculate the amount for each item
apple_amount = apple_price_per_piece * apple_qty_pieces
mango_amount = mango_price_per_piece * mango_qty_pieces

# To Calculate the total amount
total_amount = apple_amount + mango_amount
print("Total Amount  : ", total_amount)

# To calculate discount
discount_percent = 2
discount_amount = (discount_percent / 100) * total_amount
amount_after_discount = total_amount - discount_amount
print("Discount Amount: ", round(discount_amount, 2))

# To calculate GST
gst_percent = 12.5
gst_amount = (gst_percent / 100) * amount_after_discount
final_amount = amount_after_discount + gst_amount
print("GST Amount    : ", round(gst_amount, 2))

# To Display the final billable amount
print("Final Billable Amount: ", round(final_amount, 2))

########################
# constants
DOZEN = 12
DISCOUNT = 2
GST = 12.5


# cost of fruits
cost_of_apple = 12  # per piece
cost_of_mango = 34  # per piece


# Quantities of fruits
qty_of_apples = 5 * DOZEN  # pieces
qty_of_mangos = 3 * DOZEN  # pieces


# Selling Price Computation
total_sp = cost_of_apple * qty_of_apples + cost_of_mango * qty_of_mangos  # PEDMAS
# total_sp =(cost_of_apple * qty_of_apples) + (cost_of_mango * qty_of_mangos)  # PEDMAS
print("Total Selling Price :", total_sp)



# Discount Calculation
discount_amount = (total_sp * DISCOUNT) / 100
print("Discount Amount     :", discount_amount)



# Payable Amount Calculation
payable_amount = total_sp - discount_amount
print("Payable Amount      :", payable_amount)



# GST Calculation
gst_on_fruits = (payable_amount * GST) / 100
print("GST on Fruits       :", gst_on_fruits)


# Billable Amount Calculation
billable_amount = payable_amount + gst_on_fruits
print("Billable Amount     :", billable_amount)


# round(num, no_of_digits) - function
print("Billable Amount(r)  :", round(billable_amount, 2))