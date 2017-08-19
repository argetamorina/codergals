from scrapy import Spider
from scrapy.selector import Selector

from stack.items import StackItem

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

            for i in range(len(items['currency'])):
                item = StackItem()
                item['currency'] = items['currency'][i]
                item['last'] = items['last'][i].strip('\n').strip('\t').strip()
                item['dayhigh'] = items['dayhigh'][i].strip('\n').strip('\t')
                item['daylow'] = items['daylow'][i].strip('\n').strip('\t')
                yield item
        # import pdb
        # pdb.set_trace()
