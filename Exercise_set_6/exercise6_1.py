# Positive integers x 5

biggest = 0

for i in range(5):
    number = int(input("Give a number: \n"))
    if number <= 0:
        print("Give positive integer, please.")
    if number > biggest:
        biggest = number

print(f"The biggest number from user: {biggest}")
