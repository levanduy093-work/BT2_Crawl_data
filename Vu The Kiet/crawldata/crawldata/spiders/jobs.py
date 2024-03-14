import scrapy
from crawldata.items import CrawldataItem
import os,json

class JobsSpider(scrapy.Spider):
    name = "jobs"
    allowed_domains = ["vieclamtphcm.vn"]
    # start_urls = ["https://vieclamtphcm.vn"]

    def start_requests(self):
        for page_number in range (1,4):
            yield scrapy.Request(url='https://vieclamtphcm.vn/tim-kiem/viec-lam-cntt-phan-mem?page={page_number}&cat=10&order=1'.format(page_number=page_number), callback=self.parse)

    def parse(self, response):
        questionURLs = response.xpath('//div[@class="job-content"]/descendant::p/a/@href').getall()
        for questionURL in questionURLs:
            item = CrawldataItem()
            item['Link'] = response.urljoin(questionURL)
            request = scrapy.Request(url= response.urljoin(questionURL), callback= self.parseQA)
            request.meta['item'] = item
            yield request


    def parseQA(self, response):
        item = response.meta['item']
        item['JobName_Company'] = response.xpath('normalize-space(string(//h1))').get()
        item['Pay'] = response.xpath('normalize-space(string(//div[@class="_content"]/descendant::strong[@class="text-success font-def"]))').get()
        item['Career'] = response.xpath('normalize-space(string(//div[@class="_content"]/descendant::a))').get()
        item['Deadline'] = response.xpath('normalize-space(string(//div[@class="_content"]/descendant::span))').get()   
        item['Quantity'] = response.xpath('normalize-space(string(//div[@class="bg-white p-24 mb-24"]/descendant::ul/li[4]/span))').get() 
        item['Job_description'] = response.xpath('normalize-space(string(//div[@class="bg-white p-24 mb-24"]/descendant::div[1]/div[2]))').get()
        item['Benefits'] = response.xpath('normalize-space(string(//div[@class="bg-white p-24 mb-24"]/descendant::div[4]/div[2]))').get()
        item['Request'] = response.xpath('normalize-space(string(//div[@class="bg-white p-24 mb-24"]/descendant::div[7]/div[2]))').get()
        yield item
