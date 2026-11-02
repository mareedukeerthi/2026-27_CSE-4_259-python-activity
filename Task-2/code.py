
from datetime import datetime
import math


rates = {
    "two-wheeler": 10,
    "car": 20,
    "bus": 40
}


daily_limits = {
    "two-wheeler": 100,
    "car": 200,
    "bus": 400
}


overnight_charge = {
    "two-wheeler": 20,
    "car": 50,
    "bus": 100
}

PENALTY = 100

print("===== SMART PARKING FEE MANAGEMENT =====")

vehicle_number = input("Enter vehicle number: ").upper()

print("\nVehicle Categories:")
print("1. Two-wheeler")
print("2. Car")
print("3. Bus")

category = input("Enter vehicle category: ").lower()

if category not in rates:
    print("Invalid vehicle category!")
    exit()

time_format = "%Y-%m-%d %H:%M"

try:
    entry = input(
        "Enter entry date and time (YYYY-MM-DD HH:MM): "
    )
    exit_time = input(
        "Enter exit date and time (YYYY-MM-DD HH:MM): "
    )

    entry_time = datetime.strptime(entry, time_format)
    exit_time = datetime.strptime(exit_time, time_format)

  
    if exit_time <= entry_time:
        print("Error: Exit time must be after entry time.")
        exit()

except ValueError:
    print("Invalid date or time format!")
    exit()


duration = (exit_time - entry_time).total_seconds() / 3600

hours = math.ceil(duration)


days = math.ceil(duration / 24)

hourly_fee = hours * rates[category]

max_fee = days * daily_limits[category]

parking_fee = min(hourly_fee, max_fee)

overnight = (
    entry_time.date() != exit_time.date()
)

if overnight:
    night_fee = days * overnight_charge[category]
else:
    night_fee = 0

violation = input(
    "Is there any parking violation? (yes/no): "
).lower()

if violation == "yes":
    penalty = PENALTY
else:
    penalty = 0

total_amount = parking_fee + night_fee + penalty

print("\n========== PARKING BILL ==========")
print("Vehicle Number :", vehicle_number)
print("Vehicle Category:", category.title())
print("Entry Time     :", entry_time)
print("Exit Time      :", exit_time)
print("Duration       :", round(duration, 2), "hours")
print("Billable Hours :", hours)
print("Parking Fee    : Rs.", parking_fee)
print("Overnight Fee  : Rs.", night_fee)
print("Penalty        : Rs.", penalty)
print("---------------------------------")
print("TOTAL AMOUNT   : Rs.", total_amount)
print("=================================")

