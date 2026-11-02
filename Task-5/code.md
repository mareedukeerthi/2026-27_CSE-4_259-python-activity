# Weekly Electricity Consumption Matrix

## 1. Problem Statement

Develop a Python program to process appliance-wise electricity consumption readings for seven days using a two-dimensional matrix.

The program should:

- Accept electricity consumption readings (in kWh) for multiple appliances over seven days.
- Calculate the total electricity consumption for each day.
- Calculate the total electricity consumption of each appliance during the week.
- Calculate the overall weekly electricity consumption.
- Identify appliances whose weekly consumption exceeds a specified limit.
- Identify days on which total electricity consumption exceeds a specified daily limit.

## 2. Algorithm

1. Start the program.
2. Read the number of appliances.
3. Read the names of all appliances.
4. Read the weekly consumption limit for each appliance.
5. Read the daily electricity consumption limit.
6. Create a two-dimensional matrix to store seven days of readings for each appliance.
7. Accept electricity readings for every appliance across seven days.
8. Initialize daily totals and appliance totals to zero.
9. Calculate the total consumption of each appliance by adding its seven daily readings.
10. Calculate the total consumption for each day by adding readings from all appliances.
11. Compare appliance totals with their weekly limits.
12. Compare daily totals with the daily consumption limit.
13. Display the appliance-wise totals, daily totals, and overall weekly consumption.
14. Display appliances and days exceeding their respective limits.
15. Stop the program.



## 5. Sample Input

For this example, consider three appliances: Fan, AC, and Refrigerator.

```
Enter number of appliances: 3

Enter appliance 1 name: Fan
Enter weekly consumption limit (kWh): 20
Enter electricity readings for Fan:
Monday: 3
Tuesday: 3
Wednesday: 3
Thursday: 3
Friday: 3
Saturday: 3
Sunday: 3

Enter appliance 2 name: AC
Enter weekly consumption limit (kWh): 50
Enter electricity readings for AC:
Monday: 10
Tuesday: 12
Wednesday: 11
Thursday: 10
Friday: 12
Saturday: 13
Sunday: 12

Enter appliance 3 name: Refrigerator
Enter weekly consumption limit (kWh): 30
Enter electricity readings for Refrigerator:
Monday: 5
Tuesday: 5
Wednesday: 5
Thursday: 5
Friday: 5
Saturday: 5
Sunday: 5

Enter daily consumption limit (kWh): 20
```

## 6. Sample Output

```
--- APPLIANCE-WISE CONSUMPTION ---
Fan: 21.00 kWh
Status: Exceeds weekly limit

AC: 80.00 kWh
Status: Exceeds weekly limit

Refrigerator: 35.00 kWh
Status: Exceeds weekly limit

--- DAILY CONSUMPTION ---
Monday: 18.00 kWh
Status: Within daily limit

Tuesday: 20.00 kWh
Status: Within daily limit

Wednesday: 19.00 kWh
Status: Within daily limit

Thursday: 18.00 kWh
Status: Within daily limit

Friday: 20.00 kWh
Status: Within daily limit

Saturday: 21.00 kWh
Status: Exceeds daily limit

Sunday: 20.00 kWh
Status: Within daily limit

--- WEEKLY SUMMARY ---
Total weekly consumption: 136.00 kWh

Appliances exceeding weekly limits:
Fan
AC
Refrigerator

Days exceeding daily limit:
Saturday
```

## 7. Mermaid Flowchart Code
``` mermaid

flowchart TD
    A([Start]) --> B[/Enter number of appliances/]
    B --> C[/Enter appliance names and weekly limits/]
    C --> D[/Enter daily consumption limit/]
    D --> E[Initialize consumption matrix]
    E --> F[/Input 7 days readings for each appliance/]
    F --> G[Calculate appliance-wise weekly totals]
    G --> H[Calculate daily consumption totals]
    H --> I[Calculate overall weekly consumption]
    I --> J{Appliance total exceeds weekly limit?}
    J -->|Yes| K[Display appliance limit exceeded]
    J -->|No| L[Display appliance within limit]
    K --> M{More appliances?}
    L --> M
    M -->|Yes| J
    M -->|No| N{Daily total exceeds daily limit?}
    N -->|Yes| O[Display daily limit exceeded]
    N -->|No| P[Display daily consumption within limit]
    O --> Q{More days?}
    P --> Q
    Q -->|Yes| N
    Q -->|No| R[/Display weekly summary/]
    R --> S([Stop])

```

## 8. Result

The Python program successfully processes appliance-wise electricity consumption readings for seven days using a two-dimensional matrix. It calculates daily totals, appliance-wise weekly totals, and overall weekly consumption. It also identifies appliances and days that exceed the specified electricity consumption limits.

Time Complexity: \\(O(n \times 7)\\), where \\(n\\) is the number of appliances.

Space Complexity: \\(O(n \times 7)\\), for storing the electricity consumption matrix.

I can also create an image of the complete flowchart for your practical record.
