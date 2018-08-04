import scrapy
from ..items import ProductItem


class BreuningerSpider(scrapy.Spider):
    name = 'breuninger'
    allowed_urls = ['breuninger.com']
    start_urls = ['https://www.breuninger.com/damen/schuhe']

    def parse(self, response):
        urls_post = response.xpath(
            '//div[contains(@class,"shop-grid-column")]'
            '/suchen-produkt-stage/suchen-produkt/a/@href'
        ).extract()
        for url in urls_post[:1]:
            yield scrapy.Request('https://www.breuninger.com'+url, callback=self.parse_post)

    def parse_post(self, response):
        item = ProductItem()
        item['name'] = self.parse_name(response)
        yield item

    def parse_name(self, response):
        # name = response.xpath('//main[@class="shop-main bewerten-main"]/div[@class="shop-content"]'
        #                       '/div[@class="bewerten-vue-pds"]'
        #                       '//section[@class="shop-grid-row"]'
        #                       '/div[contains(@class,"bewerten-pds-summary")]//span/text()'
        #                       )
        name = response.xpath('//span[@itemprop="name"]/text()').extract()
        return name

