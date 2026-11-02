

resources = {}

n = int(input("Enter number of resource types: "))

print("\nEnter available resources:")

for i in range(n):
    name = input("Resource name: ").lower()
    quantity = int(input("Available quantity: "))
    resources[name] = quantity


activities = []

m = int(input("\nEnter number of activities: "))

for i in range(m):
    print(f"\nEnter details for Activity {i+1}")

    activity_name = input("Activity name: ")
    priority = int(input("Priority (1 = Highest): "))

    requirements = {}

    for resource in resources:
        qty = int(input(f"Required {resource}: "))
        requirements[resource] = qty

    activities.append(
        (priority, activity_name, requirements)
    )


activities.sort(key=lambda x: x[0])


print("\n--- RESOURCE ALLOCATION REPORT ---")

remaining = resources.copy()
allocation = {}

for priority, activity, requirements in activities:

    allocated = {}
    shortages = {}

    print(f"\nActivity: {activity}")
    print(f"Priority: {priority}")

    for resource in resources:

        required = requirements[resource]
        available = remaining[resource]

     
        allocated_qty = min(required, available)

        shortage = required - allocated_qty

        allocated[resource] = allocated_qty
        shortages[resource] = shortage

     
        remaining[resource] -= allocated_qty

    allocation[activity] = allocated

    print("Allocated Resources:")

    for resource, qty in allocated.items():
        print(f"{resource}: {qty}")

    print("Resource Shortages:")

    found = False

    for resource, qty in shortages.items():
        if qty > 0:
            print(f"{resource}: {qty}")
            found = True

    if not found:
        print("No shortages")

print("\n--- FINAL RESOURCE SUMMARY ---")

print("\nInitially Available Resources:")
for resource, qty in resources.items():
    print(f"{resource}: {qty}")

print("\nAllocated Resources:")
for resource in resources:
    total = resources[resource] - remaining[resource]
    print(f"{resource}: {total}")

print("\nRemaining Resources:")
for resource, qty in remaining.items():
    print(f"{resource}: {qty}")

print("\nCampus resource allocation completed.")

