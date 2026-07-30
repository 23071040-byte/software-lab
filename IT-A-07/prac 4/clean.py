"""Clean and refactored grocery store billing program."""


def get_items_data(item_count):
    """Collect item names, prices, and quantities from the user."""
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
    """Return the discount for a given item amount."""
    if amount >= 1000:
        return amount * 0.15
    if amount >= 500:
        return amount * 0.10
    return 0


def print_bill(items, prices, quantities):
    """Print the bill for each item and return the subtotal."""
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
    """Find the most expensive and cheapest items."""
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
    """Count how many items were purchased in bulk."""
    return sum(1 for quantity in quantities if quantity > 5)


def run_grocery_store_program(item_count):
    """Run the full grocery store billing workflow for the given item count."""
    print("Welcome to Grocery Store")

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


def run_with_sample_input():
    """Run the program with the same item count used in the messy.py example."""
    run_grocery_store_program(3)


if __name__ == "__main__":
    run_with_sample_input()
