distance = float(input("Journey distance (km): "))
fuel_price = float(input("Fuel price per litre: "))
mileage1 = float(input("Vehicle 1 mileage (km/litre): "))
mileage2 = float(input("Vehicle 2 mileage (km/litre): "))

if min(distance, fuel_price, mileage1, mileage2) <= 0:
    print("Invalid input: values must be positive")
else:
    fuel1 = distance / mileage1
    fuel2 = distance / mileage2
    cost1 = fuel1 * fuel_price
    cost2 = fuel2 * fuel_price

    print(f"Vehicle 1 fuel required: {fuel1:.2f} litres")
    print(f"Vehicle 1 fuel cost: Rs. {cost1:.2f}")
    print(f"Vehicle 2 fuel required: {fuel2:.2f} litres")
    print(f"Vehicle 2 fuel cost: Rs. {cost2:.2f}")

    if cost1 < cost2:
        print("Vehicle 1 is more economical")
    elif cost2 < cost1:
        print("Vehicle 2 is more economical")
    else:
        print("Both vehicles have equal fuel cost")
