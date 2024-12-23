import json


def load_data(file_path):
    """
    Load data from a JSON file with error handling for file not found and invalid JSON.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        list: The data loaded from the JSON file, or an empty list if errors occur.
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
    """
    Main function to load animal data, create an HTML file, and write it to disk.

    Returns:
        None
    """
    animals = load_data('animals_data.json')  # Load data from the JSON file
    creating_data(animals)  # Print animal data to console
    html_template = load_template()  # Load the HTML template
    animals_info = creating_string(animals)  # Generate the HTML string with animal data
    updated_html = replace_placeholder(html_template, '__REPLACE_ANIMALS_INFO__',
                                       animals_info)  # Replace the placeholder in the template
    with open('animals.html', 'w') as file:  # Write the updated HTML to a file
        file.write(updated_html)
    print("HTML file 'animals.html' has been created successfully.")


if __name__ == "__main__":
    main()
