import scrapy
import json
import re
from scrapy_splash import SplashRequest


class IndexSpider(scrapy.Spider):
    name = 'index'
    allowed_domains = ['www.flickr.com']
    start_urls = ['http://www.flickr.com/']

    def parse(self, response):
        pass
