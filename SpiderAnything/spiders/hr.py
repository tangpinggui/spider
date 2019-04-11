# -*- coding: utf-8 -*-
import scrapy
from SpiderAnything.items import HrItem


class HrSpider(scrapy.Spider):
    name = 'hr'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    def parse(self, response):
        tr_list = response.xpath("//table[@class='tablelist']/tr")[1:-1]
        item = HrItem()
        for tr in tr_list:
            item['title'] = tr.xpath("./td[1]/a/text()").extract_first()
            item['position'] = tr.xpath("./td[2]/text()").extract_first()
            item['pub_date'] = tr.xpath("./td[5]/text()").extract_first()
            yield item
        # 请求下一页  需要settings USER_AGENT
        next_url = response.xpath("//a[@id='next']/@href").extract_first()
        if next_url != "javascript:;":
            next_url = 'https://hr.tencent.com/' + next_url

            yield scrapy.Request(
                next_url,
                callback=self.parse # 调用处理方法
            )
