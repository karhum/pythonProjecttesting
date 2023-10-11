# working hours and the wage

hours = int(input("How many workhours this week?\n"))
salary = int(input("Your hourly salary?\n"))

wage = hours * salary
wage = round(wage, 2)
if hours <= 40:
    print(f"Your weekly wage: {wage}€")
else:
    wage = wage + (hours - 40) * 0.5 * salary
    print(f"Your weekly wage: {wage}€")
