# Ex. 3 Calculate the gasolin consumption

km = float(input("Give the trip length: \n"))
km = int(km)
km = km / 100 * 6.5
km = round(km, 1)

print(f"Consumption: {km} l")
