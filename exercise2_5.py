import random
# ex.5 random number

r_number = random.randint(1, 10)
print(f"Random number: {r_number}")

side_1 = random.randint(2, 10)
side_2 = random.randint(2, 10)

add = side_1 * side_2
print(f"First random side: {side_1}")
print(f"Second random side: {side_2}")
print(f"Rectangle area: {add}")
