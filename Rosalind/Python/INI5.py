file = open("input.txt", "r")

print("".join([line for i, line in enumerate(file.readlines()) if i % 2 == 1]))