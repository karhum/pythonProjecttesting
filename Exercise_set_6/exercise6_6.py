basket = ["apple", "banana", "cherry", "carrot",
          "potato", "tomato", "cabbage"]

user_word = input("Which word to ignore?\n")

if user_word not in basket:
    print("Word not found.")
else:
    for fruit in basket:
        if fruit == user_word:
            continue
        print(fruit)

