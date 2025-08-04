def first_repeated_char(s):
    seen = set()
    for ch in s:
        if ch in seen:
            return ch
        seen.add(ch)
    return None

s = input("Enter a string: ")
result = first_repeated_char(s)
if result:
    print("First repeated character:", result)
else:
    print("No repeated characters found")
