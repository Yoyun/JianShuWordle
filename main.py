# -*- coding: UTF-8 -*-

from scrapy import cmdline

cmdline.execute('scrapy crawl page'.split())
# cmdline.execute('scrapy crawl page -o page.csv -t csv'.split())

