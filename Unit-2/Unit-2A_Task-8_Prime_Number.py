n = int(input("Enter a number (1 to 100): "))
is_prime = n > 1
for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break
print("Prime number" if is_prime else "Not a prime number")
