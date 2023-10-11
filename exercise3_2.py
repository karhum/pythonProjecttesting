# temperature feedback

temp = int(input("Give the temperature:\n"))

if temp < 0:
    pass
elif temp <= 10:
    print("COLD")
elif temp <= 15:
    print("CHILLY")
elif temp <= 20:
    print("NORMAL TEMPERATURE")
elif temp <= 25:
    print("WARM")
elif temp <= 30:
    print("HOT")
