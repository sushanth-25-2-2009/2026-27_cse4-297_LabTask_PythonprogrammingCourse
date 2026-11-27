try:
    numerator = float(input("Enter numerator: "))
    denominator = float(input("Enter denominator: "))
    print("Result:", numerator / denominator)
except ZeroDivisionError:
    print("Error: Denominator cannot be zero.")
except ValueError:
    print("Error: Enter valid numbers.")
