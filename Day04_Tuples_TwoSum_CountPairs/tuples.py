students = (
    ("Kamal", 21, "CSE"),
    ("Arjun", 20, "ECE"),
    ("Priya", 22, "IT")
)

for i in range(len(students)):
    name, age, dept = students[i]
    print(f"Student {i+1} : Name: {name}, Age: {age}, Department: {dept}")