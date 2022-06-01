import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

class EmpsitSpider(scrapy.Spider):
    name = "EmpsitSpider"
    allowed_domains = ["bls.gov"]
    start_urls = [
    'https://www.bls.gov/bls/news-release/empsit.htm#2008'
    ]

    rules = [
        Rule(
            LinkExtractor(allow_domains=("bls.gov"), restrict_xpaths=('//div[@id="bodytext"]/a[following-sibling::text()[contains(., ".htm")]]')), # getting syntax error. Tried: restrict_xpaths=("//*[contains(., ".htm")]")), no success
            follow= True, callback= "parse_items"),
            ]

    def parse_items(self, response):
        self.logger.info("bls item page %s", response.url)
        item = scrapy.Item()
        item["SA"] = response.xpath(('//*[@id="ces_table1"]/tbody/tr[138]/td[8]/span')[0].text).extract()
        item["NSA"] = response.xpath(tree.xpath('//*[@id="ces_table1"]/tbody/tr[138]/td[4]/span')[0].text).extract()
        return item
