# Progressive Water Tariff Analysis – Python Project

## 1. Problem Statement

The Progressive Water Tariff Analysis system is designed to calculate water bills for multiple households based on their monthly water consumption.

The system uses a progressive tariff structure in which different rates are applied to different consumption slabs. It also considers fixed monthly charges and additional penalties for excessive water consumption or late payment.

The program accepts the number of households, household identification details, and monthly water consumption in kilolitres (KL). It calculates the water bill using slab-wise rates, adds fixed charges and penalties, and displays the total bill for each household.

It also compares water consumption among households, identifies households with excessive water usage, and determines the household with the highest consumption.

Objectives:

- Calculate water bills for multiple households.
- Apply progressive water consumption slabs.
- Include fixed monthly charges.
- Add penalties for excessive consumption.
- Compare household consumption patterns.
- Identify households with excessive water usage.
- Display individual and total water bills.

## 2. Algorithm

1. Start the program.
2. Define progressive water tariff rates:
   - First 10 KL: ₹5 per KL.
   - Next 10 KL: ₹8 per KL.
   - Next 10 KL: ₹12 per KL.
   - Above 30 KL: ₹15 per KL.
3. Define the fixed monthly charge as ₹50.
4. Define the excessive consumption limit as 30 KL.
5. Define the excessive usage penalty as ₹100.
6. Accept the number of households.
7. For each household:
   - Enter household ID.
   - Enter monthly water consumption in KL.
   - Validate the consumption value.
   - Calculate the charges according to progressive slabs.
   - Add the fixed monthly charge.
   - Check whether consumption exceeds 30 KL.
   - Add the penalty if consumption exceeds the limit.
   - Calculate the final water bill.
   - Store household details and bill information.
8. Calculate the average water consumption.
9. Identify the household with the highest consumption.
10. Identify households with excessive water usage.
11. Display individual household bills.
12. Display the consumption comparison and summary.
13. Stop the program.




## 5. Sample Input

```
===== PROGRESSIVE WATER TARIFF ANALYSIS =====

Enter number of households: 4

Household 1
Enter household ID: H101
Enter monthly water consumption (KL): 8

Household 2
Enter household ID: H102
Enter monthly water consumption (KL): 15

Household 3
Enter household ID: H103
Enter monthly water consumption (KL): 25

Household 4
Enter household ID: H104
Enter monthly water consumption (KL): 40
```

## 6. Sample Output

```
========== HOUSEHOLD WATER BILLS ==========

Household ID      : H101
Water Consumption : 8.0 KL
Water Charges     : Rs. 90.0
Penalty           : Rs. 0
Total Bill        : Rs. 90.0
Usage Status      : Normal Consumption

Household ID      : H102
Water Consumption : 15.0 KL
Water Charges     : Rs. 130.0
Penalty           : Rs. 0
Total Bill        : Rs. 130.0
Usage Status      : Normal Consumption

Household ID      : H103
Water Consumption : 25.0 KL
Water Charges     : Rs. 240.0
Penalty           : Rs. 0
Total Bill        : Rs. 240.0
Usage Status      : Normal Consumption

Household ID      : H104
Water Consumption : 40.0 KL
Water Charges     : Rs. 500.0
Penalty           : Rs. 100
Total Bill        : Rs. 600.0
Usage Status      : Excessive Consumption

========== CONSUMPTION ANALYSIS ==========

Total Households : 4
Total Consumption: 88.0 KL
Average Usage    : 22.0 KL

Highest Consumer : H104 - 40.0 KL

Excessive Water Usage Households:
H104 - 40.0 KL

Total Water Bill Revenue: Rs. 1060.0

===== ANALYSIS COMPLETED =====
```

## 7. Bill Calculation

The tariff structure used in this program is:

| Consumption slab | Rate per KL |
| ---------------- | ----------- |
| 0–10 KL          | ₹5          |
| 11–20 KL         | ₹8          |
| 21–30 KL         | ₹12         |
| Above 30 KL      | ₹15         |

Additional charges:

| Description                        | Amount |
| ---------------------------------- | ------ |
| Fixed monthly charge               | ₹50    |
| Excess usage penalty (above 30 KL) | ₹100   |

Example: Household H104

Water consumption = 40 KL.

- First 10 KL = 10 × 5 = ₹50
- Next 10 KL = 10 × 8 = ₹80
- Next 10 KL = 10 × 12 = ₹120
- Remaining 10 KL = 10 × 15 = ₹150
- Fixed charge = ₹50
- Excess usage penalty = ₹100

Total bill = 50 + 80 + 120 + 150 + 50 + 100

Final bill: ₹550

Correction to the sample output above: H104's water charges are ₹400, not ₹500, and its total bill is ₹500, not ₹600. Therefore, the correct total revenue is ₹960.

## 8. Mermaid Flowchart Code
``` mermaid

flowchart TD
    A([Start]) --> B[/Enter Number of Households/]
    B --> C[Initialize Household List]
    C --> D[/Enter Household ID and Water Consumption/]

    D --> E{Valid Numeric Input and Units >= 0?}

    E -- No --> F[/Display Invalid Input Error/]
    F --> Z([Stop])

    E -- Yes --> G[Calculate Progressive Slab Charges]

    G --> H[Add Fixed Monthly Fee]

    H --> I{Consumption > 30 KL?}

    I -- Yes --> J[Add Excess Usage Penalty]
    I -- No --> K[Penalty = 0]

    J --> L[Calculate Total Water Bill]
    K --> L

    L --> M[Store Household Details]

    M --> N{More Households?}

    N -- Yes --> D
    N -- No --> O[Calculate Average Consumption]

    O --> P[Identify Highest Consumer]

    P --> Q[Identify Excessive Usage Households]

    Q --> R[Calculate Total Revenue]

    R --> S[/Display Bills and Analysis/]

    S --> Z([Stop])

```

## 9. Conclusion

The Progressive Water Tariff Analysis system successfully calculates water bills for multiple households using progressive consumption slabs, fixed monthly charges, and excessive usage penalties.

It also compares household consumption, identifies the highest water consumer, and highlights households that exceed the permitted consumption limit.

This project helps water authorities monitor water usage, improve billing accuracy, and encourage households to conserve water.
