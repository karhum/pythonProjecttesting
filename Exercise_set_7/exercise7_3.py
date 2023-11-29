shopcart = [
     {"name": "Beehive - lamp", "price": 999.9},
     {"name": "Malm - bed", "price": 169.9},
     {"name": "Moomin - mug set", "price": 59.9},
     {"name": "Nemo - divan", "price": 699.9},
     {"name": "Ritz - armchair", "price": 369.9}
]
total = 0
print("Receipt:")
for furniture in shopcart:
    total += furniture["price"]
    print(f" - {furniture['name']}")

print()
print(f"Total sum: {total} €.\nPlease come again!")

vat = total - (total / 1.24)
vat = round(vat, 2)
print()
print(f"{vat} €.")
      