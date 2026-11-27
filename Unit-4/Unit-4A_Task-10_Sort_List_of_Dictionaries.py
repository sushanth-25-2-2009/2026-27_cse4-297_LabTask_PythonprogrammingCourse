students = [
    {"name": "Anu", "marks": 88},
    {"name": "Ravi", "marks": 95},
    {"name": "Kiran", "marks": 78}
]
ascending = sorted(students, key=lambda student: student["marks"])
descending = sorted(students, key=lambda student: student["marks"], reverse=True)
print("Ascending order:", ascending)
print("Descending order:", descending)
