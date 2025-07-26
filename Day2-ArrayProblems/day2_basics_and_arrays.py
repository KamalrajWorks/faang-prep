# Day 2 – Python Basics + Array Practice

# -------- Control Flow (If-Else) --------
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# -------- For Loop Example --------
print("\nNumbers divisible by 3 between 1 and 50:")
for i in range(1, 51):
    if i % 3 == 0:
        print(i, end=" ")

# -------- While Loop Countdown --------
print("\n\nCountdown using while loop:")
n = 5
while n > 0:
    print(n)
    n -= 1

# -------- Factorial using for loop --------
num = int(input("\nEnter a number to find factorial using for loop: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial (for):", factorial)

# -------- Factorial using while loop --------
num = int(input("Enter a number to find factorial using while loop: "))
factorial = 1
i = 1
while i <= num:
    factorial *= i
    i += 1
print("Factorial (while):", factorial)

# -------- Multiplication Table --------
num = int(input("Enter a number for multiplication table: "))
print(f"Multiplication table of {num}")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# -------- Array Input and Operations --------
n = int(input("\nEnter the number of elements in array: "))
a = []
for i in range(n):
    a.append(int(input("Enter element: ")))

print("Array:", a)

maximum = a[0]
minimum = a[0]
total = 0
for i in a:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i
    total += i

print("Maximum:", maximum)
print("Minimum:", minimum)
print("Sum:", total)
