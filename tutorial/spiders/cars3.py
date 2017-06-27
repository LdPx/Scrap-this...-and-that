import scrapy
import logging
import pprint
from pprint import pformat

class Cars3(scrapy.Spider):
    
    name = 'CarsCrawler'
    start_urls = ['https://suchen.mobile.de/fahrzeuge/search.html?damageUnrepaired=NO_DAMAGE_UNREPAIRED&isSearchRequest=true&maxMileage=100&maxPowerAsArray=PS&minPowerAsArray=35&minPowerAsArray=PS&minPrice=5000&scopeId=C&usage=NEW&usageType=PRE_REGISTRATION']

    def parse_details(self, response):
        AC = response.css('#rbt-climatisation-v::text').extract_first()
        if AC is None or AC.startswith('Keine'):
            response.meta['AC'] = 'Keine'
        else:
            response.meta['AC'] = AC
        
        #pprint.pprint(response.meta)
        yield {
            'AC':       response.meta['AC'],
            'full':     response.meta['full'],
            'brand':    response.meta['brand'],
            'name':     response.meta['name'],
            'name-all': response.meta['name-all'],
            'price':    response.meta['price'],
        }
        

    def parse(self, response):
        for offer in response.css('.cBox-body.cBox-body--resultitem.rbt-reg.rbt-no-top'):   # selecting all entries
            
            details_link = offer.css('a::attr(href)').extract_first()
            request = scrapy.Request(details_link, callback=self.parse_details)
            
            request.meta['full'] = offer.css('.h3.u-text-break-word::text').extract_first()
            request.meta['brand'] = offer.css('.h3.u-text-break-word::text').extract_first().split(' ', 1)[0]
            request.meta['name'] = offer.css('.h3.u-text-break-word::text').extract_first().split(' ', 2)[1]
            request.meta['name-all'] = offer.css('.h3.u-text-break-word::text').extract_first().split(' ', 1)[1]
            request.meta['price'] = offer.css('.h3.u-block::text').extract_first().split(' ', 1)[0].replace('.', '')
            
            if details_link is not None:
                yield request
            