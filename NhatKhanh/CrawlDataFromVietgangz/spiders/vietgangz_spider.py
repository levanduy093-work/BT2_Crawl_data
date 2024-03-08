import scrapy
import pymongo
from bs4 import BeautifulSoup
from CrawlDataFromVietgangz.items import CrawldatafromvietgangzItem    

class VietgangzSpiderSpider(scrapy.Spider):
    name = "vietgangz_spider"
    allowed_domains = ["vietgangz.com"]
    # start_urls = ["https://vietgangz.com"]

    def start_requests(self):
         for page_number in range(1, 4):
              yield scrapy.Request(url = 'https://vietgangz.com/product-category/tops/page/{page_number}'.format(page_number = page_number), callback = self.parse)
    
    def parse(self, response):
        productsURL = response.xpath('/html/body/div[2]/main/div/div[2]/div/div[2]//descendant::a/@href').getall()
        for productURL in productsURL:
            item = CrawldatafromvietgangzItem()
            item['Link'] = response.urljoin(productURL)
            request = scrapy.Request(url = response.urljoin(productURL), callback=self.parsePrd)
            request.meta['item'] = item
            yield request
    
    def parsePrd(self, response):
        item = response.meta['item']
        item['Name'] = response.xpath('normalize-space(string(//h1))').get() 
        item['Price'] = response.xpath('//div[@class="price-wrapper"]/p/span/bdi//text()').get() 
        item['Size'] = response.xpath('//select/option//text()').getall()[1:] 
        item['Description'] = response.xpath('//div[@class="product-short-description"]/ul/li//text()').getall() 
        
        yield item
