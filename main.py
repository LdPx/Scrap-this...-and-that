# -*- coding: utf-8 -*-

import logging
from twisted.internet import reactor
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

from scrapy.utils.project import get_project_settings
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals


class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://blog.scrapinghub.com']

    def parse(self, response):
        for title in response.css('h2.entry-title'):
            yield {'title': title.css('a ::text').extract_first()}

        next_page = response.css('div.prev-post > a ::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)


def spider_results():
    results = []   

    def crawler_results(parse_result):
        results.append(parse_result)

    dispatcher.connect(crawler_results)

    runner = CrawlerRunner(get_project_settings())
    running_crawler = runner.crawl(BlogSpider)
    running_crawler.addBoth(lambda _: reactor.stop())
    reactor.run()


if __name__ == '__main__':
#    logging.getLogger('scrapy').setLevel(logging.CRITICAL) # ???
    logging.getLogger('scrapy').propagate = False
    
    print("Hello. My Name is scraper.")
    
    '''    
    configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
    runner = CrawlerRunner()
    
    d = runner.crawl(BlogSpider)
    d.addBoth(lambda _: reactor.stop())
    reactor.run() # script blocks here until crawling is finished
    '''    
   
    spider_results()
    
#    process = CrawlerProcess({'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'})

#    process.crawl(BlogSpider)
#    process.start() # script blocks here until crawling is finished
    
    print("Bye. My Name was scraper.")
    
    
    
    
    
    
    
    
    
    
    
    
    
    