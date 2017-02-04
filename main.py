# -*- coding: UTF-8 -*-

from scrapy import cmdline
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

cmdline.execute('scrapy crawl page'.split())
# cmdline.execute('scrapy crawl page -o page.csv -t csv'.split())

