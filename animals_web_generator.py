import json

with open('animals_data.json', 'r') as file:
    animals_data = json.load(file)

for animal in animals_data:
    name = animal.get('name')
    characteristics = animal.get('characteristics', {})
    locations = animal.get('locations', [])
    diet = characteristics.get('diet')
    animal_type = characteristics.get('type')
    first_location = locations[0] if locations else None

    if name:
        print(f"Name: {name}")
    if diet:
        print(f"Diet: {diet}")
    if first_location:
        print(f"First location: {first_location}")
    if animal_type:
        print(f"Type: {animal_type}")

