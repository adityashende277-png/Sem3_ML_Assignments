def format_phone(raw_num):
    digits = ""

    for char in raw_num:
        if char.isdigit():
            digits += char

    if len(digits) != 10:
        return "Invalid Number"

    return "(" + digits[:3] + ") " + digits[3:6] + "-" + digits[6:]


raw_num = "555-987-6543"

print(format_phone(raw_num))