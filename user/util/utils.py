#! /usr/bin/env python
# -*- coding: utf-8 -*-

import uuid
import datetime
import time


# 随机字符串
def random_str():
    return str(uuid.uuid1()).replace('-', '')[:20]


# datetime -> timestamp
def datetime2timestamp(date):
    return time.mktime(date.timetuple())


# timestamp -> datetime
def timestamp2datetime(date):
    return datetime.datetime.fromtimestamp(float(date))