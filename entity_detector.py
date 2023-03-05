import spacy
import scrapy
from scrapy.selector import Selector


class EntityDetector:
    def __init__(self, model_name):
        self.nlp = spacy.load(model_name)

    def detect_entities(self, text):
        doc = self.nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        return entities

class EntityDetectorSpider(scrapy.Spider):
    name = "entity_detector"

    def __init__(self, url, output, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [url]
        self.detector = EntityDetector("en_core_web_sm")
        self.output = output

    def parse(self, response):
        sel = Selector(response)
        text = sel.xpath("//body//text()").getall()
        text = " ".join(text)
        text = text.replace("\n", " ").strip()
        entities = self.detector.detect_entities(text)
        self.output.append({"entities": entities})