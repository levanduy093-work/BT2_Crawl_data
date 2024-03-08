import scrapy
from scrapy.spiders import Spider
from scrapy.exporters import CsvItemExporter

class TopCVSpider(scrapy.Spider):
    name = 'topcv'
    start_urls = ['https://www.topcv.vn/viec-lam']

    def parse(self, response):
        # Bóc tách thông tin công việc từ trang web
        for job in response.css('.job-item'):
            title = job.css('.job-title::text').get()
            company = job.css('.company-name::text').get()
            location = job.css('.job-location::text').get()

            item = {'title': title, 'company': company, 'location': location}
            self.jobs_exporter.export_item(item)

       