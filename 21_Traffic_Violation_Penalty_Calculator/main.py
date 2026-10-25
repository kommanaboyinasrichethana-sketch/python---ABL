offence = input("Offence (helmet/signal/speeding): ").strip().lower()
repeat = input("Is this a repeat offence? (yes/no): ").strip().lower()

if offence == "helmet":
    fine = 500
elif offence == "signal":
    fine = 1000
elif offence == "speeding":
    fine = 1500
else:
    fine = -1

if fine == -1:
    print("Invalid offence type")
elif repeat not in ("yes", "no"):
    print("Invalid repeat-offence answer")
else:
    if repeat == "yes":
        fine = fine + fine * 0.50

    print(f"Final fine: Rs. {fine:.2f}")
    if fine >= 1500:
        print("Review warning: fine is Rs. 1500 or more")
