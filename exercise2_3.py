# EX. 3 Income and tax
salary = float(input("Your monthly salary: \n"))
tax = float(input("Your tax percentage: \n"))

earnings = round(salary * (100 - tax) / 100, 2)
print(f"Earnings: {earnings} €")
taxes = round(salary * tax / 100, 2)
print(f"Taxes: {taxes} €")
