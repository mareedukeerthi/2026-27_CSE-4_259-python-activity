
required_data = float(input("Enter required data usage (GB): "))
required_calls = int(input("Enter required call minutes: "))
required_validity = int(input("Enter required validity (days): "))
budget = float(input("Enter maximum budget (Rs): "))

n = int(input("\nEnter number of mobile plans: "))

eligible_plans = []

for i in range(n):
    print(f"\nEnter details of Plan {i + 1}")

    name = input("Plan name: ")
    price = float(input("Plan price (Rs): "))
    data = float(input("Data limit (GB): "))
    calls = int(input("Call minutes limit: "))
    validity = int(input("Validity (days): "))
    data_rate = float(input("Extra data charge per GB (Rs): "))
    call_rate = float(input("Extra call charge per minute (Rs): "))

    excess_data = max(0, required_data - data)
    excess_calls = max(0, required_calls - calls)

    extra_data_cost = excess_data * data_rate
    extra_call_cost = excess_calls * call_rate

    total_cost = price + extra_data_cost + extra_call_cost

    print("\nPlan:", name)
    print("Excess Data:", excess_data, "GB")
    print("Excess Calls:", excess_calls, "minutes")
    print("Extra Charges:", extra_data_cost + extra_call_cost)
    print("Total Cost: Rs.", total_cost)

    if validity >= required_validity and total_cost <= budget:
        eligible_plans.append((total_cost, name))

print("\n----- OPTIMIZATION RESULT -----")

if eligible_plans:
    best_plan = min(eligible_plans)

    print("Most Economical Eligible Plan:", best_plan[1])
    print("Minimum Total Cost: Rs.", best_plan[0])

else:
    print("No eligible plan found within the given budget and validity.")

