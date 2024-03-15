# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Crawldata6Item(scrapy.Item):
    Link = scrapy.Field()
    Name = scrapy.Field()
    Title = scrapy.Field()
    GV = scrapy.Field()
    Gioithieu = scrapy.Field()
