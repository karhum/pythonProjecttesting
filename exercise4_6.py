# Weather

# base conditioning
freezing = False
heatwave = False
raining = False
hailstorm = False

# Q's in app
temp = int(input("How many celsius degrees there are today?\n"))
humidity = int(input("What is the humidity percentage today?\n"))

if temp < 0:
    freezing = True
    print("It's freezing outside.")

if humidity >= 80:
    raining = True
    if raining and temp < -20:
        hailstorm = True
        print("There's a hailstorm, be careful!")
    else:
        print("It's raining.")

if temp > 20:
    heatwave = True
    print("Heatwave! Remember to hydrate!")
    if raining:
        print("It's damp and hot.")
