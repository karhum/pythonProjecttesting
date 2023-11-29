# lst about fruits, berries and vegetables

fruits = ["apple", "pear", "banana"]
berries = ["strawberry", "blueberry", "blackberry"]
vegetables = ["carrot", "kale", "cucumber"]

inventory = [fruits, berries, vegetables]

for food_types in inventory:
    for food in food_types:
        print(food)

