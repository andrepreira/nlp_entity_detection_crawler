# Doc API

My Awesome API is a Python web application built with the [FastAPI](https://fastapi.tiangolo.com/) framework. It provides an endpoint for detecting entities in a given URL using the [spaCy](https://spacy.io/) natural language processing library.

## Installation

To run the API locally, you'll need Python 3.10 and pip installed on your machine. You can install the project dependencies using pip:

````lua
pip install -r requirements.txt
````



## Usage

To start the API, run the following command:

````lua
uvicorn main:app --reload
````

This will start the API on port 8000 by default. You can then access the API at [http://localhost:8000/entitydetector?url=<url>](http://localhost:8000/entitydetector?url=<url>), where `<url>` is the URL to detect entities in.

For example, to detect entities in the Wikipedia page for Python, you would use the following URL:

[http://localhost:8000/entitydetector?url=https://en.wikipedia.org/wiki/Python_(programming_language)](http://localhost:8000/entitydetector?url=https://en.wikipedia.org/wiki/Python_(programming_language))

This will return a JSON response containing the detected entities:

````json
{
"entities": [
{
"text": "Python",
"label": "LANGUAGE"
},
{
"text": "Guido van Rossum",
"label": "PERSON"
},
{
"text": "C",
"label": "LANGUAGE"
},
...
]
}
````


## Docker

You can also run the API using Docker. To build the Docker image, run the following command:

````lua

docker build -t doc-api .

````


This will build the Docker image with the tag `my-awesome-api`.

To start a Docker container from the image, run the following command:

````lua
docker run -p 8000:8000 doc-api
````

This will start a Docker container running the API on port 8000.

## Testing

To run the unit tests, use the following command:

````lua
python -m unittest discover
````


## Contributing

If you find a bug or have an idea for a new feature, feel free to open an issue or submit a pull request on GitHub.

## License

My Awesome API is released under the [MIT License](https://opensource.org/licenses/MIT).




# NLP entity detection with crawler

This is a simple crawler that uses the [Spacy](https://spacy.io/) to detect entities in a given URL.

Entity detection in parsed HTML can be done using Natural Language Processing (NLP) techniques such as Named Entity Recognition (NER) and Part-of-Speech (POS) tagging.

NER involves identifying and classifying named entities in text, such as names of people, organizations, locations, and dates. POS tagging, on the other hand, involves assigning part-of-speech tags to words in text, such as nouns, verbs, adjectives, etc.

To use NLP for entity detection in parsed HTML, you can follow these steps:

1. Parse the HTML using an HTML parser such as BeautifulSoup to extract the text content.

2. Preprocess the text content by removing HTML tags, special characters, and other noise that might interfere with the entity detection process.

3. Use a pre-trained NER model such as spaCy or NLTK to detect named entities in the preprocessed text. These models typically classify named entities into categories such as PERSON, ORGANIZATION, LOCATION, etc.

4. Use a POS tagging tool such as NLTK or Stanford CoreNLP to assign part-of-speech tags to the words in the preprocessed text.

5. Use the results of the NER and POS tagging to extract and classify entities in the parsed HTML, such as people's names, company names, locations, etc.

Overall, NLP can be a powerful tool for entity detection in parsed HTML, but it requires careful preprocessing and selection of appropriate models and tools for the task.