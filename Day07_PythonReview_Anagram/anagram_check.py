# anagram_check.py
# Program to check if two strings are anagrams using HashMap

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in t:
        if ch not in freq or freq[ch] == 0:
            return False
        freq[ch] -= 1

    return True


# Test
s = input("Enter first string: ")
t = input("Enter second string: ")

if isAnagram(s, t):
    print("The strings are Anagrams ✅")
else:
    print("The strings are NOT Anagrams ❌")
