def simple_interest(principal, time, rate=5):
    return principal * time * rate / 100

p = float(input("Enter principal: "))
t = float(input("Enter time in years: "))
print("Using default rate (5%):", simple_interest(p, t))
r = float(input("Enter another rate: "))
print("Using entered rate:", simple_interest(p, t, r))
