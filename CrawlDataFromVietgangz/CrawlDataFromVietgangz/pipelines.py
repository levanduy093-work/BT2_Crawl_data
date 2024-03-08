# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
import json
from scrapy.exceptions import DropItem

class MongoDBPipeline:
    def __init__(self):
        self.client = pymongo.MongoClient('mongodb+srv://sa:sapassword@cluster0.yx3puvk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
        self.db = self.client["vietgangz"]
    
    def process_item(self, item, spider):
        collection = self.db["vietgangz_db"]

        try:
            collection.insert_one(dict(item))
            return item
        except Exception as e:
            raise DropItem(f"Error in pipeline : {e}")
    
class JsonDBPipeline:
    def process_item(self, item, spider):
        self.file = open('vietgangz.vietgangz_db.json', 'a', encoding='utf-8')
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        self.file.close()
        return item


