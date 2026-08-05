def get_non_empty_text(prompt):
    # TODO: Keep asking until the user enters non-empty text.
    pass


def get_valid_integer(prompt):
    # TODO: Keep asking until the user enters a valid integer.
    pass


def get_valid_float(prompt):
    # TODO: Keep asking until the user enters a valid float.
    pass


def calculate_order_total(quantity, unit_price, discount_percent):
    # TODO: Calculate subtotal, apply discount, and return final total.
    pass


def format_summary(customer_name, quantity, unit_price, discount_percent, total):
    # TODO: Return a formatted multi-line summary string.
    pass


def main():
    print("Order Calculator")
    print("----------------")

    # TODO: Use validation helpers for all inputs.
    customer_name = get_non_empty_text("Customer name: ")
    quantity = get_valid_integer("Quantity: ")
    unit_price = get_valid_float("Unit price: ")
    discount_percent = get_valid_float("Discount (%): ")

    # TODO: Validate ranges before calculation.
    total = calculate_order_total(quantity, unit_price, discount_percent)
    summary = format_summary(customer_name, quantity, unit_price, discount_percent, total)

    print()
    print(summary)


if __name__ == "__main__":
    main()
