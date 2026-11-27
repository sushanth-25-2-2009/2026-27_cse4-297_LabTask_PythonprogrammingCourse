text = input("Enter a line to write: ")
with open("output.txt", "w") as file:
    file.write(text + "\n")
print("Text written to output.txt")
