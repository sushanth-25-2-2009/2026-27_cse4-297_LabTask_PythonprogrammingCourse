def to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

c = float(input("Enter Celsius: "))
print("Fahrenheit:", to_fahrenheit(c))
