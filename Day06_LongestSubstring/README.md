# Day 06 - Longest Substring Without Repeating Characters

## 📌 Problem Statement
Given a string `s`, find the length of the **longest substring** 
without repeating characters.

This is a popular FAANG interview problem that tests:
- Understanding of **sliding window technique**
- Use of **HashMap (dictionary) for optimization**
- Ability to reason about **time & space complexity**

---

## 🚀 Approaches

### 1. Sliding Window with Set
- Use a `set` to store unique characters.
- If a duplicate is found, shrink the window from the left.
- Keep track of the maximum window size.

**Time Complexity:** O(n)  
**Space Complexity:** O(min(n, alphabet_size))

---

### 2. Sliding Window with HashMap (Optimized)
- Use a dictionary to store the **last index** of each character.
- When a duplicate is found, directly move the left pointer 
  to `last_index + 1` (jump instead of step-by-step).
- More efficient for large inputs.

**Time Complexity:** O(n)  
**Space Complexity:** O(min(n, alphabet_size))

---

## 🖥️ Code
See the file 👉 `Day06_DSA_LongestSubstring.py`

---

## 🧪 Example

Input:
