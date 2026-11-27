students = {
    1: {"name": "Anu", "marks": 90},
    2: {"name": "Ravi", "marks": 85},
    3: {"name": "Kiran", "marks": 95}
}
for roll, details in students.items():
    print("Roll:", roll, "Name:", details["name"], "Marks:", details["marks"])
