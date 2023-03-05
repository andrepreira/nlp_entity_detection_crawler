import requests
from bs4 import BeautifulSoup
import spacy

# Load the pre-trained NER model
nlp = spacy.load("en_core_web_sm")

# Parse the HTML content
url = "https://en.wikipedia.org/wiki/Natural_language_processing"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
text = soup.get_text()

# Preprocess the text
text = text.replace("\n", " ").strip()

# Use spaCy to detect named entities in the text
doc = nlp(text)
entities = [(ent.text, ent.label_) for ent in doc.ents]

# Print the detected entities
print(entities)
