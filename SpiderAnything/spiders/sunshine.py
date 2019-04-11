# -*- coding: utf-8 -*-
import scrapy
from SpiderAnything.items import SunshineItem


class SunshineSpider(scrapy.Spider):
    name = 'sunshine'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    def parse(self, response):
        tr_list= response.xpath("//div[@class='greyframe']/table[2]/tr/td/table/tr")
        item = SunshineItem()
        for tr in tr_list:
            item['title'] = tr.xpath("./td[2]//a[2]/text()").extract_first()
            item['addr'] = tr.xpath("./td[2]//a[3]/text()").extract_first()
            item['status'] = tr.xpath("./td[3]/span/text()").extract_first()
            item['name'] = tr.xpath("./td[4]/text()").extract_first()
            item['pub_date'] = tr.xpath("./td[last()]/text()").extract_first()
            item['content_href'] = tr.xpath("./td[2]//a[2]/@href").extract_first()
            yield scrapy.Request(
                item['content_href'],
                self.parse_detail,
                meta={'item': item}
            )

    def parse_detail(self, response):
        item = response.meta['item']
        item['content_img'] = response.xpath("//div[@class='textpic']/img/@src").extract()
        content_text = response.xpath("//div[@class='contentext']/text()").extract()
        if not content_text:
            content_text = response.xpath("//td[@class='txt16_3']/text()").extract()
        item['content_text'] = content_text
        yield item
