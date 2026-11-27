student = {
    "name": input("Enter student name: "),
    "marks": float(input("Enter marks: ")),
    "grade": input("Enter grade: ")
}
print("Student record:")
for key, value in student.items():
    print(key, ":", value)
