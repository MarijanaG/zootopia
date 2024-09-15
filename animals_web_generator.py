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


def creating_string(animals_data):
    output = ''  # define an empty string
    output = '<ul class="cards">\n'
    for animal_data in animals_data:
        output += '<li class="cards__item">'
        output += '    <li>\n'  # List item start
        output += f"        <strong>Name:</strong> {animal_data.get('name', 'Unknown')}<br>\n"
        characteristics = animal_data.get('characteristics', {})
        output += f"        <strong>Diet:</strong> {characteristics.get('diet', 'N/A')}<br>\n"
        output += f"        <strong>Location:</strong> {animal_data['locations'][0] if animal_data.get('locations') else 'N/A'}<br>\n"
        output += f"        <strong>Type:</strong> {characteristics.get('type', 'N/A')}<br>\n"
        output += '    </li>\n'
        output += '</li>'
    output += '</ul>\n'

    return output


def replace_placeholder(html_content, placeholder, replacement):
    """ Replace a placeholder with the given replacement """
    return html_content.replace(placeholder, replacement)



def main():
    animals = load_data('animals_data.json')
    creating_data(animals)
    html_template = load_template()
    animals_info = creating_string(animals)
    updated_html = replace_placeholder(html_template, '__REPLACE_ANIMALS_INFO__', animals_info)
    with open('animals.html', 'w') as file:
        file.write(updated_html)
    print("HTML file 'animals.html' has been created successfully.")


if __name__=="__main__":
    main()



