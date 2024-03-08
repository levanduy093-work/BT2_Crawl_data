import scrapy
from crawldata3.items import Crawldata3Item
import os,json
class DatamonkeySpider(scrapy.Spider):
    name = "datamonkey"
    allowed_domains = ["datamonkey.pro"]
   # start_urls = ["https://datamonkey.pro"]    
   
    def start_requests(self):
        yield scrapy.Request(url='https://datamonkey.pro/guess_sql/lessons/')
        
        
    def parse(self, response):
        questionURLs = response.xpath('//div[@class="strip_single_course"]/descendant::h4/a/@href').getall()
        for questionURL  in questionURLs:
            item = Crawldata3Item()
            item['Link'] = response.urljoin(questionURL)
            # request = scrapy.Request(url=response.urljoin(questionURL),callback=self.parseQA)
            # request.meta['item'] = item
            # yield request
            yield item
    
    # def parseQA(self, response):
    #     item = response.meta['item']
    #     item ['Name'] = "Bai Hoc"
    #     item ['Answer'] = response.xpath('normalize-space(string(//html/body/div[2]/div[1]/div[1]/article/div[1]))').getall()
        
    #     yield item