


transactions = []


n = int(input("Enter number of transactions: "))


for i in range(n):
    print(f"\nEnter transaction {i+1} details:")

    tid = input("Transaction ID: ")
    amount = float(input("Transaction Amount: "))
    ttype = input("Transaction Type (DEPOSIT/WITHDRAWAL): ").upper()

    
    transaction = (tid, amount, ttype)
    transactions.append(transaction)


seen_ids = set()
duplicates = []
invalid_amounts = []
suspicious = []

for transaction in transactions:

    tid, amount, ttype = transaction

    if tid in seen_ids:
        duplicates.append(tid)
    else:
        seen_ids.add(tid)

    if amount <= 0:
        invalid_amounts.append(transaction)

count = 0
sequence = []

for transaction in transactions:

    if transaction[2] == "WITHDRAWAL":
        count += 1
        sequence.append(transaction)

        if count == 3:
            suspicious.append(sequence.copy())

    else:
        count = 0
        sequence = []

print("\n--- TRANSACTION RECORDS ---")

for transaction in transactions:
    print(transaction)

print("\n--- DUPLICATE TRANSACTION IDs ---")

if duplicates:
    for tid in duplicates:
        print(tid)
else:
    print("No duplicate IDs found")


print("\n--- INVALID TRANSACTIONS ---")

if invalid_amounts:
    for transaction in invalid_amounts:
        print(transaction)
else:
    print("No invalid amounts found")

print("\n--- SUSPICIOUS SEQUENCES ---")

if suspicious:
    for seq in suspicious:
        print("Consecutive withdrawals detected:")
        for transaction in seq:
            print(transaction)
else:
    print("No suspicious sequences found")


print("\n--- AUDIT SUMMARY ---")

print("Total transactions:", n)
print("Duplicate IDs:", len(duplicates))
print("Invalid transactions:", len(invalid_amounts))
print("Suspicious sequences:", len(suspicious))

print("\nTransaction audit completed.")

