import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        books = response.css("article.product_pod")
        for book in books:
            relative_url = book.css("h3 a::attr(href)").get()
            if 'catalogue' in relative_url:
                    book_url = 'https://books.toscrape.com/' + relative_url
            else:
                    book_url = 'https://books.toscrape.com/catalogue/' + relative_url
            yield response.follow(relative_url, callback= self.parse_book_page)

            next_page = response.css("li.next a::attr(href)").get()
            if next_page is not None:
                if 'catalogue' in next_page:
                    next_page = 'https://books.toscrape.com/' + next_page
                else:
                     next_page = 'https://books.toscrape.com/catalogue/' + next_page
                yield response.follow(next_page, callback=self.parse)
        
    def parse_book_page(self, response):
         
        table_rows = response.css("table tr")
        yield {
            'url': response.url,
            'title': response.css(".product_main h1::text").get(),
            'product_type': table_rows[1].css("td::text").get(),
            'price_excl_tax': table_rows[2].css("td::text").get(), 
            'price_incl_tax': table_rows[3].css("td::text").get(),
            'tax': table_rows[4].css("td::text").get(),
            'availability': table_rows[5].css("td::text").get(),
            'number_of_reviews': table_rows[6].css("td::text").get(),
            'star_rating': response.css("p.star-rating").attrib['class'],
            'price': response.css(".price_color::text").get(),
        }
