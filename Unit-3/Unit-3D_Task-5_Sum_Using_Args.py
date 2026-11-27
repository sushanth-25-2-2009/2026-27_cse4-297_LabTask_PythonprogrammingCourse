def find_sum(*args):
    total = 0
    for value in args:
        total += value
    return total

print("Sum:", find_sum(10, 20, 30, 40))
