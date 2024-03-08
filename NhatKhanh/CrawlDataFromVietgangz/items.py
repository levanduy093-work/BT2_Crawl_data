# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawldatafromvietgangzItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Link = scrapy.Field()
    Name = scrapy.Field()
    Price = scrapy.Field()
    Size = scrapy.Field()
    Description = scrapy.Field()
