# 📘 Assignment: Python Refactoring and Input Validation

## 🎯 Objective

Refactor a small Python program into clear, reusable functions and handle user input safely with validation. In this assignment, you will practice writing cleaner code structure and preventing common runtime errors.

## 📝 Tasks

### 🛠️ Extract Reusable Functions

#### Descrição
You will receive starter code for an order summary calculator. Reorganize the logic into small functions so the program is easier to read, test, and maintain.

#### Requisitos
O programa concluído deve:

- Implement `calculate_order_total(quantity, unit_price, discount_percent)` to return the final total after discount.
- Implement `format_summary(customer_name, quantity, unit_price, discount_percent, total)` to return a readable, multi-line summary string.
- Keep `main()` as the orchestration point that calls helper functions instead of duplicating logic.
- Print the final summary exactly once at the end of execution.

### 🛠️ Validate User Input Safely

#### Descrição
Improve program reliability by validating user input before performing calculations.

#### Requisitos
O programa concluído deve:

- Implement `get_non_empty_text(prompt)` to reject blank names.
- Implement `get_valid_integer(prompt)` to accept only valid integers and retry on invalid input.
- Implement `get_valid_float(prompt)` to accept only valid decimal numbers and retry on invalid input.
- Reject invalid ranges: quantity must be greater than 0, unit price must be greater than 0, and discount must stay between 0 and 100.
- Show a clear error message and ask again whenever input is invalid.

Exemplo de interacao esperada:

```text
Customer name: Ana
Quantity: two
Invalid input. Please enter a whole number.
Quantity: 3
Unit price: 25
Discount (%): 10

Order Summary
-------------
Customer: Ana
Quantity: 3
Unit price: $25.00
Discount: 10.0%
Total: $67.50
```
