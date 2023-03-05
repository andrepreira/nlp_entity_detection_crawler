from scrapy.crawler import CrawlerProcess
from fastapi import FastAPI

from entity_detector import EntityDetectorSpider

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/entitydetector")
async def detect_entities(url: str):
    # Create an empty list to hold the spider output
    output = []

    # Run the spider to extract the text and detect entities
    process = CrawlerProcess(settings={
        "LOG_LEVEL": "ERROR"
    })
    process.crawl(EntityDetectorSpider, url=url, output=output)
    process.start()

    # Extract the entities from the spider output
    entities = output[0]["entities"]

    # Return the detected entities
    return {"entities": entities}
