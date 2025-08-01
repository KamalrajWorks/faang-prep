"""
Day 06 - Longest Substring Without Repeating Characters
------------------------------------------------------
Problem:
Given a string s, find the length of the longest substring 
without repeating characters.

Approaches:
1. Sliding Window with Set
2. Sliding Window with HashMap (Optimized)
"""

# -------------------------------------------------------
# 1. Sliding Window with Set
# -------------------------------------------------------
def longest_substring_set(s):
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len


# -------------------------------------------------------
# 2. Sliding Window with HashMap (Optimized)
# -------------------------------------------------------
def longest_substring_hashmap(s):
    char_index = {}  # stores last index of each character
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            # Jump left to skip duplicate
            left = char_index[char] + 1
        char_index[char] = right
        max_len = max(max_len, right - left + 1)

    return max_len


# -------------------------------------------------------
# Run the program
# -------------------------------------------------------
if __name__ == "__main__":
    s = input("Enter a string: ")

    print("\nUsing Set:")
    print("Length of longest substring:", longest_substring_set(s))

    print("\nUsing HashMap:")
    print("Length of longest substring:", longest_substring_hashmap(s))
