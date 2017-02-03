# -*- coding: UTF-8 -*-

import random
from JianShuWordle.settings import HTTP_PROXYS


class RandomProxy(object):
    """
    随机代理
    """

    def process_request(self, request, spider):
        request.meta['proxy'] = random.choice(HTTP_PROXYS)
        print request.meta['proxy']

