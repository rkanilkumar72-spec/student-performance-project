import csv
import random

with open("students.csv", "w", newline="") as file:

  
    writer = csv.writer(file)
    writer.writerow([
        "Student_ID",
        "Name",
        "Department",
        "Attendance",
        "Marks",
        "Result"
    ])

    for i in range(1, 20001):

        student_id = i
        name = "Student_" + str(i)

        department = random.choice([
            "CSD",
            "ISE",
            "CSE",
            "ECE"
        ])

        attendance = random.randint(50, 100)
        marks = random.randint(0, 100)

        if marks >= 35:
            result = "Pass"
        else:
            result = "Fail"

        writer.writerow([
            student_id,
            name,
            department,
            attendance,
            marks,
            result
        ])

print("Student dataset created successfully!")
print("Total student records: 20000")