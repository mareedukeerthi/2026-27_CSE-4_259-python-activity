

days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]

n = int(input("Enter number of appliances: "))

appliances = []
weekly_limits = []
matrix = []

for i in range(n):
    name = input(f"\nEnter appliance {i+1} name: ")
    limit = float(input("Enter weekly consumption limit (kWh): "))

    appliances.append(name)
    weekly_limits.append(limit)

    readings = []
    print(f"Enter electricity readings for {name}:")

    for day in days:
        value = float(input(f"{day}: "))
        readings.append(value)

    matrix.append(readings)

daily_limit = float(input("\nEnter daily consumption limit (kWh): "))

appliance_totals = []

print("\n--- APPLIANCE-WISE CONSUMPTION ---")

for i in range(n):
    total = sum(matrix[i])
    appliance_totals.append(total)

    print(f"{appliances[i]}: {total:.2f} kWh")

    if total > weekly_limits[i]:
        print("Status: Exceeds weekly limit")
    else:
        print("Status: Within weekly limit")

daily_totals = []

print("\n--- DAILY CONSUMPTION ---")

for j in range(7):
    total = 0

    for i in range(n):
        total += matrix[i][j]

    daily_totals.append(total)

    print(f"{days[j]}: {total:.2f} kWh")

    if total > daily_limit:
        print("Status: Exceeds daily limit")
    else:
        print("Status: Within daily limit")

weekly_total = sum(appliance_totals)

print("\n--- WEEKLY SUMMARY ---")
print(f"Total weekly consumption: {weekly_total:.2f} kWh")

print("\nAppliances exceeding weekly limits:")
found = False

for i in range(n):
    if appliance_totals[i] > weekly_limits[i]:
        print(appliances[i])
        found = True

if not found:
    print("None")

print("\nDays exceeding daily limit:")
found = False

for j in range(7):
    if daily_totals[j] > daily_limit:
        print(days[j])
        found = True

if not found:
    print("None")

