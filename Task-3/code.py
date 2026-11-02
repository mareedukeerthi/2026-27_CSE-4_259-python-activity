

FIXED_CHARGE = 50
EXCESS_LIMIT = 30
EXCESS_PENALTY = 100

def calculate_water_bill(units):

    bill = 0

    if units <= 10:
        bill = units * 5

    elif units <= 20:
        bill = (10 * 5) + ((units - 10) * 8)

    elif units <= 30:
        bill = (10 * 5) + (10 * 8) + ((units - 20) * 12)

    else:
        bill = (
            (10 * 5)
            + (10 * 8)
            + (10 * 12)
            + ((units - 30) * 15)
        )

    bill += FIXED_CHARGE

    penalty = 0

    if units > EXCESS_LIMIT:
        penalty = EXCESS_PENALTY

    total = bill + penalty

    return bill, penalty, total


print("===== PROGRESSIVE WATER TARIFF ANALYSIS =====")

try:
    n = int(input("Enter number of households: "))

    if n <= 0:
        print("Number of households must be positive.")
        raise SystemExit

    households = []

    for i in range(n):

        print("\nHousehold", i + 1)

        household_id = input("Enter household ID: ")

        units = float(
            input("Enter monthly water consumption (KL): ")
        )

        if units < 0:
            print("Invalid consumption! Enter a positive value.")
            raise SystemExit

        bill, penalty, total = calculate_water_bill(units)

        households.append({
            "id": household_id,
            "units": units,
            "bill": bill,
            "penalty": penalty,
            "total": total
        })

    total_consumption = sum(h["units"] for h in households)

    average = total_consumption / n

    highest = max(households, key=lambda h: h["units"])

    print("\n========== HOUSEHOLD WATER BILLS ==========")

    for h in households:

        print("\nHousehold ID      :", h["id"])
        print("Water Consumption :", h["units"], "KL")
        print("Water Charges     : Rs.", round(h["bill"], 2))
        print("Penalty           : Rs.", h["penalty"])
        print("Total Bill        : Rs.", round(h["total"], 2))

        if h["units"] > EXCESS_LIMIT:
            print("Usage Status      : Excessive Consumption")
        else:
            print("Usage Status      : Normal Consumption")

    print("\n========== CONSUMPTION ANALYSIS ==========")

    print("Total Households :", n)
    print("Total Consumption:", total_consumption, "KL")
    print("Average Usage    :", round(average, 2), "KL")

    print(
        "Highest Consumer :",
        highest["id"],
        "-",
        highest["units"],
        "KL"
    )

    print("\nExcessive Water Usage Households:")

    excessive_found = False

    for h in households:
        if h["units"] > EXCESS_LIMIT:
            print(h["id"], "-", h["units"], "KL")
            excessive_found = True

    if not excessive_found:
        print("No excessive usage detected.")

    total_revenue = sum(h["total"] for h in households)

    print("\nTotal Water Bill Revenue: Rs.", round(total_revenue, 2))

    print("\n===== ANALYSIS COMPLETED =====")

except ValueError:
    print("Invalid input! Please enter valid numeric values.")

