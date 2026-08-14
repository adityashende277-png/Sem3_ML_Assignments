def validate_username(username):
    username = username.strip()
    if len(username) < 5:
        return "Invalid"
    if not username.isalnum():
        return "Invalid"
    return username.lower()