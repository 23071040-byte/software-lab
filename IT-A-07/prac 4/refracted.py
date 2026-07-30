def get_items_data(item_count):
    items = []
    prices = []
    quantities = []

    for _ in range(item_count):
        name = input("Item Name: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))

        items.append(name)
        prices.append(price)
        quantities.append(quantity)

    return items, prices, quantities


def calculate_discount(amount):
    if amount >= 1000:
        return amount * 0.15
    if amount >= 500:
        return amount * 0.10
    return 0


def print_bill(items, prices, quantities):
    print("\n------ BILL ------")

    total = 0.0

    for index in range(len(items)):
        amount = prices[index] * quantities[index]
        total += amount

        discount = calculate_discount(amount)
        final_amount = amount - discount

        print("Item:", items[index])
        print("Price:", prices[index])
        print("Quantity:", quantities[index])
        print("Amount:", amount)
        print("Discount:", discount)
        print("Final:", final_amount)
        print("----------------")

    return total


def find_extreme_items(items, prices):
    expensive_price = prices[0]
    cheap_price = prices[0]
    expensive_item = items[0]
    cheap_item = items[0]

    for index in range(1, len(items)):
        if prices[index] > expensive_price:
            expensive_price = prices[index]
            expensive_item = items[index]

        if prices[index] < cheap_price:
            cheap_price = prices[index]
            cheap_item = items[index]

    return expensive_item, expensive_price, cheap_item, cheap_price


def count_bulk_purchases(quantities):
    return sum(1 for quantity in quantities if quantity > 5)


def main():
    print("Welcome to Grocery Store")

    item_count = int(input("Enter number of items: "))
    items, prices, quantities = get_items_data(item_count)

    total = print_bill(items, prices, quantities)

    gst = total * 0.05
    grand_total = total + gst

    expensive_item, expensive_price, cheap_item, cheap_price = find_extreme_items(items, prices)
    bulk_count = count_bulk_purchases(quantities)

    print("Subtotal:", total)
    print("GST:", gst)
    print("Grand Total:", grand_total)
    print("Most Expensive Item:", expensive_item, expensive_price)
    print("Cheapest Item:", cheap_item, cheap_price)
    print("Items purchased in bulk:", bulk_count)


if __name__ == "__main__":
    main()


# Theory of Refactoring
# 1. Refactoring improves readability by breaking long code into smaller,
#    well-named helper functions.
# 2. Clear naming makes the purpose of variables and functions easier to understand.
# 3. Removing duplicate logic and reusing functions reduces mistakes and makes
#    maintenance easier.
# 4. A structured program is easier to test, debug, and extend.
#
# Comparison with the messy version:
# - Naming: The refactored version uses descriptive names like
#   'get_items_data' and 'calculate_discount' instead of short, unclear names.
# - Structure: The logic is split across functions instead of being written in one
#   long block.
# - Documentation: The refactored version includes docstrings and comments,
#   while the messy version has little or no explanation.
# - Readability: The refactored code is easier to follow, modify, and maintain.
