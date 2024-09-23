# #1
# def calculate_discount(price, discount_percent):
#     # Check if the discount is 20% or higher
#     if discount_percent >= 20:
#         # Calculate the discount
#         discount_amount = price * (discount_percent / 100)
#         # Calculate the final price
#         final_price = price - discount_amount
#         return final_price
#     else:
#         # If discount is less than 20%, return the original price
#         return price
# price = 100
# discount_percent = 10
# final_price = calculate_discount(price, discount_percent)
# print(final_price)  # Output will be 75.0

#2
def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount
        discount_amount = price * (discount_percent / 100)
        # Calculate the final price
        final_price = price - discount_amount
        return final_price
    else:
        # If discount is less than 20%, return the original price
        return price

# Prompt the user for input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(price, discount_percent)

# Check if the price changed and print the appropriate message
if final_price != price:
    print(f"The final price after applying the discount is: ${final_price:.2f}")
else:
    print(f"No discount applied. The original price is: ${price:.2f}")
