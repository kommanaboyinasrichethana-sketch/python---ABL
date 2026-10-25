attended = int(input("Classes attended: "))
total = int(input("Total classes held: "))

if total <= 0 or attended < 0 or attended > total:
    print("Invalid attendance data")
else:
    percentage = attended / total * 100
    print(f"Current attendance: {percentage:.2f}%")
    extra = 0

    while percentage < 75:
        attended += 1
        total += 1
        extra += 1
        percentage = attended / total * 100

    if extra == 0:
        print("Attendance requirement already satisfied")
    else:
        print("Additional consecutive classes required:", extra)
    print(f"Attendance after extra classes: {percentage:.2f}%")
