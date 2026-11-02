# Tuple-Based Transaction Audit

## 1. Problem Statement

Develop a Python program using tuples to process financial transaction records containing transaction ID, transaction amount, and transaction type.

The program should perform the following operations:

- Store transaction details as tuples.
- Detect duplicate transaction identifiers.
- Identify invalid transaction amounts, such as zero or negative values.
- Detect suspicious transaction sequences, such as three or more consecutive withdrawals.
- Display all transaction details and audit results.
- Generate a summary of duplicate IDs, invalid transactions, and suspicious sequences.

The objective is to identify potential transaction errors and unusual transaction patterns using Python tuples.

## 2. Algorithm

1. Start the program.
2. Read the number of transactions.
3. Create an empty list to store transaction tuples.
4. Accept the following details for each transaction:
   - Transaction ID
   - Transaction amount
   - Transaction type (DEPOSIT/WITHDRAWAL)
5. Store each transaction as a tuple.
6. Create an empty set to track transaction IDs.
7. Check every transaction ID:
   - If the ID already exists, identify it as a duplicate.
   - Otherwise, add the ID to the set.
8. Check transaction amounts:
   - If the amount is less than or equal to zero, mark it as invalid.
   - Otherwise, consider it valid.
9. Check transaction sequences:
   - Count consecutive withdrawals.
   - If three or more consecutive withdrawals occur, mark the sequence as suspicious.
10. Display all transaction records.
11. Display duplicate transaction IDs.
12. Display invalid transactions.
13. Display suspicious transaction sequences.
14. Display the audit summary.
15. Stop the program.


## 5. Sample Input

```
Enter number of transactions: 7

Enter transaction 1 details:
Transaction ID: T101
Transaction Amount: 5000
Transaction Type (DEPOSIT/WITHDRAWAL): DEPOSIT

Enter transaction 2 details:
Transaction ID: T102
Transaction Amount: 2000
Transaction Type (DEPOSIT/WITHDRAWAL): WITHDRAWAL

Enter transaction 3 details:
Transaction ID: T103
Transaction Amount: 1500
Transaction Type (DEPOSIT/WITHDRAWAL): WITHDRAWAL

Enter transaction 4 details:
Transaction ID: T104
Transaction Amount: 1000
Transaction Type (DEPOSIT/WITHDRAWAL): WITHDRAWAL

Enter transaction 5 details:
Transaction ID: T102
Transaction Amount: 3000
Transaction Type (DEPOSIT/WITHDRAWAL): DEPOSIT

Enter transaction 6 details:
Transaction ID: T105
Transaction Amount: -500
Transaction Type (DEPOSIT/WITHDRAWAL): WITHDRAWAL

Enter transaction 7 details:
Transaction ID: T106
Transaction Amount: 2500
Transaction Type (DEPOSIT/WITHDRAWAL): DEPOSIT
```

## 6. Sample Output

```
--- TRANSACTION RECORDS ---
('T101', 5000.0, 'DEPOSIT')
('T102', 2000.0, 'WITHDRAWAL')
('T103', 1500.0, 'WITHDRAWAL')
('T104', 1000.0, 'WITHDRAWAL')
('T102', 3000.0, 'DEPOSIT')
('T105', -500.0, 'WITHDRAWAL')
('T106', 2500.0, 'DEPOSIT')

--- DUPLICATE TRANSACTION IDs ---
T102

--- INVALID TRANSACTIONS ---
('T105', -500.0, 'WITHDRAWAL')

--- SUSPICIOUS SEQUENCES ---
Consecutive withdrawals detected:
('T102', 2000.0, 'WITHDRAWAL')
('T103', 1500.0, 'WITHDRAWAL')
('T104', 1000.0, 'WITHDRAWAL')

--- AUDIT SUMMARY ---
Total transactions: 7
Duplicate IDs: 1
Invalid transactions: 1
Suspicious sequences: 1

Transaction audit completed.
```

## 7. Mermaid Flowchart Code
``` mermaid

flowchart TD
    A([Start]) --> B[/Enter number of transactions/]
    B --> C[Create empty transaction list]
    C --> D[/Input transaction ID, amount and type/]
    D --> E[Store transaction as tuple]
    E --> F{More transactions?}
    F -->|Yes| D
    F -->|No| G[Initialize audit variables]
    G --> H[Check transaction ID]
    H --> I{ID already exists?}
    I -->|Yes| J[Record duplicate ID]
    I -->|No| K[Add ID to set]
    J --> L{Amount <= 0?}
    K --> L
    L -->|Yes| M[Record invalid transaction]
    L -->|No| N[Continue audit]
    M --> O[Check transaction sequence]
    N --> O
    O --> P{Three consecutive withdrawals?}
    P -->|Yes| Q[Mark suspicious sequence]
    P -->|No| R[Continue checking]
    Q --> S[Display audit results]
    R --> S
    S --> T[/Display audit summary/]
    T --> U([Stop])

```

## 8. Result

The Python program successfully performs tuple-based transaction auditing. It detects duplicate transaction identifiers, identifies invalid transaction amounts, and finds suspicious sequences of three or more consecutive withdrawals.

The program also generates an audit summary showing the total number of transactions, duplicate IDs, invalid transactions, and suspicious sequences.

Time Complexity: \\(O(n)\\), where \\(n\\) is the number of transactions.

Space Complexity: \\(O(n)\\), for storing transaction tuples and audit records.

Conclusion: Tuple-based transaction auditing helps identify duplicate records, invalid amounts, and unusual transaction patterns efficiently using Python data structures.
