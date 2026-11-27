n = int(input("Enter a number (1 to 100): "))
prime = n > 1
for i in range(2, n):
    if n % i == 0:
        prime = False
        break
print("Prime number" if prime else "Not a prime number")
