# Day 3 - Python Functions Practice

# Recursive Factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number for factorial: "))
print("Factorial is:", factorial(num))


# Find Maximum in List
def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

a = [2, 9, 1, 6]
print("Maximum is:", find_max(a))
