from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]
squares = list(map(lambda x: x * x, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
total = reduce(lambda x, y: x + y, numbers)
print("Original:", numbers)
print("Squares using map:", squares)
print("Even numbers using filter:", evens)
print("Sum using reduce:", total)
