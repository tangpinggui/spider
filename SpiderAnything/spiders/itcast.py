# -*- coding: utf-8 -*-
import scrapy
import logging


logger = logging.getLogger(__name__)


class ItcastSpider(scrapy.Spider):
    name = 'itcast' # 爬虫名字
    allowed_domains = ['itcast.cn'] # 爬取范围
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml'] # 最开始请求的url地址

    def parse(self, response):
        # 处理start_urls地址对应的响应  extract提取文字
        # res = response.xpath("//div[@class='li_txt']//h3/text()").extract()
        # print(res)

        # 分组
        li_list = response.xpath("//div[@class='li_txt']")
        for li in li_list:
            item = {} # 存入pipeline  settings开启ITEM_PIPELINES
            item['tea_name'] = li.xpath(".//h3/text()").extract_first()
            item['tea_position'] = li.xpath(".//h4/text()").extract_first()
            # 减少内存占用 存入pipeline
            # yield item
            logger.warning(item) # debug info