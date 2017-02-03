# -*- coding: UTF-8 -*-

import scrapy
from JianShuWordle.items import PageItem


class PageSpider(scrapy.Spider):
    name = 'page'
    allowed_domains = ['jianshu.com']
    start_urls = ['http://www.jianshu.com/trending/monthly']
    page = 1

    def parse(self, response):

        # 获取文章列表
        note_list = response.css('div#list-container>ul.note-list>li')
        if len(note_list) == 0:
            return

        for sel in note_list:

            # 去除官网安利文章
            info = sel.css('div.meta>*')
            if len(info) < 4:
                continue

            title = sel.css('a.title::text')[0].extract().strip()
            link = 'http://www.jianshu.com'+(sel.css('a.title::attr(href)')[0].extract())
            time = sel.css('span.time::attr(data-shared-at)')[0].extract()
            read = ''.join(info[0].xpath('text()').extract()).strip()
            comments = ''.join(info[1].xpath('text()').extract()).strip()
            like = info[2].xpath('text()')[0].extract().strip()
            money = info[3].xpath('text()')[0].extract().strip()

            item = PageItem()
            item['title'] = title
            item['link'] = link
            item['time'] = time
            item['read'] = int(read)
            item['comments'] = int(comments)
            item['like'] = int(like)
            item['money'] = int(money)
            yield item

        # 翻页
        self.page += 1
        new_url = '%s?page=%d' % (self.start_urls[0], self.page)
        yield scrapy.Request(new_url, callback=self.parse)
