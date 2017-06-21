# -*- coding: utf-8 -*-
import time
import logging
from twisted.internet import reactor
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

from tutorial.spiders.c_pull_spider import CSpider

if __name__ == '__main__':
#    logging.getLogger('scrapy').setLevel(logging.CRITICAL) # ???
    logging.getLogger('scrapy').propagate = False
    
    print("Hello. My Name is scraper.")
    
    configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
    runner = CrawlerRunner()
    
    d = runner.crawl(CSpider)
    d.addBoth(lambda _: reactor.stop())
    reactor.run() # script blocks here until crawling is finished
    
   
#    process = CrawlerProcess({'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'})

#    process.crawl(BlogSpider)
#    process.start() # script blocks here until crawling is finished
    
#    time.sleep(5)
    print("Bye. My Name was scraper.")
    
    
    
    
    
    
    
    
    
    
    
    
    
    