text = "Aba c"

frequency = {}

for char in text.lower():
    if char != " ":
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

print(frequency)