students = {
    1: {"name": "Nagesh", "age":19},
    2: {"name": "Mahesh", "age":43},
    3: {"name": "Deepak", "age":14},
    4: {"name": "Sai", "age":23},
    5: {"name": "Tanush", "age":90}

}
for student_id, details in students.items():
    print(f"Student ID: {student_id}, Name: {details['name']}, Age: {details['age']}")