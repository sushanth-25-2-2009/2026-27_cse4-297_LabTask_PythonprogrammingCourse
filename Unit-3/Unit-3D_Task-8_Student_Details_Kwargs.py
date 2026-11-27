def student_details(**marks):
    for subject, mark in marks.items():
        print(subject, ":", mark)

student_details(name="Anu", Mathematics=90, Python=95, English=88)
