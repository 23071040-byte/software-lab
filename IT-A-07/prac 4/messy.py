print("Welcome to Grocery Store")

n = int(input("Enter number of items: "))

items = []
prices = []
qty = []

i = 0
while i < n:
    name = input("Item Name: ")
    p = float(input("Price: "))
    q = int(input("Quantity: "))
    items.append(name)
    prices.append(p)
    qty.append(q)
    i += 1

print("\n------ BILL ------")

total = 0

for i in range(n):
    amount = prices[i] * qty[i]
    total += amount

    if amount >= 1000:
        discount = amount * 0.15
    elif amount >= 500:
        discount = amount * 0.10
    else:
        discount = 0

    final = amount - discount

    print("Item:", items[i])
    print("Price:", prices[i])
    print("Quantity:", qty[i])
    print("Amount:", amount)
    print("Discount:", discount)
    print("Final:", final)
    print("----------------")

gst = total * 0.05
grand = total + gst

expensive = prices[0]
cheap = prices[0]
exp_item = items[0]
cheap_item = items[0]

for i in range(1, n):
    if prices[i] > expensive:
        expensive = prices[i]
        exp_item = items[i]

    if prices[i] < cheap:
        cheap = prices[i]
        cheap_item = items[i]

print("Subtotal:", total)
print("GST:", gst)
print("Grand Total:", grand)
print("Most Expensive Item:", exp_item, expensive)
print("Cheapest Item:", cheap_item, cheap)

count = 0
for i in range(n):
    if qty[i] > 5:
        count += 1

print("Items purchased in bulk:", count)