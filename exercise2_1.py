import math
# EX. 1 PART a) Calculating box sides
side1 = float(input("Give the first side:\n"))
side2 = float(input("Give the second side:\n"))
side3 = float(input("Give the third side:\n"))

volume = side3 * side1 * side2
volume = round(volume, 2)
print(f"Box volume: {volume}")

# PART b) Calculating sphere
radius = float(input("Give the sphere radius:\n"))
volume = 4 / 3 * math.pi * radius ** 3
volume = round(volume, 2)

print(f"Sphere volume: {volume} m3")