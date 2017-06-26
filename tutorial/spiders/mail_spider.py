import scrapy

class MailSpider(scrapy.Spider):
	name = "emails"
	start_urls = [
		'https://www.hs-niederrhein.de/elektrotechnik-informatik/personen/',
	]

	def parse(self, response):
		persons = response.css("div.tx-iwpersonen-pi1-item-box")

		for person in persons:
			mail = person.css("a.font-size-11::text").extract_first();
			name = person.css("a.tx-iwpersonen-pi1-detaillink::text").extract_first();
			mail = mail.replace("(at)", "@")
			yield{name : mail,}
