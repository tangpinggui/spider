# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HrItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    position = scrapy.Field()
    pub_date = scrapy.Field()


class SunshineItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    addr = scrapy.Field()
    status = scrapy.Field()
    name = scrapy.Field()
    pub_date = scrapy.Field()
    content_href = scrapy.Field()
    content_img = scrapy.Field()
    content_text = scrapy.Field()