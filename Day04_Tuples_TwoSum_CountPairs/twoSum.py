# Two Sum Problem using Hash Map (Dictionary)

def two_sum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[num] = i
    return []

# ---- Main Program ----
n = int(input("Enter the size of the array: "))
nums = []
for _ in range(n):
    nums.append(int(input("Enter element: ")))

target = int(input("Enter the target: "))
result = two_sum(nums, target)

if result:
    print("Indices:", result)
else:
    print("No pair found")
