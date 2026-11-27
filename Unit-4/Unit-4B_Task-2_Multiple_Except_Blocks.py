items = [10, 20, 30]
try:
    index = int(input("Enter list index: "))
    print("Value:", items[index])
except ValueError:
    print("Please enter an integer index.")
except IndexError:
    print("Index is outside the list.")
