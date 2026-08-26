test1 = {"amit": 40, "bina": 35}
test2 = {"amit": 30, "chirag": 45}

result = {}

for name, marks in test1.items():
    result[name] = marks

for name, marks in test2.items():
    if name in result:
        result[name] += marks
    else:
        result[name] = marks

print(result)