cafe = {
    "name": "Imaginary Cafe Ltd.",
    "website": "https://edu.frostbit.fi/sites/cafe/en",
    "categories": [
        "cafe",
        "tea",
        "lunch",
        "breakfast"
    ],
    "location": {
        "city": "Rovaniemi",
        "address": "Test address 22",
        "zip_code": "FI-96100"
    }
}

print(cafe["name"])
print(cafe["location"]["address"])
print(f"{cafe['location']['zip_code']} {cafe['location']['city']}")
print()
print(cafe["website"])
services = cafe['categories']
print(f"Services: {', '.join(services)}")
