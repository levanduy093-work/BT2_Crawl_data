import scrapy
from crawldata6.items import Crawldata6Item

class UnicaSpider(scrapy.Spider):
    name = "unica"
    allowed_domains = ["unica.vn"]
  #  start_urls = ["https://unica.vn"]

    def start_requests(self):
        for page_number in range(1,5):
            yield scrapy.Request(url='https://unica.vn/tag/cong-nghe-thong-tin?page={page_number}'.format(page_number=page_number),callback=self.parse)
            
    def parse(self, response):
        questionURLs = response.xpath('/html/body/div[4]/div/div[7]/div[2]/a/@href').getall() 
        for questionURL in questionURLs:
            item = Crawldata6Item()
            item['Link'] = response.urljoin(questionURL)
            request = scrapy.Request(url= response.urljoin(questionURL),callback=self.parseQA)
            request.meta['item'] = item
            yield request
            
    def parseQA(self, response):
        item = response.meta['item']
        item['Name'] = "unica"
        item['Title'] = response.xpath('normalize-space(string(//html/body/div[4]/div[2]/div/div/div/div/h1))').get() 
        item['GV'] = response.xpath('normalize-space(string(//html/body/div[4]/div[2]/div/div/div/div/div[3]/a))').get() 
        item['Gioithieu'] = response.xpath('normalize-space(string(//html/body/div[4]/div[3]/div[1]/div[2]/div[3]))').get() 
        
        yield item