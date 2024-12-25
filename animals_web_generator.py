import json
import os
import requests
from data_fetcher import fetch_animal_data, generate_html


def load_data(file_path):
    """
    Load data from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        list: The data loaded from the JSON file.
    """
    try:
        with open(file_path, "r") as handle:
            return json.load(handle)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from {file_path}.")
        return []


def creating_data(animals_data):
    """
    Print information about animals from the data.

    Args:
        animals_data (list): A list of dictionaries containing animal data.

    Returns:
        None
    """
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
    """
    Load the HTML template from a file.

    Returns:
        str: The content of the HTML template.
    """
    with open('animals_template.html', 'r') as file:
        html_content = file.read()
    return html_content


def creating_string(animals_data):
    """
    Create an HTML string with animal data.

    Args:
        animals_data (list): A list of dictionaries containing animal data.

    Returns:
        str: The generated HTML string.
    """
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

    output += '</ul>\n'
    return output


def replace_placeholder(html_content, placeholder, replacement):
    """
    Replace a placeholder in the HTML content with a given replacement string.

    Args:
        html_content (str): The original HTML content.
        placeholder (str): The placeholder to replace.
        replacement (str): The string to replace the placeholder with.

    Returns:
        str: The updated HTML content.
    """
    return html_content.replace(placeholder, replacement)


def main():
    """Main function to prompt user input, fetch animal data, and generate an HTML file.

The function:
1. Prompts the user to enter an animal name.
2. Fetches data about the animal from the API.
3. If data is found, generates an HTML file with the results.
4. If no data is found, generates an HTML file with an error message."""

    animal_name = input("Enter the name of an animal: ").strip()

    if not animal_name:
        print("Animal name cannot be blank.")
        return

    animals = fetch_animal_data(animal_name)

    if animals:
        generate_html(animal_name, animals)
        print("Website was successfully generated to the file animals.html.")
    else:
        generate_html(
            animal_name,
            [{"name": f"The animal '{animal_name}' doesn't exist."}]
        )
        print("Website was successfully generated with an error message to the file animals.html.")


if __name__ == "__main__":
    main()
