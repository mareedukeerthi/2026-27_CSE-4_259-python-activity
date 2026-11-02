# Integrated Manufacturing Production Planner

## 1. Problem Statement

Develop a Python program to implement an Integrated Manufacturing Production Planner that analyses raw materials, production quantities, defect counts, and customer order demand using lists and tuples.

The program should evaluate the availability of raw materials, calculate the maximum possible production, identify material shortages, calculate defective products, and determine whether production meets customer demand and quality requirements.

The program should:

- Store raw material details using lists and tuples.
- Accept available raw material quantities and required quantities per product.
- Calculate the maximum production possible based on available materials.
- Accept customer order demand.
- Calculate total production and good products after removing defective products.
- Identify raw material shortages.
- Calculate the defect percentage.
- Validate production quality against the maximum permitted defect percentage.
- Determine whether customer demand can be fulfilled.
- Generate a final production feasibility report.

## 2. Algorithm

1. Start the program.
2. Initialize raw material details with available and required quantities.
3. Initialize production quantity and customer order demand.
4. Define the maximum permitted defect percentage.
5. Calculate the maximum possible production using available raw materials.
6. Compare maximum production with customer demand.
7. Identify raw materials that are insufficient.
8. Calculate the actual production quantity.
9. Accept the number of defective products.
10. Calculate the number of good products.
11. Calculate the defect percentage.
12. Compare the defect percentage with the permitted quality limit.
13. Check whether good production meets customer demand.
14. Determine production feasibility.
15. Display raw material availability and shortages.
16. Display production quantity, defective quantity, and good quantity.
17. Display quality status and order fulfilment status.
18. Generate the final production report.
19. Stop.


## 5. Sample Input

The following details are predefined in the program.

Raw Material Details:

| Material | Available Quantity | Required per Product |
| -------- | ------------------ | -------------------- |
| Steel    | 500                | 5                    |
| Plastic  | 300                | 3                    |
| Rubber   | 200                | 2                    |

Production Details:

| Parameter                 | Value |
| ------------------------- | ----- |
| Planned production        | 100   |
| Customer demand           | 80    |
| Maximum defect percentage | 5%    |

User Input:

```
Enter defective product count: 4
```

## 6. Sample Output

```
===== MANUFACTURING PRODUCTION PLANNER =====

========== RAW MATERIAL ANALYSIS ==========

Material: Steel
Available Quantity: 500
Required Quantity: 500
Status: Sufficient

Material: Plastic
Available Quantity: 300
Required Quantity: 240
Shortage: 0

Material: Rubber
Available Quantity: 200
Required Quantity: 160
Status: Sufficient

========== PRODUCTION ANALYSIS ==========

Planned Production : 100
Maximum Production : 100
Actual Production  : 100
Customer Demand    : 80

Enter defective product count: 4

========== QUALITY ANALYSIS ==========

Defective Products : 4
Good Products      : 96
Defect Percentage  : 4.0 %
Quality Status: ACCEPTABLE

========== ORDER ANALYSIS ==========

Order Status: Demand Fulfilled

========== FINAL PRODUCTION REPORT ==========

Production Status: FULLY FEASIBLE

No Raw Material Shortages.

============================================
```

## 7. Mermaid Flowchart Code
``` mermaid

flowchart TD
    A([Start]) --> B[Initialize Raw Materials]
    B --> C[Enter Production and Order Details]
    C --> D[Set Quality Limit]
    D --> E[Calculate Maximum Possible Production]

    E --> F[Determine Actual Production]
    F --> G[Analyze Raw Material Requirements]

    G --> H{Material Sufficient?}
    H -- No --> I[Identify Material Shortage]
    H -- Yes --> J[Continue Material Analysis]

    I --> J
    J --> K{More Materials?}
    K -- Yes --> G
    K -- No --> L[Display Material Report]

    L --> M[Enter Defect Count]
    M --> N{Defect Count Valid?}

    N -- No --> O[Display Invalid Input]
    O --> Z([Stop])

    N -- Yes --> P[Calculate Good Products]
    P --> Q[Calculate Defect Percentage]

    Q --> R{Within Quality Limit?}
    R -- Yes --> S[Quality Acceptable]
    R -- No --> T[Quality Violation]

    S --> U{Good Products Meet Demand?}
    T --> U

    U -- Yes --> V[Demand Fulfilled]
    U -- No --> W[Calculate Product Shortage]

    V --> X[Evaluate Production Feasibility]
    W --> X

    X --> Y[Display Final Production Report]
    Y --> Z

```

## 8. Concepts Used

| Python concept         | Purpose                                   |
| ---------------------- | ----------------------------------------- |
| Lists                  | Store multiple raw material records       |
| Tuples                 | Store material name and quantities        |
| For loop               | Analyse each raw material                 |
| Conditional statements | Identify shortages and quality violations |
| Arithmetic operations  | Calculate production and defects          |
| `min()`                | Determine feasible production quantity    |
| `float('inf')`         | Initialize maximum production calculation |
| `len()`                | Check shortage records                    |
| `round()`              | Calculate defect percentage               |

## 9. Result

The Python program successfully implements an Integrated Manufacturing Production Planner using lists and tuples. It calculates maximum production based on available raw materials, identifies shortages, evaluates defective products, checks quality standards, and determines whether customer orders can be fulfilled.

