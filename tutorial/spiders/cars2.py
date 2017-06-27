import scrapy
import logging
import pprint
from pprint import pformat

class Cars2(scrapy.Spider):
    
    name = 'CarsCrawler'
    start_urls = ['https://suchen.mobile.de/fahrzeuge/search.html?damageUnrepaired=NO_DAMAGE_UNREPAIRED&isSearchRequest=true&maxMileage=100&maxPowerAsArray=PS&minPowerAsArray=35&minPowerAsArray=PS&minPrice=5000&scopeId=C&usage=NEW&usageType=PRE_REGISTRATION']

    def parse_details(self, response):
        print(response.css('#rbt-climatisation-v::text').extract_first())
        yield {
            'AC': response.css('#rbt-climatisation-v::text').extract_first()
        }
        

    def parse(self, response):
        for offer in response.css('.cBox-body.cBox-body--resultitem.rbt-reg.rbt-no-top'):   # selecting all entries
            
            details_link = offer.css('a::attr(href)').extract_first()
            request = scrapy.Request(details_link, callback=self.parse_details)
            
            if details_link is not None:
                yield request
            