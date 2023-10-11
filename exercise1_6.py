# Ex. 6 The cents

# PART 1 Apply the amount of cents
cents = int(input("How many cents? (1-100):\n"))

# PART 2 The calculation
cents50 = cents // 50
cents = cents % 50
cents20 = cents // 20
cents = cents % 20
cents10 = cents // 10
cents = cents % 10
cents5 = cents // 5
cents = cents % 5
cents2 = cents // 2
cents1 = cents % 2

# PART 3 Printing the outcome
print(f"Amount of 50 cents: {cents50}")
print(f"Amount of 20 cents: {cents20}")
print(f"Amount of 10 cents: {cents10}")
print(f"Amount of 5 cents: {cents5}")
print(f"Amount of 2 cents: {cents2}")
print(f"Amount of 1 cents: {cents1}")
