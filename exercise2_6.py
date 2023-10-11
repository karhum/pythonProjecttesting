import math
# ex. 6. fruit game

# apple equals
apple = (math.sqrt(3 + 10 - 4)) / 3 + (5 ** 3 - 5) / 20 + 3

# 2 cherries equals
cherry = 2 + 2 * 2 + 2 - 2 - 2

# orange equals
orange = apple - 9

# 3 bananas equals
banana = cherry - 10

# pear equals
pear = banana - 8

# result
result = apple - (banana * 2)/3 + orange * 2 * (pear + cherry/2)
result = int(result)
print(f"{result}")