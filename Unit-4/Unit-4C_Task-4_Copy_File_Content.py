try:
    with open("sample.txt", "r") as source:
        content = source.read()
    with open("copy.txt", "w") as destination:
        destination.write(content)
    print("Content copied to copy.txt")
except FileNotFoundError:
    print("sample.txt was not found.")
