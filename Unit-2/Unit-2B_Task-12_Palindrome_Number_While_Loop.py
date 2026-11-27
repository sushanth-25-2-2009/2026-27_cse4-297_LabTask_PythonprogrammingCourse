n = int(input("Enter an integer: "))
original = n
temp = abs(n)
reverse = 0
while temp > 0:
    reverse = reverse * 10 + temp % 10
    temp //= 10
if original >= 0 and original == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome number")
