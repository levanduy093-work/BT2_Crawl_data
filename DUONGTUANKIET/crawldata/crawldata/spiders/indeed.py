import scrapy


class IndeedSpider(scrapy.Spider):
    name = "indeed"
    allowed_domains = ["vn.indeed.com"]
    start_urls = ["https://vn.indeed.com"]

   #Ham
    def start_requests(self):
        for page_number in range(1, 2):
            yield scrapy.Request(url="https://vn.indeed.com/?vjk=ffd6cfdbe9b2817a{page_number}".format(page_number=page_number, callback=self.parse))

    def parse(self, response):
        quesionURLs = response.xpath('//div[@class="fastviewjob jobsearch-ViewJobLayout--embedded css-1lo7kga eu4oa1w0"]/descendant::ul/li[1]/a/@href').getall()
        for quesionURL in quesionURLs:
            item = ScrawldatalabItem()
            item['Link'] = response.urljoin(quesionURL)
            request = scrapy.Request(url=response.urljoin(quesionURL), callback = self.parseQA)
            request.meta['item'] = item
            yield request
        pass

   

    def parseQA(self, response):
        item = response.meta['item']
        item['LawName'] = "doanhnghiep"
        item['Title'] =  response.xpath('normalize-space(string(//h1))').get()
        item['Answer'] =  response.xpath('normalize-space(string(//div[@id="tra-loi"]))').get()

        yield item

        pass