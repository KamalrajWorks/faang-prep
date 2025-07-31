def majority_element(nums):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
        if freq[num] > len(nums) // 2:
            return num
    return None

nums = [3, 3, 4, 2, 3, 3, 3]
print("Majority Element:", majority_element(nums))
