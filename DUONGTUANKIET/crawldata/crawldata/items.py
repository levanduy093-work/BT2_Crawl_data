# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


import scrapy


class ScrawldatalabItem(scrapy.Item):
   Link = scrapy.Field()
   Title = scrapy.Field()
   LawName = scrapy.Field()
   Answer = scrapy.Field()

