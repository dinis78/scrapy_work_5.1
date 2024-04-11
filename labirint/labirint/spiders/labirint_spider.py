import scrapy

class LabirintSpider(scrapy.Spider):
    name = 'labirint_spider'
    start_urls = ['https://www.labirint.ru/']

    def parse(self, response):
      
        books = response.css('.product-title-link')
        
        for book in books:
            genre = book.css('.genre a::text').get()
            
            # Проверяем, что жанр соответствует "ужасы"
            if genre == "ужасы":
                title = book.css('::text').get()
                
                yield {
                    'title': title,
                    'genre': genre
                }

