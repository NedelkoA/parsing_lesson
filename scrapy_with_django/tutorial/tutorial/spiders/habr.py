import scrapy
from ..items import PostItem


class HabrSpider(scrapy.Spider):
    name = 'habr'
    start_urls = ['https://habr.com']

    def parse(self, response):
        urls_post = response.xpath(
            '//li/article[contains(@class,"post")]'
            '/h2[@class="post__title"]/a[@class="post__title_link"]/@href'
        ).extract()
        for url in urls_post:
            yield scrapy.Request(url, callback=self.parse_post)

    def parse_post(self, response):
        item = PostItem()
        item['title'] = self.parse_title(response)
        item['description'] = self.parse_description(response)
        yield item

    def parse_title(self, response):
        return response.xpath(
            '//div[@class="post__wrapper"]/h1[contains(@class,"post__title")]/span/text()'
        ).extract()

    def parse_description(self, response):
        content = response.xpath(
            '//div[@class="post__wrapper"]/div[contains(@class,"post__body")]'
            '/div[contains(@class,"post__text")]//text()'
        ).extract()
        return ''.join([i.strip() for i in content])
