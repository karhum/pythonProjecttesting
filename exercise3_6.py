# leap year

year = int(input("Give year:\n"))

if year % 400 == 0:
    print("Leap year: YES")
elif year % 100 == 0:
    print("Leap year: NO")
elif year % 4 == 0:
    print("Leap year: YES")
else:
    print("Leap year: NO")
