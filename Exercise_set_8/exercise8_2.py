import random
import colorama
from colorama import Back

colorama.init(autoreset=True)

random_number = (random.randint(1, 21))

while True:
    user_answer = int(input("Guess the number (1-20):\n"))
    if user_answer == random_number:
        print(Back.GREEN + "CONGRATULATIONS!!")
        break
    elif user_answer < random_number:
        print(Back.BLUE + "Too low.")
    elif user_answer > random_number:
        print(Back.RED + "Too high.")
    