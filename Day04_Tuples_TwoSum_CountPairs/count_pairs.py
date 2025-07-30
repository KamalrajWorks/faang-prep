# Count Pairs with Given Sum using Hash Map

def count_pairs(nums, target):
    hashmap = {}
    count = 0
    for num in nums:
        diff = target - num
        if diff in hashmap:
            count += hashmap[diff]
        hashmap[num] = hashmap.get(num, 0) + 1
    return count

# ---- Main Program ----
n = int(input("Enter size of array: "))
nums = []
for _ in range(n):
    nums.append(int(input("Enter element: ")))

target = int(input("Enter target sum: "))
print("Number of pairs:", count_pairs(nums, target))
