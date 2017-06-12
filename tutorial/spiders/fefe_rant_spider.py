import scrapy
from pprint import pformat
from urllib.parse import urlparse
from collections import Counter, OrderedDict

# beachte: ab 'https://blog.fefe.de/?mon=200806' kein body
# beachte: zählz akt.Monat alles doppelt, wenn 'https://blog.fefe.de' Ausgangspunkt

class FefeRantSpider(scrapy.Spider):
    
    name = 'feferant'
    start_urls = ['https://blog.fefe.de/']
    
    def __init__(self):
        self.counter = Counter()

    def parse(self, response):
        links = response.css('ul li a::attr(href)').extract()
        #self.logger.info('raw links:\n{}'.format(pformat(links)))
        links = [urlparse(link).hostname for link in links if urlparse(link).hostname]
        #self.logger.info('links:\n{}'.format(pformat(links)))
        self.counter.update(links)
        #self.logger.info('counted links:\n{}'.format(pformat(occurences)))
        #yield occurences
        
        last_month_link = response.css('div:nth-last-child(2) a:nth-of-type(1)::attr(href)').extract_first()
        if last_month_link is None:
            yield OrderedDict(sorted(self.counter.items(), key = lambda item: item[1], reverse=True))
        else:
            self.logger.info('last month {}'.format(last_month_link))
            yield response.follow(last_month_link, callback=self.parse)
            
                