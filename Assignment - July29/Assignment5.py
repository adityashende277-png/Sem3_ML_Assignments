def is_palindrome(sentence):
    clean = ""

    for char in sentence:
        if char.isalnum():
            clean += char.lower()

    return clean == clean[::-1]


sentence = "Was it a car or a cat I saw?"

print(is_palindrome(sentence))