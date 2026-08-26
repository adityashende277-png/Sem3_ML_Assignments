sentence = "Python is a very powerful language"

words = sentence.split()

total_words = len(words)

vowel_count = 0

for word in words:
    if word[-1].lower() in "aeiou":
        vowel_count += 1

longest_word = words[0]

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("Total words:", total_words)
print("Words ending with vowel:", vowel_count)
print("Longest word:", longest_word)