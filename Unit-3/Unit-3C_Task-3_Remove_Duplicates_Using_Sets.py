numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
unique = list(set(numbers))
print("List without duplicates:", unique)
