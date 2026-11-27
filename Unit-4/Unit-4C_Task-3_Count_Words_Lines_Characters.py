filename = input("Enter file name: ")
try:
    with open(filename, "r") as file:
        content = file.read()
    lines = content.splitlines()
    words = content.split()
    print("Lines:", len(lines))
    print("Words:", len(words))
    print("Characters:", len(content))
except FileNotFoundError:
    print("File not found.")
