# -*- coding: utf-8 -*-
import random
import re
from time import sleep

import scrapy

from scrapy_crawler.items import BiliVideoItem


class BiliBiliVideoSpider(scrapy.Spider):
    """
    爬取b站视频
    """
    name = 'bilibili'
    allowed_domains = ['search.bilibili.com', 'www.bilibili.com']  # 允许爬取的域名
    start_urls = 'https://search.bilibili.com/all?keyword={}&page='

    def __init__(self, name=None, **kwargs):
        super(BiliBiliVideoSpider, self).__init__(name, **kwargs)
        self.search_word = [
            '汉服',
            # 修改具体爬取的分类（搜索关键词）
        ]
        self.header = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q = 0.9'
        }
        self.pn = []
        self.page = 0
        self.page_max = 1
        self._next = []

    def get_next(self, meta):
        """
        获取下一页数据
        :return:
        """
        item_word = meta['word']  # 通过上面的meta传递过来item
        uri = self.start_urls.format(item_word)

        if self.page > self.page_max:
            return None

        self.page += 1

        return uri + str(self.page)

    def start_requests(self):
        for word in self.search_word:
            self.pn.append(0)
            word_index = self.search_word.index(word)

            meta = {
                'word': word,
                'type': self.name,
                'index_append': word_index
            }

            url = self.get_next(meta)
            if not url: return
            yield scrapy.Request(
                url, dont_filter=True,
                meta=meta, headers=self.header
            )

    def parse(self, response):
        text = response.text
        text.encode('utf-8').decode('unicode_escape')

        rec = re.findall('<li class="video-item matrix"><a.*?href=".*?".*?>', str(text).replace('\n', ''))
        rec = re.findall('href="//(.*?)" title="(.*?)"', ''.join(rec))

        video_next = re.findall('<div class="pager">.*</div>', str(response.text).replace('\n', ''))
        video_next = re.findall('<li class="page-item last">.*?</li>', ''.join(video_next))
        video_next = re.findall('<button class="pagination-btn">.*?</button>', ''.join(video_next))
        video_next = re.findall('>.*?<', ''.join(video_next))
        self.page_max = int(re.findall('\d+', ''.join(video_next)).pop())

        index_append = response.meta['index_append']
        item = BiliVideoItem()
        for uri, name in rec:
            item['word'] = self.search_word[index_append]
            item['type'] = self.name
            item['uri'] = uri
            item['name'] = name
            item['page'] = self.page
            a = random.randint(1, 4)
            b = random.randint(1, 8)
            c = random.randint(a, a + b)
            sleep(c)
            yield item

        url = self.get_next(response.meta)
        print('url', url)
        if url:
            a = random.randint(1, 5)
            b = random.randint(1, 9)
            c = random.randint(a, a + b)
            sleep(c)
            yield scrapy.Request(url, callback=self.parse, meta=response.meta, headers=self.header)
