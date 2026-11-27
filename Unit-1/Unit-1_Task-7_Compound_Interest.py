p = float(input("Enter principal amount: "))
r = float(input("Enter annual rate of interest: "))
t = float(input("Enter time in years: "))
amount = p * (1 + r / 100) ** t
print("Compound interest =", amount - p)
print("Total amount =", amount)
