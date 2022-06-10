# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo


class ImdbPipeline:
    def __init__(self):
        self.conn = pymongo.MongoClient("localhost", 27017)

        db = self.conn["IMDB"]
        self.collection = db["IMDB"]

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
