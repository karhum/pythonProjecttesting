import math
# radius

while True:
    radius = int(input("Give radius:\n"))
    area = math.pi * radius ** 2
    area = round(area, 2)
    print(f"Circle area: {area}")
    is_yes = input("Do you want to continue? y/n\n").lower()
    if is_yes != "y":
        break
