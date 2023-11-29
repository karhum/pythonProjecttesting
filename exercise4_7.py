# Numbers into words and other way around

digits = input("Please type max 5 numbers:\n")
if len(digits) > 5:
    raise ValueError("Too many digits.")
elif not digits.isnumeric():
    raise TypeError("Please use numbers.")

numbers = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero"
}

for d in digits:
    print(numbers[d], end = " ")

"""
txt = ""
for d in digits:
    txt = f"{txt}{numbers[d]} "
print(txt)
"""
"""
txt = []
for d in digits:
    txt.append(numbers[d])
print(" ".join(txt))
"""
"""
characters = input("Please type in numbers in words:\n")
characters = characters.split()
"""