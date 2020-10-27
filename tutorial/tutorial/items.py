# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PostItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()


class ProductItem(scrapy.Item):
    name = scrapy.Field()
    brand = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()
    image = scrapy.Field()