# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

from scrapy import signals
from scrapy.contrib.exporter import CsvItemExporter


class JianshuwordlePipeline(object):
    def process_item(self, item, spider):
        return item


class PagePipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db = self.client['jianshu']
        self.collection = self.db['page']

    def process_item(self, item, spider):
        data = {
            'title': item['title'],
            'link': item['link'],
            'time': item['time'],
            'read': item['read'],
            'comments': item['comments'],
            'like': item['like'],
            'money': item['money'],
        }
        self.collection.insert_one(data)
        print 'insert'
        return item

    def close_spider(self, spider):
        pass


class CSVPipeline(object):

    def __init__(self):
        self.files = {}

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline


    def spider_opened(self, spider):
        file = open('%s_items.csv' % spider.name, 'w+b')
        self.files[spider] = file
        self.exporter = CsvItemExporter(file)
        self.exporter.fields_to_export = [
            'title',
            'link',
            'time',
            'read',
            'comments',
            'like',
            'money',
        ]
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()


    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


class WordCloudPipeline(object):
    pass