# the cashier

given_money = int(input("Give money:\n"))
cost = int(input("Purchase cost:\n"))
change = cost - given_money
if given_money >= cost:
    print(f"Thank you. Here's the change: {change*-1} €")
else:
    extra = int(input(f"Not enough money, give more:\n"))
    change = cost - (given_money + extra)
    if given_money + extra >= cost:
        print(f"Thank you. Here's the change: {change*-1} €")
    else:
        print("You don't have enough money.")
