# difficult exercise

postage = input("Are you sending a letter or a parcel? L/P\n")
postage = postage.lower()

if postage == "l":
    letter = True
else:
    letter = False

size = int(input("What is the size of your postage in grams?\n"))

if letter:
    if size < 200:
        print("Prize is 0.5€, please.")
    elif size <= 500:
        size_small = 0.5 + 0.04 * (size // 100)
        print(f"The price is {size_small} €, please.")
    elif size > 500:
        letter_big = input("Does your letter fit into the mailbox? Y/N\n")
        letter_big = letter_big.lower()
        size_big = 0.5 + 0.07 * (size // 100)
        if letter_big == "y":
            print(f"The price is {size_big} €, please.")
        else:
            print(f"The price is {size_big + 2} €, please.")
else:
    if size < 200:
        print("Prize is 2 €, please.")
    elif size <= 500:
        size_small = 2 + 0.08 * (size // 100)
        print(f"The price is {size_small} €, please.")
    elif size > 500:
        size_big = 2 + 0.14 * (size // 100)
        print(f"The price is {size_big} €, please.")
