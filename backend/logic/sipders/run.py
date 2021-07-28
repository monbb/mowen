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
            img_url = node.xpath(img_xpath)[0] # 首页图片url
            label_message_xpath = './/div[@class="item_message"]/a//b'
            label_info = node.xpath(label_message_xpath)
            if label_info:
                label = label_info[0].text # 左上角标签
            tag_xpath = './/div[@class="item_message"]/div[@class="item_detail"]/div[@class="name_wrap"]//div[@class="p_tag"]/span'
            tag_list = node.xpath(tag_xpath)
            if tag_list:
                tag = tag_list[0].text # 优惠标签
            title_xpath = './/div[@class="item_message"]/div[@class="item_detail"]/div[@class="name_wrap"]//h3'
            title_list = node.xpath(title_xpath)
            title = title_list[0].text # 名称
            recommend_xpath = './/div[@class="item_message"]/div[@class="item_detail"]/div[@class="name_wrap"]//div[@class="recommend_reason no_wrap"]'
            recommend_reason_info = node.xpath(recommend_xpath)[0].text.strip() # 推荐原因
            price_xpath = './/div[@class="item_message"]/div[@class="item_detail"]/div[@class="price_wrap"]/p/text()'
            price = node.xpath(price_xpath)[1].strip() # 价格





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