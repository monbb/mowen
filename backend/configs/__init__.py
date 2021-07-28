#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    __init__.py.py
    ~~~~~~~~~~~~~~~~~~~~~~~
    
    Description of this file
    
    :author: yatming
    :copyright: (c) 2020
    :date created: 2021/7/27
    
"""
from fake_useragent import UserAgent

try:
    ua = UserAgent()
except:
    ua = UserAgent()


class Targets(object):

    LECAKE = "https://www.lecake.com"

    targets = [
        LECAKE
    ]

