import scrapy
from drawldata.items import DrawldataItem
import os, json


class DangSpider(scrapy.Spider):
    name = "dang"
    allowed_domains = ["dangcongsan.vn"]
    start_urls = ["https://dangcongsan.vn"]

    def start_requests(self):
        for page_number in range(1, 2):
            yield scrapy.Request(url='https://dangcongsan.vn/lanh-dao-dang-nha-nuoc/p/page_number'.format(page_number=page_number), callback=self.parse)

    def parse(self, response):
        questionURLs = response.xpath('//div[@class="col-md-4 col-sm-12 col0 box-thumbnail"]/descendant::a/@href').getall()
        for questionURL in questionURLs:
            item = DrawldataItem()
            item['Link'] = response.urljoin(questionURL)
            request = scrapy.Request(url=response.urljoin(questionURL),callback=self.parseQA)
            request.meta['item'] = item
            yield request
       
        pass

    #  C1           
    def parseQA(self, response):
        item = response.meta['item']
        item['Lawname'] = "dang"
        item['Title'] = response.xpath('normalize-space(string(//h1[@class="post-title"]))').get()
        item['Answer'] = response.xpath('normalize-space(string(//div[@class="post-content"]))').get()
        yield item


        current_dir = os.getcwd()
        file_path = os.path.json(current_dir, 'data.json')
        with open(file_path , 'a') as f:
            line = json.dumps({
                'Link' : item['Link'],
                'LawName': item['LawName'],
                'Answer': item['Answer'],
                'Title': item['Item']}, ensure_ascii=False) + '\n'
            f.write(line)

