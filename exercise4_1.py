from datetime import date, datetime

# Exact mission

name = "John Doe"
year = 1984
balance = 345
time = date.today
date_txt = date.today().strftime("%d.%m.%Y.")

txt = f"{name} ({year}), balance: {balance} €, updated on {date_txt}"

print(txt)
