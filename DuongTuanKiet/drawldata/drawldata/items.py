# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DrawldataItem(scrapy.Item):
    Link = scrapy.Field()
    Answer = scrapy.Field()
    Title = scrapy.Field()
    Lawname = scrapy.Field()
 
