try:
    number = int(input("Enter an integer: "))
except ValueError:
    print("Invalid integer.")
else:
    print("Square =", number ** 2)
finally:
    print("Program finished")
