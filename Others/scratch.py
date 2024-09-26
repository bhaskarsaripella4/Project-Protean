import requests
from bs4 import BeautifulSoup

def read_public_google_doc(url):
    # Ensure the URL is a Google Docs URL and accessible publicly
    response = requests.get(url)

    if response.status_code == 200:
        # Parse HTML content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract the text content from the document
        text = soup.get_text()
        return text
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None

# Example usage
url = 'https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub'
text = read_public_google_doc(url)
if text:
    print(text)