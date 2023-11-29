# tuple of months

months = ("January", "February", "March", "April",
          "May", "June", "July", "August", "September",
          "October", "November", "December")

number = int(input("Give the number of a month: 1-12\n"))
number -= 1

print(months[number])
