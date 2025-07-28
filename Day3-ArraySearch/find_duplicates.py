# Day 3 - Find Duplicates in Array using Dictionary

def find_duplicates(arr):
    seen = {}
    duplicates = []
    for num in arr:
        if num in seen:
            duplicates.append(num)
        else:
            seen[num] = 1
    return list(set(duplicates))

a = [1, 2, 3, 2, 4, 5, 1, 3]
print("Array:", a)
print("Duplicates:", find_duplicates(a))
