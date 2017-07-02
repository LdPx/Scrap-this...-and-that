# -*- coding: utf-8 -*-
import logging
from twisted.internet import reactor
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

from tutorial.spiders.c_pull_spider import CSpider
from tutorial.spiders.cars1 import Cars1
from tutorial.spiders.cars2 import Cars2
from tutorial.spiders.cars3 import Cars3

if __name__ == '__main__':
    logging.getLogger('scrapy').propagate = False
    
    configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
    runner = CrawlerRunner()
    
    d = runner.crawl(Cars3)   # Class name - with CMD: 'name' attribute
    d.addBoth(lambda _: reactor.stop())
    reactor.run()
    
    print("Finished.")
    
    