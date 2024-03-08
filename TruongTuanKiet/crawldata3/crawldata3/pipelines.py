# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.exceptions import DropItem
from itemadapter import ItemAdapter
import pymongo
import json
from bson.objectid import ObjectId
class MongoDBPipeline:
    def __init__(self):
        
        self.client = pymongo.MongoClient('mongodb+srv://tuankietbmy:tuankiet123@cluster0.o0qoemc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
        self.db =self.client["datamonkey"]
        
    def process_item(self, item, spider):
        
        collecttion = self.db['datamonkey']
        
        try:
            collecttion.insert_one(dict(item))
            return item
        except Exception as e:
            raise DropItem(f"Error in pipeline: {e}")
class JsonDBPipeline:
    def process_item(self, item, spider):
        self.file = open('datamonkey_datamonkey.json','a',encoding='utf-8')
        line = json.dumps(dict(item),ensure_ascii=False)+"\n"
        self.file.write(line)
        self.line.close()
        return item