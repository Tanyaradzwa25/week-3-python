
def calculate_discount(price, discount_percent):
    """Calculate the final price after applying a discount."""
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
    else:
        final_price = price
    return final_price


original_price = 1000.00
discount_percent = 20

final_price = calculate_discount(original_price, discount_percent)
print(f"Original Price: R{original_price:.2f}")
print(f"Discount Percent: {discount_percent}%")
print(f"Final Price: R{final_price:.2f}")


def main():
    # Prompt user for input
    try:
        price = float(input("Enter the original price of the item: R"))
        discount_percent = float(input("Enter the discount percentage: "))
        
        # Validate inputs
        #if price < 0 or discount_percent < 0:
        if price > 800 or discount_percent > 20:
            print("Price and discount percentage must be non-negative values.")
            return

        # Calculate and print the final price
        final_price = calculate_discount(price, discount_percent)
        print(f"The final price is: R{final_price:.2f}")
        
    except ValueError:
        print("Invalid input. Please enter numerical values for price and discount percentage.")

if __name__ == "__main__":
    main()

