# print the bigger number

number_1 = int(input("Give first number:\n"))
number_2 = int(input("Give second number:\n"))

if number_1 == number_2:
    print("Numbers are equal.")
elif number_1 > number_2:
    print(f"Bigger number = {number_1}")
else:
    print(f"Bigger number = {number_2}")
