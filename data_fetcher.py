import requests
import os
from dotenv import load_dotenv

# Load from .env file
load_dotenv()

# Fetch the API key from environment variables
API_KEY = os.getenv("API_KEY")


def fetch_animal_data(api_key, animal_name):
    # API URL
    url = "https://api.api-ninjas.com/v1/animals"

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
        # Fetch and return the results in JSON format
        return response.json()
    else:
        # Print an error message and return an empty list
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")
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
