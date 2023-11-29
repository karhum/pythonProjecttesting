file_handle = open("weekdays.txt", "r")

content = file_handle.read()



# make it a list
lines = content.split("\n")

print(lines)

amount = len(lines)

for index in range(amount):
    line = lines[index]
    print(f"{index + 1}.{line}")
