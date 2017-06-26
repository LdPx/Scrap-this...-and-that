# -*- coding: utf-8 -*-
import logging
from twisted.internet import reactor
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

from tutorial.spiders.c_pull_spider import CSpider

if __name__ == '__main__':
    logging.getLogger('scrapy').propagate = False
    
    configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
    runner = CrawlerRunner()
    
    d = runner.crawl(CSpider)   # Class name - with CMD: 'name' attribute
    d.addBoth(lambda _: reactor.stop())
    reactor.run()
    
    print("Finished.")
    
    
    
    
    
    
    
    
    
    
    
    
    
    