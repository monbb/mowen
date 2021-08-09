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
import os

from fake_useragent import UserAgent
import yaml

try:
    ua = UserAgent()
except:
    ua = UserAgent()



BASE_DIR = os.path.dirname(os.path.abspath(__file__))

yaml_file = open(os.path.join(BASE_DIR, 'configs.yaml'), 'r', encoding='utf8')

config_obj = yaml.safe_load(yaml_file)

yaml_file.close()



class Targets(object):

    LECAKE = "https://www.lecake.com"

    targets = [
        LECAKE
    ]

