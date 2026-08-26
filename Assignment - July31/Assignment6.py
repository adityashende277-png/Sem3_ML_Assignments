sentence = "python is fun and python is easy"

words = sentence.lower().split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

result = sorted(
    frequency.items(),
    key=lambda x: x[1],
    reverse=True
)

print("Word:", result[0][0])
print("Frequency:", result[0][1])