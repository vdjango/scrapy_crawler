# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os

from scrapy.pipelines.images import ImagesPipeline

from scrapy import Request


class ScrapyImagesPipeline(object):
    def process_item(self, item, spider):
        return item


class DownloadImagesPipeline(ImagesPipeline):

    def __init__(self, *args, **kwargs):
        super(DownloadImagesPipeline, self).__init__(*args, **kwargs)
        self.num = 1

    def get_media_requests(self, item, info):
        """
        下载图片
        :param item:
        :param info:
        :return:
        """
        for image_url in item['image']:
            yield Request(
                image_url,
                meta={
                    'item': item, 'index': item['image'].index(image_url)
                }
            )  # 添加meta是为了下面重命名文件名使用

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']  # 通过上面的meta传递过来item

        filename = os.path.join(item['word'], '{}.jpg'.format(str(self.num)))
        self.num += 1
        return filename
