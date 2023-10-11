# EX. 4
# 5.1 liters per 100 km outside urban area and
# #7.5 liters per 100 km within an urban area

km_out = float(input("Kilometers outside urban area:\n"))
km_in = float(input("Kilometers within urban area: \n"))

consumption = round(km_out / 100 * 5.1 + km_in / 100 * 7.5, 2)
print(f"Consumption: {consumption} l")
