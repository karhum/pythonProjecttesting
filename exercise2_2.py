import math
# EX. 2 Triangle

side_a = float(input("Give the first leg: \n"))
side_b = float(input("Give the second leg: \n"))

hypotenuse = math.sqrt(side_a ** 2 + side_b ** 2)
hypotenuse = round(hypotenuse, 2)
print(f"Hypotenuse: {hypotenuse} m")
