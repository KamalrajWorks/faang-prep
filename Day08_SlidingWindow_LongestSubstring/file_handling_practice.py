# File Handling Practice

# Writing data to a file
with open("student_data.txt", "w") as file:
    file.write("Name,Age,Department\n")
    file.write("Kamal,21,CSE\n")
    file.write("Arjun,20,ECE\n")
    file.write("Priya,22,IT\n")

print("Data written to student_data.txt")

# Reading data from the file
with open("student_data.txt", "r") as file:
    content = file.read()
    print("\nReading from student_data.txt:")
    print(content)

# Appending more data
with open("student_data.txt", "a") as file:
    file.write("Vikram,23,EEE\n")

print("\nNew data appended to student_data.txt")

# Reading again after append
with open("student_data.txt", "r") as file:
    print("\nUpdated file content:")
    print(file.read())
