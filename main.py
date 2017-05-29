# -*- coding: utf-8 -*-

import logging
from twisted.internet import reactor
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

from tutorial.spiders.quotes_spider import QuotesSpider

if __name__ == '__main__':
#    logging.getLogger('scrapy').setLevel(logging.CRITICAL) # ???
    logging.getLogger('scrapy').propagate = False
    
    print("Hello. My Name is scraper.")
    
    
    configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
    runner = CrawlerRunner()
    
    d = runner.crawl(QuotesSpider)
    d.addBoth(lambda _: reactor.stop())
    reactor.run() # script blocks here until crawling is finished
    
   
#    process = CrawlerProcess({'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'})

#    process.crawl(BlogSpider)
#    process.start() # script blocks here until crawling is finished
    
    print("Bye. My Name was scraper.")
    
    
    
    
    
    
    
    
    
    
    
    
    
    