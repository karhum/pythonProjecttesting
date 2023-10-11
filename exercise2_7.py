import math
# ex. 7 The quadratic equation

a = float(input("Give value for a:\n"))
b = float(input("Give value for b:\n"))
c = float(input("Give value for c:\n"))

discriminant = b ** 2 - 4 * a * c
if discriminant < 0:  # no real answer
    print(f"No result")
elif discriminant == 0:  # one real answer
    equation = -b / 2 * a
    print(f"Result is {equation}")
elif discriminant > 0:  # two real answers
    equation = -b + math.sqrt(discriminant) / 2 * a
    equation2 = -b - math.sqrt(discriminant) / 2 * a
    print(f"Result is {equation}")
