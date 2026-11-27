first = input("Enter first string: ").replace(" ", "").lower()
second = input("Enter second string: ").replace(" ", "").lower()
if sorted(first) == sorted(second):
    print("Anagrams")
else:
    print("Not anagrams")
