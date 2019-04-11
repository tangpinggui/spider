# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from SpiderAnything.items import HrItem, SunshineItem

import re


client = MongoClient()
collection = client['SpiderAnything']['hr']


class SpideranythingPipeline(object):
    def process_item(self, item, spider):
        if spider.name == 'hr':
            print(item)

            collection.insert(dict(item))
            return item


class SpideranythingPipeline1(object):
    def process_item(self, item, spider):
        print(isinstance(item, HrItem), 'hr')
        if isinstance(item, HrItem):
            collection.insert(dict(item))
            return item


class SunshinePipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, SunshineItem):
            item['content_text'] = self.process_content_text(item['content_text'])
            item['content_img'] = self.process_content_img(item['content_img'])
            collection.insert(dict(item))
            return item

    def process_content_text(self, content):
        content = [re.sub(r'\xa0|s\t', '', i) for i in content]
        content = content[0]
        return content

    def process_content_img(self, content_img):
        content_img = ['http://wz.sun0769.com' + i for i in content_img if i]
        return content_img