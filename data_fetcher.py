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
    """Generates an HTML file containing information about animals.
       animal_name (str): The name of the animal searched.
       animals (list): A list of dictionaries with animal data retrieved from the API."""

    html_content = """
        <html>
        <head>
            <title>Animal Information</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    margin: 0;
                    padding: 20px;
                }}
                h1 {{
                    color: #333;
                    text-align: center;
                }}
                ul {{
                    list-style-type: none;
                    padding: 0;
                }}
                li {{
                    background-color: #fff;
                    padding: 15px;
                    margin: 10px 0;
                    border-radius: 5px;
                    box-shadow: 0 0 5px rgba(0,0,0,0.1);
                }}
                h2 {{
                    color: #555;
                }}
                p {{
                    color: #666;
                    font-size: 14px;
                }}
            </style>
        </head>
        <body>
            <h1>Animals related to '{0}'</h1>
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

    # Write the HTML content to a file
    with open('animals.html', 'w') as file:
        file.write(html_content)

    print("Website was successfully generated to the file animals.html.")
