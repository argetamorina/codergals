from scrapy import Spider
from scrapy.selector import Selector

from tutorial.items import StackItem

class StackSpider(Spider):
    name = "stack"
    allowed_domains = ["reuters.com"]
    start_urls = [
        "https://www.reuters.com/finance/currencies/quote?srcAmt=1&srcCurr=USD&destAmt=&destCurr=USD",
    ]
    def parse(self, response):
        table = Selector(response).xpath('//*[@id="currPairs"]')

        for row in table[:1]:
            items = {}
            items['currency'] = row.xpath('tbody/tr/td/a/text()').extract()
            items['last'] = row.xpath('tbody/tr/td[2]/text()').extract()
            items['dayhigh'] = row.xpath('tbody/tr/td[3]/text()').extract()
            items['daylow'] = row.xpath('tbody/tr/td[4]/text()').extract()

            yield items
        # import pdb
        # pdb.set_trace()
