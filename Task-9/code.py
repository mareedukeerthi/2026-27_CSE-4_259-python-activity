

courses = [
    ("C101", 40),
    ("C102", 30),
    ("C103", 50),
    ("C104", 25),
    ("C105", 60)
]


classrooms = [
    ("R101", 40),
    ("R102", 35),
    ("R103", 55)
]


periods = ["9AM-10AM", "10AM-11AM", "11AM-12PM"]


timetable = []


unallocated = []

print("===== SMART CLASSROOM TIMETABLE ALLOCATION =====")

for course_id, strength in courses:

    allocated = False

    for period in periods:

        for room_id, capacity in classrooms:

            
            if capacity >= strength:

             
                clash = False

                for allocation in timetable:
                    if allocation[1] == room_id and allocation[2] == period:
                        clash = True
                        break

              
                if not clash:
                    timetable.append(
                        (course_id, room_id, period, strength)
                    )

                    allocated = True
                    break

        if allocated:
            break

    if not allocated:
        unallocated.append(course_id)


print("\n========== ALLOCATED TIMETABLE ==========")

if timetable:
    for course_id, room_id, period, strength in timetable:
        print("Course ID       :", course_id)
        print("Classroom       :", room_id)
        print("Time Period     :", period)
        print("Student Strength:", strength)
        print("----------------------------------------")
else:
    print("No courses allocated.")

print("\n========== UNALLOCATED COURSES ==========")

if unallocated:
    for course in unallocated:
        print(course)
else:
    print("All courses allocated successfully.")


print("\n========== FINAL REPORT ==========")
print("Total Courses     :", len(courses))
print("Allocated Courses :", len(timetable))
print("Unallocated       :", len(unallocated))


if len(unallocated) == 0:
    print("Status: All courses accommodated.")
else:
    print("Status: All courses cannot be accommodated.")

print("==================================")

