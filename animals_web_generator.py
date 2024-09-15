import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)
animals_data = load_data('animals_data.json')


def creating_data(animals_data):
    '''Providing informations about animals'''
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
            print(f"Type: {animal_type}\n")


def load_template():
    with  open('animals_template.html','r') as file:
        html_content = file.read()
    return html_content


def creating_string(html_content):
    output = ''  # define an empty string
    for animal_data in html_content:
    # append information to each string
        output += f"Name: {animal_data['name']}\n"
        output += f"Diet: {animal_data['characteristics']['diet']}\n"
        output += f"First Location {animal_data['locations'][0]}\n"
        output += f"Type {animal_data['characteristics'].get('type', 'N/A')}\n\n"

    print(output)


def main():
    animals = load_data('animals_data.json')
    creating_data(animals)
    html_template = load_template()
    creating_string(animals)


if __name__=="__main__":
    main()



