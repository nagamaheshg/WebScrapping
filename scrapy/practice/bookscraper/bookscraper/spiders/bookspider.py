import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        
        books = response.css('.product_pod')
        for book in books:
            yield{
                'name': book.css('h3 a::attr(title)').get(),
                'price': book.css('.price_color ::text').get(),
                'book_url': book.css('a ::attr(href)').get(),
                
            }

        next_page = response.css('.next a::attr(href)').get()
        
        if next_page is not None:
            
            if 'catalogue/' in next_page:
                next_page_url = 'https://books.toscrape.com/' + next_page
            
            else:
                next_page_url = 'https://books.toscrape.com/catalogue/' + next_page
            
            yield response.follow(next_page_url, callback=self.parse)
            
        
        