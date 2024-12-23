import requests
import os
from dotenv import load_dotenv

# Load from .env file
load_dotenv()


# Fetch the API key from env
API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL", "https://api.api-ninjas.com/v1/animals")


def fetch_animal_data(animal_name):
    """
    Fetches animal data from the API based on the provided animal name.

    Args:
        animal_name (str): The name of the animal to search for.

    Returns:
        list: A list of dictionaries containing animal data if successful; otherwise, an empty list.
    """
    headers = {'X-Api-Key': API_KEY}
    params = {'name': animal_name}

    try:
        response = requests.get(API_URL, headers=headers, params=params, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Error: Failed to establish a connection to the API.")
    except requests.exceptions.Timeout:
        print("Error: The request timed out.")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")
    return []


def generate_html(animal_name, animals):
    # Start generating the HTML content
    html_content = """
    <html>
    <head>
        <title>Animal Information</title>
    </head>
    <body>
        <h1>Animals related to '{}'</h1>
        <ul>
    """.format(animal_name.capitalize())

    # Add animals details to the HTML
    for animal in animals:
        html_content += "<li><h2>{}</h2>".format(animal.get('name', 'Unknown Animal'))
        html_content += "<p><strong>Kingdom:</strong> {}</p>".format(animal['taxonomy'].get('kingdom', 'N/A'))
        html_content += "<p><strong>Phylum:</strong> {}</p>".format(animal['taxonomy'].get('phylum', 'N/A'))
        html_content += "<p><strong>Class:</strong> {}</p>".format(animal['taxonomy'].get('class', 'N/A'))
        html_content += "<p><strong>Order:</strong> {}</p>".format(animal['taxonomy'].get('order', 'N/A'))
        html_content += "<p><strong>Family:</strong> {}</p>".format(animal['taxonomy'].get('family', 'N/A'))
        html_content += "</li>"

    html_content += """
        </ul>
    </body>
    </html>
    """

    # Write in the HTML file
    with open('animals.html', 'w') as file:
        file.write(html_content)

    print("Website was successfully generated to the file animals.html.")
