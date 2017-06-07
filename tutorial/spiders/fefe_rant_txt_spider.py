import scrapy
from pprint import pformat
from urllib.parse import urlparse
from collections import Counter, OrderedDict
from scrapy.selector import HtmlXPathSelector

# beachte: ab 'https://blog.fefe.de/?mon=200806' kein body
# beachte: z�hlz akt.Monat alles doppelt, wenn 'https://blog.fefe.de' Ausgangspunkt

class FefeRantSpider(scrapy.Spider):
    
    name = 'feferanttxt'
    start_urls = ['https://blog.fefe.de/?mon=201706']
    
    def __init__(self):
        self.counter = Counter()



    def parse(self, response):
        for txt in response.css('li'):
            yield {
                #'text': txt.extract_first(),
            }


        hxs = HtmlXPathSelector(response)
        hxs.select('//div[@style="text-align:center"]/text()').extract()
        print(response.css('div[style="text-align:center"]').extract_first())
        
        
        next_page = response.css('div > a').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)


