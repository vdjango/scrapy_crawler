# -*- coding: utf-8 -*-
import json
import re

import scrapy

from scrapy_crawler.items import ScrapyImagesItem


class PaintingSpider(scrapy.Spider):
    name = 'painting'
    allowed_domains = ['image.baidu.com']  # 允许爬取的域名
    start_urls = [
        'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&fp=result&ie=utf-8&oe=utf-8&word={}&pn='
    ]

    def __init__(self, name=None, **kwargs):
        super(PaintingSpider, self).__init__(name, **kwargs)
        self.search_word = [
            '课堂趴桌子',
            '课堂举手'
            # 修改具体爬取的分类（搜索关键词）
        ]
        self.pn = []
        self.page = 1

    def get_image_uri_next(self, meta):
        """
        获取下一页数据
        :return:
        """
        item_word = meta['word']  # 通过上面的meta传递过来item
        item_index = meta['index_append']  # 通过上面的meta传递过来item

        uri = self.start_urls[0].format(item_word)
        uri += str(self.pn[item_index])
        self.pn[item_index] += 20
        return uri

    def start_requests(self):
        for word in self.search_word:
            self.pn.append(0)
            word_index = self.search_word.index(word)

            meta = {
                'word': word, 'index_append': word_index
            }
            yield scrapy.Request(
                self.get_image_uri_next(meta), dont_filter=True,
                meta=meta
            )

    def parse(self, response):
        response_json = response.text
        response_json.encode('utf-8').decode('unicode_escape')

        try:
            response_dict = json.loads(
                response_json,
                strict=False
            )
        except Exception:
            middle = re.findall(r'"middleURL":.?"(.*?)",', response_json)
            list_num = re.findall(r'"listNum":.?(.*?),', response_json)
            data = [{
                'middleURL': i,
                'fromPageTitleEnc': None,
                'pageNum': None
            } for i in middle]

            response_dict = {
                'data': data,
                'listNum': list_num[0],
            }

        response_dict_data = response_dict['data']  # 图片的有效数据在data参数中
        self.page = response_dict['listNum']

        index_append = response.meta['index_append']

        item = ScrapyImagesItem()
        for pic in response_dict_data:
            if not pic: continue
            item['word'] = self.search_word[index_append]
            item['image'] = [pic['middleURL']]
            item['name'] = pic['fromPageTitleEnc']
            item['page'] = pic['pageNum']
            yield item

        if self.pn[index_append] < self.page:
            next_url = self.get_image_uri_next(response.meta)
            next_url = response.urljoin(next_url)
            yield scrapy.Request(next_url, callback=self.parse, meta=response.meta)
