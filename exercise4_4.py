# Divider
try:
    num_1 = int(input("First number: \n"))

    num_2 = int(input("Second number: \n"))
    print(num_1 / num_2)
except ValueError:
    print("Incorrect format.")
except ZeroDivisionError:
    print("You can't divide by zero!")
