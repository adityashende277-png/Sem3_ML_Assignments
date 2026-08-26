employees = [
    ("Ravi", 55000),
    ("Sita", 72000),
    ("Amit", 48000)
]

sorted_employees = sorted(
    employees,
    key=lambda x: x[1],
    reverse=True
)

for name, salary in sorted_employees:
    print(f"{name} earns Rs. {salary}")