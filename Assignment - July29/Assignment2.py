def reverse_code(secret_code):
    words = secret_code.split("-")
    words.reverse()
    
    return " ".join(words).upper()


secret_code = "charlie-bravo-alpha"

print(reverse_code(secret_code))