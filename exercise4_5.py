# student discount

student = input("Are you a student? (y/n)\n")

# ask the month of the travel
month = int(input("In which month you will travel? (1-12)\n"))

student = student.lower()

if student == "y" and not 6 <= month <= 8:
    special_price = True
else:
    special_price = False

if special_price:
    print("Special price!")
else:
    print("Normal price.")