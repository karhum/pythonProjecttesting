# list of movies

movies = [
    {"name": "Casablanca", "year": 1942},
    {"name": "Avatar", "year": 2009},
    {"name": "Forrest Gump", "year": 1994},
    {"name": "Pulp Fiction", "year": 1994},
    {"name": "Puss in Boots, Last wish", "year": 2022},
    {"name": "Palmeras En La Nieve", "year": 2015}
]

is_new = []
is_old = []

print("These movies have been released in year 2000 or later:")
for movie in movies:
    if movie["year"] >= 2000:
        is_new.append(movie["name"])

is_new = ', '.join(is_new)

print(is_new)
print()
print("These movies have been released before the year 2000:")
for movie in movies:
    if movie["year"] < 2000:
        is_old.append(movie["name"])

is_old = ', '.join(is_old)

print(is_old)
