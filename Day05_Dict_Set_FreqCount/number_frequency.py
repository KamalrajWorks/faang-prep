def count_frequency(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    return freq

nums = [2, 5, 2, 8, 5, 6, 8, 8]
print("Number frequency:", count_frequency(nums))
