from datetime import (datetime)
from colorama import Fore


birth_years = []

# let's ask user the birth years with a loop for 5 times
for i in range(5):
    birth_year = int(input(f"Give the birth year of the person {i + 1}:\n"))
    birth_years.append(birth_year)
print()

# let's calculate the ages and print them with correct colors
print("Let's process all birth years...")
for year in birth_years:
    age = datetime.now().year - year
    if 0 <= age <= 125:
        print(f"{Fore.GREEN}{age} years old, age OK!" + Fore.RESET)
    else:
        print(f"{Fore.RED}{age} years old, incorrect age." + Fore.RESET)



print("All done!")
