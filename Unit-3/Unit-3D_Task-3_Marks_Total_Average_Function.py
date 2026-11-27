def calculate(m1, m2, m3):
    total = m1 + m2 + m3
    average = total / 3
    return total, average

a = float(input("Enter subject 1 marks: "))
b = float(input("Enter subject 2 marks: "))
c = float(input("Enter subject 3 marks: "))
total, average = calculate(a, b, c)
print("Total:", total)
print("Average:", average)
