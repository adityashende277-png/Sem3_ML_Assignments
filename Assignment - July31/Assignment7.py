sales = {"mon": 200, "tue": 350, "wed": 200}

inverted = {}

for day, value in sales.items():
    if value in inverted:
        inverted[value].append(day)
    else:
        inverted[value] = [day]

print(inverted)