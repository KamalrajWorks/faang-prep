# review_exercise.py
# Mini exercise mixing lists, tuples, and dicts

students = [
    ("Kamal", 21, "CSE"),
    ("Arjun", 20, "ECE"),
    ("Priya", 22, "IT"),
]

# Convert list of tuples to a dictionary {name: department}
student_dict = {name: dept for name, age, dept in students}

print("Dictionary of students:", student_dict)

# Print all names from CSE department
print("Students in CSE:", [name for name, dept in student_dict.items() if dept == "CSE"])
