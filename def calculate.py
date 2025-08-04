def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.

    Args:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage.

    Returns:
        float: The final price after the discount, or the original price if no discount is applied.
    """
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Calculate the final price
        final_price = price - discount_amount
        return final_price
    else:
        # If the discount is less than 20%, return the original price
        return price

# --- Main program logic ---
# Use a try-except block to handle cases where the user might not enter a valid number.
try:
    # Prompt the user for the original price and convert it to a float
    original_price = float(input("Enter the original price of the item: "))
    
    # Prompt the user for the discount percentage and convert it to a float
    discount_percentage = float(input("Enter the discount percentage: "))

    # Call the calculate_discount function with the user's input
    final_price = calculate_discount(original_price, discount_percentage)

    # Print the result to the user
    # We check if the final price is less than the original price to determine if a discount was applied.
    if final_price < original_price:
        print(f"\nFinal price after a {discount_percentage}% discount: ₦{final_price:.2f}")
    else:
        print(f"\nNo discount was applied because the discount was less than 20%.")
        print(f"The original price remains: ₦{original_price:.2f}")

except ValueError:
    print("\nError: Please enter valid numerical values for the price and discount.")