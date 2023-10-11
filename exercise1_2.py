# Ex. 2 Calculate the VAT

price = float(input("Give the price without VAT:\n"))

price = int(price)
price = price * 1.24
price = round(price, 2)

print(f"Price with VAT: {price} €")
