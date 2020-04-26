# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyImagesItem(scrapy.Item):
    word = scrapy.Field()  # 搜索关键字
    name = scrapy.Field()  # 图片标题
    image = scrapy.Field()  # 图片url
    page = scrapy.Field()  # 图片url
    pass
