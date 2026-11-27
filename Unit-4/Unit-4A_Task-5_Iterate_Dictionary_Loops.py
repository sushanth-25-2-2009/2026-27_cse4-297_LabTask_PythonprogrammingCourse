marks = {"Python": 95, "Maths": 90, "English": 88}
print("Keys:")
for subject in marks.keys():
    print(subject)
print("Values:")
for mark in marks.values():
    print(mark)
print("Items:")
for subject, mark in marks.items():
    print(subject, ":", mark)
