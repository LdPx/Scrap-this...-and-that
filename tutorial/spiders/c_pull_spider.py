import scrapy
import logging
import pprint
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
        pprint.pprint(response.meta)

    def parse(self, response):
        for offer in response.css('.cBox-body.cBox-body--resultitem.rbt-reg.rbt-no-top'):   # selecting all entries
            #print(offer.css('.h3.u-block::text').extract_first().split(' ', 1)[0])  # selecting only the elements inside the previous selection    # extract_first() or else a list with one item would be returned

            # TODO extract information for the current item from a sub-page
            details_link = offer.css('a::attr(href)').extract_first()
            details_link = offer.css('a::attr(href)').extract_first()
            scrapy.Request(url=details_link, callback=self.parsed_detailes)
            print(details_link)
            
            #.css('#rbt-damageCondition-v').extract_first()

            yield {
#                'full': offer.css('.h3.u-text-break-word::text').extract_first(),
#                'brand': offer.css('.h3.u-text-break-word::text').extract_first().split(' ', 1)[0],
#                'name': offer.css('.h3.u-text-break-word::text').extract_first().split(' ', 2)[1],
#                'name-all': offer.css('.h3.u-text-break-word::text').extract_first().split(' ', 1)[1],
#                'price': offer.css('.h3.u-block::text').extract_first().split(' ', 1)[0],    # excludes the € sign - includes '.'

                'text': offer.css('.h3.u-text-break-word').extract_first(),
            }
            
            # TODO next page
            details_link = response.urljoin(details_link)
            request = scrapy.Request(details_link, callback=self.parsed_detailes)
            request.meta['name-all'] = offer.css('.h3.u-text-break-word::text').extract_first().split(' ', 1)[1]
            request.meta['price'] = offer.css('.h3.u-block::text').extract_first().split(' ', 1)[0]
            if details_link is not None:
                yield request
            
            
            
            
            
            