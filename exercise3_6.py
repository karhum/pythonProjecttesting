# leap year

year = int(input("Give year:\n"))

if year % 400:
    print("Leap year: YES")
    if year % 100:
        print("Leap year: NO")
    if year % 4:
        print("Leap year: YES")
    if not year % 4:
        print("Leap year: NO")
