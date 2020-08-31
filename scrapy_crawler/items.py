# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyImagesItem(scrapy.Item):
    """
    百度图片
    """
    word = scrapy.Field()  # 搜索关键字
    name = scrapy.Field()  # 图片标题
    image = scrapy.Field()  # 图片url
    page = scrapy.Field()  # 图片url
    pass


class BiliVideoItem(scrapy.Item):
    """
    b站视频
    """
    type = scrapy.Field()  # 搜索关键字
    word = scrapy.Field()  # 搜索关键字
    name = scrapy.Field()  # 图片标题
    uri = scrapy.Field()  # 图片url
    page = scrapy.Field()  # 图片url
