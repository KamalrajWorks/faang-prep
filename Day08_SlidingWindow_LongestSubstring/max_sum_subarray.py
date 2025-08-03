def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return "Invalid: window size is larger than array"
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum

arr = [2, 1, 5, 1, 3, 2]
k = 3
print("Maximum sum of a subarray of size", k, "is:", max_sum_subarray(arr, k))
