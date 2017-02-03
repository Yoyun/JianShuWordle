# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JianshuwordleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class PageItem(scrapy.Item):
    title = scrapy.Field()      # 标题
    link = scrapy.Field()       # 链接
    time = scrapy.Field()       # 时间
    read = scrapy.Field()       # 阅读数
    comments = scrapy.Field()    # 评论数
    like = scrapy.Field()       # 喜欢数
    money = scrapy.Field()      # 打赏数
