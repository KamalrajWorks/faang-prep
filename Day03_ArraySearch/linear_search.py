# Day 3 - Linear Search in Array

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

a = [10, 20, 30, 40, 50]
x = int(input("Enter the number to search: "))

result = linear_search(a, x)
if result != -1:
    print(x, "found at index", result)
else:
    print(x, "not found")
    