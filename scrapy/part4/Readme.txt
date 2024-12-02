#### Creating Scrapy project

1. install python
2. create a folder
3. create a virtual environment
4. install scrapy
5. verify scrapy

6. scrapy startproject <projectname>
7. navigate project
8. navigate project package
9. navigate spider package
10. execute "scrapy genspider <name_of_spider> <url_of_website>"
11. above command create a  spider file
12. pip install ipython

after install ipython configure things in scrapy.cfg 
under settings add shell = ipython

[settings]
default = bookscraper.settings
shell = ipython
13. execute "scrapy shell"

check the given domain able to fetching or not.
14. execute fetch('https://books.toscrape.com)

put everything into response variable

15. execute response

get all different books on the page.
16. execute response.css('article.product_pod')

To get all html of the first book 
17. execute response.css('article.product_pod').get()

To store all books in separate variable. all different books stored in separate variable
18. execute books = response.css('article.product_pod')

get the book from books

19 execute book = books[1]

get the title of the book

20. book.css('h3 a::text').get()

get the price of the book

21. book.css('div.product_price p::text').get()
       (or)
    book.css('.product_price .price_color::text').get()

get the url of the book

22. book.css('h3 a').attrib['href']

exit scrapy shell

23. exit
    cd ..

navigate to bookscraper folder 
scrapy crawl <name of the spider>

24. execute "scrapy crawl bookspider"

we just scrapy one page how to scrapy all the books in all pages

25. 
response.css('li.next a').attrib['href']
(or)
response.css('li.next a::attr(href)').get()

example:


import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books = response.css('article.product_pod')
        
        for book in books:
            yield{
                'name': book.css('h3 a::text').get(),
                'price': book.css('div.product_price p::text').get(),
                'url': book.css('h3 a').attrib['href'],
            }
