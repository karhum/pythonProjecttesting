# grade scale

points = int(input("Exam point:\n"))

if points < 0:
    print("Invalid points value.")
elif points == 0:
    print("Grade: 0")
elif 1 <= points <= 50:
    print("Grade: 0")
elif points <= 60:
    print("Grade: 1")
elif points <= 70:
    print("Grade: 2")
elif points <= 80:
    print("Grade: 3")
elif points <= 90:
    print("Grade: 4")
elif points <= 100:
    print("Grade: 5")
else:
    print("Invalid points value.")