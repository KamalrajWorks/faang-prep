def first_unique_index(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i
    return -1

s = input("Enter a String: ")
print("Index of first non-repeating character:", first_unique_index(s))
