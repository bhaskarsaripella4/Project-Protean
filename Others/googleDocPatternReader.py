import requests
from bs4 import BeautifulSoup
import re


def fetch_public_google_doc(url):
    """Fetch the content of a public Google Doc."""
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to retrieve data. Status code: {response.status_code}")


def parse_grid_data(doc_text):
    """Parse the Google Doc content to extract Unicode characters and their grid positions."""
    soup = BeautifulSoup(doc_text, 'html.parser')
    raw_text = soup.get_text()

    # Regex to find Unicode characters and their positions (format: "char (x, y)")
    pattern = re.compile(r'(\d+)█?(\S)█?(\d+)|(\d+)░(\d+█?)')

    grid = {}
    for match in pattern.findall(raw_text):
        x1, char1, y1, x2, y2 = match
        x, y = int(x1), int(y1)
        if y not in grid:
            grid[y] = {}
        grid[y][x] = char1

    return grid


def print_grid(grid):
    """Print the grid of characters."""
    if not grid:
        print("No data to display.")
        return

    # Determine the maximum dimensions of the grid
    max_y = max(grid.keys())
    max_x = max(max(row.keys(), default=0) for row in grid.values())

    # Print the grid
    for y in range(max_y + 1):
        row = ''.join(grid.get(y, x) for x in range(max_x + 1))
        print(row)


# Example usage
url = 'https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub'
doc_text = fetch_public_google_doc(url)

if doc_text:
    grid = parse_grid_data(doc_text)
    print_grid(grid)
