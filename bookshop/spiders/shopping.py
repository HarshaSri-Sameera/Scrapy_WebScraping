# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ShoppingSpider(CrawlSpider):
    name = 'shopping'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/index.html']
        
    # The first Rule object will handle opening each book URL
    # The second Rule object will handle pagination
    rules = (
        Rule(LinkExtractor(restrict_xpaths="//article[@class='product_pod']/div/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//li[@class='next']/a/@href"))
    )

    def parse_item(self, response):
        yield {
            'Name': response.xpath("//li[@class='col-xs-6 col-sm-4 col-md-3 col-lg-3']//a/img/@alt").get(),
            'Price': response.xpath("//p[@class='price_color']/text()").get()
        }
