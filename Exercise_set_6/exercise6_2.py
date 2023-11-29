# multiplication tables
number = 1

while True:
    number = int(input(
        "Which multiplication table would you like to see? (1-10). 0 stops program.\n"
    ))
    if number == 0:
        break
    if number >= 11 or number <= -1:
        print("Wrong number format.")
        continue
    for i in range(10):
        m_table = number * (i + 1)

        print(f"{number} * {i + 1} = {m_table}")
