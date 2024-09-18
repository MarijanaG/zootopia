import json
import requests
from data_fetcher import fetch_animal_data, generate_html


def fetch_animal_data_and_generate_html(api_key, animal_name):
# API URL
    url = "https://api.api-ninjas.com/v1/animals"

# Your API key
    api_key = "uLnOf5PL3S9PZlsu36+n7Q==6iL55zWMjQ7qHpPH"

# Ask the user for an animal name
    animal_name = input("Enter a name of an animal: ")

# Parameters for the API
    params = {'name': animal_name}

# Headers with the API key
    headers = {
        'X-Api-Key': api_key
    }

# Send the GET request
    response = requests.get(url, headers=headers, params=params)

# Check the request
    if response.status_code == 200:
    # Fetch the results
        animals = response.json()

        if animals:  # Check if there are any results in the response
        # Start the HTML content
            html_content = """
            <html>
            <head>
                <title>Animal Information</title>
            </head>
            <body>
                <h1>Animals related to '{}'</h1>
                <ul>
            """.format(animal_name.capitalize())

        # Add each animal's details to the HTML content
            for animal in animals:
                html_content += "<li><h2>{}</h2>".format(animal.get('name', 'Unknown Animal'))
                html_content += "<p><strong>Kingdom:</strong> {}</p>".format(animal['taxonomy'].get('kingdom', 'N/A'))
                html_content += "<p><strong>Phylum:</strong> {}</p>".format(animal['taxonomy'].get('phylum', 'N/A'))
                html_content += "<p><strong>Class:</strong> {}</p>".format(animal['taxonomy'].get('class', 'N/A'))
                html_content += "<p><strong>Order:</strong> {}</p>".format(animal['taxonomy'].get('order', 'N/A'))
                html_content += "<p><strong>Family:</strong> {}</p>".format(animal['taxonomy'].get('family', 'N/A'))
                html_content += "</li>"

        # Close the HTML tags
            html_content += """
                </ul>
            </body>
            </html>
            """

        # Write the content to an HTML file
            with open('animals.html', 'w') as file:
                file.write(html_content)

            print("Website was successfully generated to the file animals.html.")
        else:
        # No animals found, print a message to the user
            print(f"No animals found for the name '{animal_name}'. Please try again.")
    else:
        print(f"Error: Unable to fetch animal data. Status code: {response.status_code}")


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
        output += '<li class="cards__item">\n'
        output += f'  <div class="card__title">{animal_data.get("name", "Unknown")}</div>\n'
        output += '  <p class="card__text">\n'

        characteristics = animal_data.get('characteristics', {})
        locations = animal_data.get('locations', [])

        output += f'      <strong>Location:</strong> {", ".join(locations) if locations else "N/A"}<br/>\n'
        output += f'      <strong>Type:</strong> {characteristics.get("type", "N/A")}<br/>\n'
        output += f'      <strong>Diet:</strong> {characteristics.get("diet", "N/A")}<br/>\n'

        output += '  </p>\n'
        output += '</li>\n'

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



