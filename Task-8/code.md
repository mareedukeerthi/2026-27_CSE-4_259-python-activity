# Integrated Student Record Consistency Checker

## 1. Problem Statement

Develop a Python program to implement an Integrated Student Record Consistency Checker that validates student academic records stored using lists and tuples.

The program should check student identifiers, names, marks, attendance percentages, and course records. It should identify duplicate student IDs, missing values, invalid marks, incorrect attendance percentages, and inconsistent course records.

The program should:

- Store student details using lists and tuples.
- Validate student ID and student name.
- Detect duplicate student identifiers.
- Identify missing or empty values.
- Validate marks within the range of 0 to 100.
- Validate attendance percentages within the range of 0 to 100.
- Check whether course records are valid.
- Display valid and invalid student records.
- Generate a consistency report.

## 2. Algorithm

1. Start the program.
2. Initialize a list containing student records.
3. Store each student's ID, name, marks, attendance, and course details in a tuple.
4. Create an empty set to track student IDs.
5. Create an empty list to store validation errors.
6. Read each student record from the list.
7. Check whether the student ID is missing.
8. Check whether the student ID is duplicated.
9. Validate the student name.
10. Check whether marks are available and within the range of 0–100.
11. Validate attendance percentage between 0 and 100.
12. Check whether the course record is missing or invalid.
13. Add error messages for inconsistent records.
14. If no errors are found, classify the record as valid.
15. Otherwise, classify the record as invalid.
16. Display each student's validation status and errors.
17. Display the total number of valid and invalid records.
18. Stop.


## 5. Sample Input

The following student records are predefined in the program:

```
S101, Arun, 85, 92, Python
S102, Bala, 78, 88, Java
S103, "", 105, 75, Python
S101, Divya, 90, 95, C++
S105, Kiran, 65, 110, ""
S106, Ravi, None, 80, Java
S107, Meena, 95, 98, Python
```

Record format:

```
(Student ID, Name, Marks, Attendance, Course)
```

## 6. Sample Output

```
===== STUDENT RECORD CONSISTENCY CHECKER =====

Student ID: S101
Name: Arun
Marks: 85
Attendance: 92
Course: Python
Status: VALID

Student ID: S102
Name: Bala
Marks: 78
Attendance: 88
Course: Java
Status: VALID

Student ID: S103
Name:
Marks: 105
Attendance: 75
Course: Python
Status: INVALID
Error: Missing Student Name
Error: Marks must be between 0 and 100

Student ID: S101
Name: Divya
Marks: 90
Attendance: 95
Course: C++
Status: INVALID
Error: Duplicate Student ID

Student ID: S105
Name: Kiran
Marks: 65
Attendance: 110
Course:
Status: INVALID
Error: Attendance must be between 0 and 100
Error: Missing Course Record

Student ID: S106
Name: Ravi
Marks: None
Attendance: 80
Course: Java
Status: INVALID
Error: Missing Marks

Student ID: S107
Name: Meena
Marks: 95
Attendance: 98
Course: Python
Status: VALID

========== CONSISTENCY REPORT ==========
Total Student Records : 7
Valid Records         : 3
Invalid Records       : 4
========================================
```

## 7. Mermaid Flowchart Code
``` mermaid

flowchart TD
    A([Start]) --> B[Initialize Student Records]
    B --> C[Create Empty ID Set]
    C --> D[Set Valid and Invalid Counters]
    D --> E[Read Next Student Record]

    E --> F{More Records Available?}

    F -- No --> R[Display Final Consistency Report]
    R --> S([Stop])

    F -- Yes --> G[Extract ID Name Marks Attendance Course]

    G --> H{Student ID Missing?}
    H -- Yes --> I[Add Missing ID Error]
    H -- No --> J{ID Already Exists?}

    J -- Yes --> K[Add Duplicate ID Error]
    J -- No --> L[Add ID to Set]

    I --> M[Validate Name]
    K --> M
    L --> M

    M --> N{Name Missing?}
    N -- Yes --> O[Add Name Error]
    N -- No --> P[Validate Marks]

    O --> P

    P --> Q{Marks Valid?}
    Q -- No --> T[Add Marks Error]
    Q -- Yes --> U[Validate Attendance]

    T --> U

    U --> V{Attendance Valid?}
    V -- No --> W[Add Attendance Error]
    V -- Yes --> X[Validate Course]

    W --> X

    X --> Y{Course Missing?}
    Y -- Yes --> Z[Add Course Error]
    Y -- No --> AA[Check Error List]

    Z --> AA

    AA --> AB{Any Errors?}
    AB -- No --> AC[Display VALID]
    AB -- Yes --> AD[Display INVALID and Errors]

    AC --> AE[Update Valid Count]
    AD --> AF[Update Invalid Count]

    AE --> E
    AF --> E

```

## 8. Concepts Used

| Python concept         | Purpose                            |
| ---------------------- | ---------------------------------- |
| Lists                  | Store multiple student records     |
| Tuples                 | Store individual student details   |
| Sets                   | Detect duplicate student IDs       |
| Conditional statements | Validate student information       |
| For loop               | Process each student record        |
| If-else                | Identify valid and invalid records |
| Lists                  | Store validation error messages    |
| `len()`                | Count student records              |

Result: The Python program successfully checks student records, detects duplicate IDs, missing values, invalid marks, attendance errors, and missing course details, and generates a final consistency report.
