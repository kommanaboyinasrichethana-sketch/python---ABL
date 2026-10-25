distance = float(input("Distance in kilometres: "))
travel_class = input("Travel class (Sleeper/AC): ").strip().lower()
age = int(input("Passenger age: "))

if distance <= 0 or age < 0:
    print("Invalid input")
elif travel_class not in ("sleeper", "ac"):
    print("Invalid travel class")
else:
    rate = 1.2 if travel_class == "sleeper" else 2.0
    base_fare = distance * rate
    concession = base_fare * 0.20 if age >= 60 else 0
    reservation_fee = 30
    final_fare = base_fare - concession + reservation_fee

    print(f"Base fare: Rs. {base_fare:.2f}")
    print(f"Age concession: Rs. {concession:.2f}")
    print(f"Reservation fee: Rs. {reservation_fee:.2f}")
    print(f"Final fare: Rs. {final_fare:.2f}")
