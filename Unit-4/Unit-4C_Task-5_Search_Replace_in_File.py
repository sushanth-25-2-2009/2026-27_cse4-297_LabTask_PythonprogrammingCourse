filename = input("Enter file name: ")
old_word = input("Word to replace: ")
new_word = input("New word: ")
try:
    with open(filename, "r") as file:
        content = file.read()
    content = content.replace(old_word, new_word)
    with open(filename, "w") as file:
        file.write(content)
    print("File updated successfully.")
except FileNotFoundError:
    print("File not found.")
