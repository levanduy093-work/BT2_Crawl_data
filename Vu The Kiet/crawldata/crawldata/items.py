# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawldataItem(scrapy.Item):
    Link = scrapy.Field()
    JobName_Company = scrapy.Field()
    Deadline = scrapy.Field()
    Pay = scrapy.Field()
    Career = scrapy.Field()
    Quantity = scrapy.Field()
    Job_description = scrapy.Field()
    Benefits = scrapy.Field()
    Request = scrapy.Field()
