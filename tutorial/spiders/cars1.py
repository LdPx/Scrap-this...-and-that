import scrapy
import logging
import pprint
from pprint import pformat

class Cars1(scrapy.Spider):
    
    name = 'CarsCrawler'
    start_urls = ['https://suchen.mobile.de/fahrzeuge/search.html?damageUnrepaired=NO_DAMAGE_UNREPAIRED&isSearchRequest=true&maxMileage=100&maxPowerAsArray=PS&minPowerAsArray=35&minPowerAsArray=PS&minPrice=5000&scopeId=C&usage=NEW&usageType=PRE_REGISTRATION']
    

    def parse(self, response):
        for offer in response.css('.cBox-body.cBox-body--resultitem.rbt-reg.rbt-no-top'):   # selecting all entries
            
            yield {
                'full': offer.css('.h3.u-text-break-word::text').extract_first(),   # Complete name of the offer
                'brand': offer.css('.h3.u-text-break-word::text').extract_first().split(' ', 1)[0], # First word of the offer
                'car-name': offer.css('.h3.u-text-break-word::text').extract_first().split(' ', 2)[1],  # Second word of the offer
                'car-name-all': offer.css('.h3.u-text-break-word::text').extract_first().split(' ', 1)[1],  # All but the first word of the offer
                'price': offer.css('.h3.u-block::text').extract_first().split(' ', 1)[0],    # excludes the '€' and '.'
            }
            