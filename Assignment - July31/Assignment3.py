username = "  Rahul_123  "

username = username.strip().lower()

if (5 <= len(username) <= 12 and
        username[0].isalpha() and
        username.isalnum()):
    print("Valid username")
else:
    print("Invalid username")