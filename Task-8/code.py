

students = [
    ("S101", "Arun", 85, 92, "Python"),
    ("S102", "Bala", 78, 88, "Java"),
    ("S103", "", 105, 75, "Python"),
    ("S101", "Divya", 90, 95, "C++"),
    ("S105", "Kiran", 65, 110, ""),
    ("S106", "Ravi", None, 80, "Java"),
    ("S107", "Meena", 95, 98, "Python")
]


student_ids = set()


valid_count = 0
invalid_count = 0

print("===== STUDENT RECORD CONSISTENCY CHECKER =====")

for student in students:

    student_id, name, marks, attendance, course = student

    errors = []

    
    if not student_id:
        errors.append("Missing Student ID")
    elif student_id in student_ids:
        errors.append("Duplicate Student ID")
    else:
        student_ids.add(student_id)

   
    if not isinstance(name, str) or not name.strip():
        errors.append("Missing Student Name")

    if marks is None:
        errors.append("Missing Marks")
    elif not isinstance(marks, (int, float)):
        errors.append("Invalid Marks Format")
    elif marks < 0 or marks > 100:
        errors.append("Marks must be between 0 and 100")

    
    if attendance is None:
        errors.append("Missing Attendance")
    elif not isinstance(attendance, (int, float)):
        errors.append("Invalid Attendance Format")
    elif attendance < 0 or attendance > 100:
        errors.append("Attendance must be between 0 and 100")

    
    if not isinstance(course, str) or not course.strip():
        errors.append("Missing Course Record")

   
    print("\nStudent ID:", student_id)
    print("Name:", name)
    print("Marks:", marks)
    print("Attendance:", attendance)
    print("Course:", course)

    if len(errors) == 0:
        print("Status: VALID")
        valid_count += 1
    else:
        print("Status: INVALID")
        for error in errors:
            print("Error:", error)

        invalid_count += 1


print("\n========== CONSISTENCY REPORT ==========")
print("Total Student Records :", len(students))
print("Valid Records         :", valid_count)
print("Invalid Records       :", invalid_count)
print("========================================")

