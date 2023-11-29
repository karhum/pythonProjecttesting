# Rain amount

rain_amount_total = 0

for x in range(12):
    rain_amount = int(input("Give rain amount of month:\n"))
    rain_amount_total = rain_amount_total + rain_amount

average = rain_amount_total / 12
print(f"Year average for rain = {average} mm")
