# -*- coding: UTF-8 -*-

import random
from JianShuWordle.settings import USER_AGENTS


class RandomUserAgent(object):
    """
    随机生成 User-Agent
    """

    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', random.choice(USER_AGENTS))

