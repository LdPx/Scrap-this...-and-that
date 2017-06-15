import scrapy
import logging
from pprint import pformat
from urllib.parse import urlparse
from collections import Counter, OrderedDict

class CSpider(scrapy.Spider):
    
    name = 'cccp'
    start_urls = ['https://suchen.mobile.de/fahrzeuge/search.html?damageUnrepaired=NO_DAMAGE_UNREPAIRED&isSearchRequest=true&maxMileage=100&maxPowerAsArray=PS&minPowerAsArray=35&minPowerAsArray=PS&minPrice=5000&scopeId=C&usage=NEW&usageType=PRE_REGISTRATION']
    
    def __init__(self):
        self.counter = Counter()

    def parsed_detailes(self, response):
        logging.getLogger('scrapy').critical("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("jojojo")

    def parse(self, response):
        for quote in response.css('.cBox-body.cBox-body--resultitem.rbt-reg.rbt-no-top'):   # selecting all entries
            print(quote.css('.h3.u-block::text').extract_first().split(' ', 1)[0])  # selecting only the elements inside the previous selection    # extract_first() or else a list with one item would be returned

            # TODO extract information for the current item from a sub-page
            details_link = quote.css('a::attr(href)').extract_first()
            scrapy.Request(url=details_link, callback=self.parsed_detailes)
            
            #.css('#rbt-damageCondition-v').extract_first()

            yield {
#                'full': quote.css('.h3.u-text-break-word::text').extract_first(),
#                'brand': quote.css('.h3.u-text-break-word::text').extract_first().split(' ', 1)[0],
#                'name': quote.css('.h3.u-text-break-word::text').extract_first().split(' ', 2)[1],
#                'name-all': quote.css('.h3.u-text-break-word::text').extract_first().split(' ', 1)[1],
#                'price': quote.css('.h3.u-block::text').extract_first().split(' ', 1)[0],    # excludes the € sign

                'text': quote.css('.h3.u-text-break-word').extract_first(),
            }
            
            # TODO next page
#            next_page = response.css('li.next a::attr(href)').extract_first()
#            if next_page is not None:
#                next_page = response.urljoin(next_page)
#                yield scrapy.Request(next_page, callback=self.parse)
            
            
            
            
            
            