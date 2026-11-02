# Smart Classroom Timetable Allocation

## 1. Problem Statement

Develop a Python program to implement a Smart Classroom Timetable Allocation System using lists and tuples.

The program should allocate courses to classrooms and time periods while satisfying classroom capacity and timetable constraints. It should detect scheduling clashes, identify insufficient classroom capacity, and determine whether all courses can be accommodated.

The program should:

- Store course details, classroom details, and time periods using lists and tuples.
- Validate classroom capacity against course student strength.
- Allocate courses to suitable classrooms and periods.
- Detect clashes when two courses are assigned to the same classroom and period.
- Ensure that a course is not scheduled more than once.
- Identify courses that cannot be allocated.
- Check whether all courses can be accommodated.
- Display the final timetable and allocation status.

## 2. Algorithm

1. Start the program.
2. Initialize a list of courses with course ID and student strength.
3. Initialize a list of classrooms with room ID and seating capacity.
4. Initialize a list of available time periods.
5. Create an empty list to store timetable allocations.
6. Create an empty list to store unallocated courses.
7. Read each course from the course list.
8. Check each available classroom.
9. Validate whether the classroom capacity is sufficient for the course.
10. Check whether the classroom is already occupied during the selected period.
11. If the classroom is available and capacity is sufficient, allocate the course.
12. Store the allocation as a tuple containing course, classroom, and period.
13. If no suitable classroom is available, add the course to the unallocated list.
14. Repeat the process for all courses.
15. Display the allocated timetable.
16. Display any classroom capacity errors or scheduling clashes.
17. Check whether all courses are allocated.
18. Display the final allocation status.
19. Stop.


## 5. Sample Input

The following details are predefined in the program.

Courses:

| Course ID | Student Strength |
| --------- | ---------------- |
| C101      | 40               |
| C102      | 30               |
| C103      | 50               |
| C104      | 25               |
| C105      | 60               |

Classrooms:

| Classroom ID | Capacity |
| ------------ | -------- |
| R101         | 40       |
| R102         | 35       |
| R103         | 55       |

Available Time Periods:

```
9AM-10AM
10AM-11AM
11AM-12PM
```

## 6. Sample Output

```
===== SMART CLASSROOM TIMETABLE ALLOCATION =====

========== ALLOCATED TIMETABLE ==========

Course ID       : C101
Classroom       : R101
Time Period     : 9AM-10AM
Student Strength: 40
----------------------------------------
Course ID       : C102
Classroom       : R101
Time Period     : 10AM-11AM
Student Strength: 30
----------------------------------------
Course ID       : C103
Classroom       : R103
Time Period     : 9AM-10AM
Student Strength: 50
----------------------------------------
Course ID       : C104
Classroom       : R101
Time Period     : 11AM-12PM
Student Strength: 25
----------------------------------------

========== UNALLOCATED COURSES ==========
C105

========== FINAL REPORT ==========
Total Courses     : 5
Allocated Courses : 4
Unallocated       : 1
Status: All courses cannot be accommodated.
==================================
```

Explanation: Course C105 requires 60 seats, but the largest available classroom has only 55 seats. Therefore, C105 cannot be allocated.

## 7. Mermaid Flowchart Code
``` mermaid

flowchart TD
    A([Start]) --> B[Initialize Courses]
    B --> C[Initialize Classrooms]
    C --> D[Initialize Time Periods]
    D --> E[Create Timetable and Unallocated Lists]
    E --> F[Select Next Course]

    F --> G{More Courses Available?}

    G -- No --> R[Display Final Report]
    R --> S{All Courses Allocated?}
    S -- Yes --> T[Display All Courses Accommodated]
    S -- No --> U[Display Unallocated Courses]
    T --> V([Stop])
    U --> V

    G -- Yes --> H[Select Available Period]
    H --> I[Select Classroom]
    I --> J{Classroom Capacity Sufficient?}

    J -- No --> K[Try Next Classroom]
    J -- Yes --> L{Classroom Already Occupied?}

    L -- Yes --> K
    L -- No --> M[Allocate Course to Classroom and Period]

    M --> N[Store Allocation as Tuple]
    N --> O[Mark Course as Allocated]
    O --> F

    K --> P{More Classrooms Available?}
    P -- Yes --> I
    P -- No --> Q{More Periods Available?}

    Q -- Yes --> H
    Q -- No --> W[Add Course to Unallocated List]
    W --> F

```

## 8. Concepts Used

| Python concept         | Purpose                                   |
| ---------------------- | ----------------------------------------- |
| Lists                  | Store courses, classrooms and periods     |
| Tuples                 | Store course, room and allocation details |
| Nested loops           | Check possible classroom allocations      |
| Conditional statements | Validate capacity and clashes             |
| Boolean variables      | Track allocation status                   |
| `append()`             | Store timetable allocations               |
| `len()`                | Count allocated and unallocated courses   |
| If-else                | Determine final allocation status         |

## 9. Result

The Python program successfully implements a Smart Classroom Timetable Allocation System using lists and tuples. It validates classroom capacities, prevents classroom scheduling clashes, allocates courses to available periods, identifies unallocated courses, and determines whether all courses can be accommodated.

