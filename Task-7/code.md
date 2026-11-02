# Campus Resource Allocation Under Constraints

## 1. Problem Statement

Develop a Python program to manage and allocate available campus resources among multiple activities based on their equipment requirements and priority order.

The program should perform the following operations:

- Accept the total available quantity of different campus resources, such as projectors, laptops, microphones, and chairs.
- Accept equipment requirements for multiple campus activities.
- Assign priorities to activities.
- Compare the required resources with the available resources.
- Calculate resource shortages for each activity.
- Allocate resources according to the specified priority order.
- Ensure that allocated resources do not exceed the available quantities.
- Display the final allocation, shortages, and unallocated requirements.

The objective is to maximize resource utilization and provide a feasible allocation while respecting resource availability and activity priorities.

## 2. Algorithm

1. Start the program.
2. Read the number of available resource types.
3. Accept the resource names and their available quantities.
4. Read the number of campus activities.
5. Accept the following details for each activity:
   - Activity name
   - Priority number
   - Required quantity of each resource.
6. Store the activity details in a list.
7. Sort activities according to priority order (highest priority first).
8. Initialize allocated resources to zero.
9. For each activity:
   - Compare its requirements with the remaining available resources.
   - Allocate resources if sufficient quantities are available.
   - Calculate shortages if resources are insufficient.
   - Update the remaining resource quantities.
10. Display the allocation details for every activity.
11. Display shortages for each activity.
12. Display the remaining available resources.
13. Display the final allocation summary.
14. Stop the program.


## 5. Sample Input

Consider three available resource types: projectors, laptops, and microphones.

There are three campus activities with different priorities.

```
Enter number of resource types: 3

Enter available resources:
Resource name: projector
Available quantity: 5

Resource name: laptop
Available quantity: 10

Resource name: microphone
Available quantity: 6

Enter number of activities: 3

Enter details for Activity 1
Activity name: Technical Workshop
Priority (1 = Highest): 1
Required projector: 3
Required laptop: 6
Required microphone: 4

Enter details for Activity 2
Activity name: Cultural Event
Priority (1 = Highest): 2
Required projector: 4
Required laptop: 5
Required microphone: 4

Enter details for Activity 3
Activity name: Seminar
Priority (1 = Highest): 3
Required projector: 2
Required laptop: 3
Required microphone: 2
```

## 6. Sample Output

```
--- RESOURCE ALLOCATION REPORT ---

Activity: Technical Workshop
Priority: 1
Allocated Resources:
projector: 3
laptop: 6
microphone: 4
Resource Shortages:
No shortages

Activity: Cultural Event
Priority: 2
Allocated Resources:
projector: 2
laptop: 4
microphone: 2
Resource Shortages:
projector: 2
laptop: 1
microphone: 2

Activity: Seminar
Priority: 3
Allocated Resources:
projector: 0
laptop: 0
microphone: 0
Resource Shortages:
projector: 2
laptop: 3
microphone: 2

--- FINAL RESOURCE SUMMARY ---

Initially Available Resources:
projector: 5
laptop: 10
microphone: 6

Allocated Resources:
projector: 5
laptop: 10
microphone: 6

Remaining Resources:
projector: 0
laptop: 0
microphone: 0

Campus resource allocation completed.
```

## 7. Mermaid Flowchart Code
``` mermaid

flowchart TD
    A([Start]) --> B[/Enter available resource types and quantities/]
    B --> C[/Enter number of activities/]
    C --> D[/Input activity names, priorities and requirements/]
    D --> E[Store activity details]
    E --> F{More activities?}
    F -->|Yes| D
    F -->|No| G[Sort activities by priority]
    G --> H[Initialize remaining resources]
    H --> I[Select next activity]
    I --> J[Compare requirements with available resources]
    J --> K[Allocate minimum of required and available]
    K --> L[Calculate resource shortages]
    L --> M[Update remaining resources]
    M --> N{More activities?}
    N -->|Yes| I
    N -->|No| O[Display allocation report]
    O --> P[Display shortage report]
    P --> Q[Display remaining resources]
    Q --> R([Stop])

```

## 8. Result

The Python program successfully manages campus resource allocation under availability constraints.

It compares equipment requirements with available resources, sorts activities according to priority, allocates resources to higher-priority activities first, calculates shortages, and displays the remaining resources.

Time Complexity: \\(O(m \log m + m \times n)\\)

Where:

- \\(m\\) = Number of campus activities.
- \\(n\\) = Number of resource types.

Space Complexity: \\(O(m \times n)\\), for storing activity requirements and allocation details.

Conclusion: The program provides an effective priority-based resource allocation system that helps educational institutions distribute limited campus resources fairly according to specified priorities.
