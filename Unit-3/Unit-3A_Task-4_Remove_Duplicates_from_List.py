numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
unique = []
for item in numbers:
    if item not in unique:
        unique.append(item)
print("List without duplicates:", unique)
