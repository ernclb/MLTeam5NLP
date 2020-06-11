# -*- coding: utf-8 -*-
import scrapy
from bnz_scrapy.items import BnzScrapyItem


class BnzSpider(scrapy.Spider):
    name = 'bnz'
    allowed_domains = ['community.bnz.co.nz']
    start_urls = ['http://community.bnz.co.nz/latest/']

    def parse(self, response):
        item = BnzScrapyItem()
        latest_list = response.xpath('//tbody/tr')
        for topic in latest_list:
            item['title'] = topic.xpath('.//*[@class="link-top-line"]/a/text()').extract_first()
            item['tag'] = topic.xpath('.//*[@class="category-name"]/text()').extract_first()
            item['link'] = topic.xpath('.//*[@class="link-top-line"]/a/@href').extract_first()
            yield item
