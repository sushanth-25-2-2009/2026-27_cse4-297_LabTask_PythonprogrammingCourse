try:
    with open("sample.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("sample.txt was not found. Create it in the same folder as this program.")
