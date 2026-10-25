material = float(input("Material cost: "))
labour = float(input("Labour cost: "))
machine = float(input("Machine cost: "))
quantity = int(input("Number of items produced: "))
price = float(input("Selling price per item: "))
target = float(input("Target profit percentage: "))

if min(material, labour, machine, price, target) < 0 or quantity <= 0:
    print("Invalid input")
else:
    total_cost = material + labour + machine
    revenue = quantity * price
    profit = revenue - total_cost
    profit_percent = profit / total_cost * 100 if total_cost > 0 else 0

    print(f"Total manufacturing cost: Rs. {total_cost:.2f}")
    print(f"Sales revenue: Rs. {revenue:.2f}")
    print(f"Profit/Loss: Rs. {profit:.2f}")
    print(f"Profit percentage: {profit_percent:.2f}%")

    if profit < 0:
        print("Result: Loss")
    elif profit_percent >= target:
        print("Result: Profit target achieved")
    else:
        print("Result: Profit target not achieved")
