# -*- coding: utf-8 -*-

import scrapy
from scrapy.crawler import CrawlerProcess

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://blog.scrapinghub.com']

    def parse(self, response):
        for title in response.css('h2.entry-title'):
            yield {'title': title.css('a ::text').extract_first()}

        next_page = response.css('div.prev-post > a ::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

if __name__ == '__main__':
    print("Hello. My Name is scraper.")
    
    process = CrawlerProcess({'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'})

    process.crawl(BlogSpider)
    process.start() # script blocks here until crawling is finished
    
    print("Bye. My Name was scraper.")