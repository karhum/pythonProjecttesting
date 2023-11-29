# While and for-loops

number = 1

while number <= 50:
    print(number)

    number = number + 1

for x in range(1, 51):
    # this is the line we ask Python to run 10 times in a row
    print(x)

total = 0
for x in range(31):
    # this is the line we ask Python to run 10 times in a row
    total = total + x
print(total)

no_space = ""

for x in range(2005, 2011):
    print(x, end=" ")
