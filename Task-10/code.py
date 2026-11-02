

materials = [
    ("Steel", 500, 5),
    ("Plastic", 300, 3),
    ("Rubber", 200, 2)
]


order_demand = 80
planned_production = 100


quality_limit = 5

print("===== MANUFACTURING PRODUCTION PLANNER =====")


max_production = float('inf')

for material, available, required in materials:

    possible = available // required

    if possible < max_production:
        max_production = possible


actual_production = min(planned_production, max_production)

print("\n========== RAW MATERIAL ANALYSIS ==========")

shortages = []

for material, available, required in materials:

    needed = actual_production * required

    print("\nMaterial:", material)
    print("Available Quantity:", available)
    print("Required Quantity:", needed)

    if available < planned_production * required:
        shortage = (planned_production * required) - available
        shortages.append((material, shortage))

        print("Shortage:", shortage)
    else:
        print("Status: Sufficient")


print("\n========== PRODUCTION ANALYSIS ==========")

print("Planned Production :", planned_production)
print("Maximum Production :", max_production)
print("Actual Production  :", actual_production)
print("Customer Demand    :", order_demand)


defects = int(input("\nEnter defective product count: "))


if defects < 0 or defects > actual_production:

    print("Invalid defect count!")
    exit()


good_products = actual_production - defects


defect_percentage = (
    defects / actual_production * 100
    if actual_production > 0 else 0
)


print("\n========== QUALITY ANALYSIS ==========")

print("Defective Products :", defects)
print("Good Products      :", good_products)
print("Defect Percentage  :", round(defect_percentage, 2), "%")

if defect_percentage <= quality_limit:
    print("Quality Status: ACCEPTABLE")
else:
    print("Quality Status: VIOLATION")


print("\n========== ORDER ANALYSIS ==========")

if good_products >= order_demand:
    print("Order Status: Demand Fulfilled")
else:
    print("Order Status: Demand Not Fulfilled")
    print("Product Shortage:", order_demand - good_products)


print("\n========== FINAL PRODUCTION REPORT ==========")

if (
    actual_production >= planned_production
    and good_products >= order_demand
    and defect_percentage <= quality_limit
    and len(shortages) == 0
):
    print("Production Status: FULLY FEASIBLE")
else:
    print("Production Status: NOT FULLY FEASIBLE")

if shortages:
    print("\nRaw Material Shortages:")
    for material, shortage in shortages:
        print(material, ":", shortage, "units")
else:
    print("\nNo Raw Material Shortages.")

print("\n============================================")

