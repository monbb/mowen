#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    run.py
    ~~~~~~~~~~~~~~~~~~~~~~~
    
    Description of this file
    
    :author: yatming
    :copyright: (c) 2020
    :date created: 2021/7/28
    
"""
from lxml.html import etree
import requests

from backend.configs import ua


class TaskExecutor(object):

    def __init__(self, url, headers=None):
        self.url = url
        self.userAgent = ua.random
        self.cookie = None
        self.headers = headers

    def set_headers(self, params:dict) -> dict:
            headers = {
                'User-Agent': self.userAgent
            }
            if isinstance(params, dict):
                headers.update(params)
            return headers

    def parse_html(self, html: str, xpath: str):
        xpath_parser = etree.HTML(html)
        return xpath_parser.xpath(xpath)

    def run(self):

        headers = self.set_headers(params=self.headers)
        rsp = requests.get(
            url=self.url,
            headers=headers
        )
        html_text = rsp.content.decode("utf-8")
        xpath_exp = '/html/body/article/div[@class="main"]/section[@class="section_cake"]/ul//li'
        cake_ele_nodes = self.parse_html(html_text, xpath_exp)
        for node in cake_ele_nodes:
            img_xpath = './div[@class="item_info"]/div[@class="item_message"]//a[@class="img_link"]//img/@data-original'
            ele = node.xpath(img_xpath)
            print(ele)


if __name__ == '__main__':
    from backend.configs import Targets
    url = Targets.LECAKE
    header = {
        "Host": "www.lecake.com"
    }
    task = TaskExecutor(
        url=url,
        headers=header
    )
    task.run()