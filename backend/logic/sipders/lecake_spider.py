#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    lecake_spider.py
    ~~~~~~~~~~~~~~~~~~~~~~~
    
    Description of this file
    
    :author: yatming
    :copyright: (c) 2020
    :date created: 2021/7/28
    
"""
import random
import re

from bson import ObjectId
import js2py
from lxml.html import etree
import requests

from backend.configs import agent_list
from backend.model.hot_goods import HotGoods
from backend.model.shuffling_figure_config import ShufflingFigureConfig
from backend.model.comments import Comments
from backend.model.goods import Goods


class TaskExecutor(object):

    def __init__(self, url, headers=None):
        self.goods_list = list()
        self.comments = list()
        self.figure_config_list = list()
        self.hot_list = list()
        self.failed_url_list = list()
        self.url = url
        self.userAgent = random.choice(agent_list)
        self.cookie = None
        self.headers = headers
        self.targets = dict()

    def set_headers(self, params: dict) -> dict:
        headers = {
            'User-Agent': self.userAgent
        }
        if isinstance(params, dict):
            headers.update(params)
        return headers

    @staticmethod
    def parse_html(html: str, xpath: str):
        xpath_parser = etree.HTML(html)
        return xpath_parser.xpath(xpath)

    def lecake_index(self, headers):
        rsp = requests.get(
            url=self.url,
            headers=headers
        )
        html_text = rsp.content.decode("utf-8")
        # 轮播图数据
        xpath_exp = '/html/body/article/div[@class="main"]/section[@id="bannerSwiper"]/ul[@class="swiper-wrapper"]//li'
        shuffling_figure_nodes = self.parse_html(html_text, xpath_exp)
        for node in shuffling_figure_nodes:
            figure_img_url_xpath = "./a/img/@src"
            figure_url = node.xpath(figure_img_url_xpath)[0]  # 轮播图url
            title_xpath = './a/div/p[@class="main_title"]/text()'
            title = node.xpath(title_xpath)  # title
            sub_title_xpath = './a/div/p[@class="sub_title"]/text()'
            sub_title = node.xpath(sub_title_xpath)  # sub_title
            self.figure_config_list.append({
                ShufflingFigureConfig.Field._id: str(ObjectId()),
                ShufflingFigureConfig.Field.title: title,
                ShufflingFigureConfig.Field.sub_title: sub_title,
                ShufflingFigureConfig.Field.figure_url: figure_url
            })

        # 热门评论
        xpath_exp = '/html/body/article/div[@class="main"]/section[@class="comment_section"]/div[@id="comments"]/ul//li//div[@class="comment_item"]'
        hot_comment_nodes = self.parse_html(html_text, xpath_exp)
        for node in hot_comment_nodes:
            # 评论图片
            comment_img_url_xpath = './div[@class="img_goods"]/a/img/@data-original'
            comment_img_url = node.xpath(comment_img_url_xpath)[0]  # 商品图片url
            comment_content_xpath = './div[@class="comment_content"]/p[@class="nick"]/text()'
            comment_content_nick = node.xpath(comment_content_xpath)  # 号码/日期
            nick_info = comment_content_nick[0].strip().split('\n')
            nick_phone = nick_info[0].strip()  # 号码
            date = nick_info[1].strip()  # 日期
            comment_text_xpath = './div[@class="comment_content"]/p[@class="text"]/text()'
            text = node.xpath(comment_text_xpath)[0]  # 评论内容
            self.comments.append({
                Comments.Field._id: str(ObjectId()),
                Comments.Field.img_url: comment_img_url,
                Comments.Field.nick_phone: nick_phone,
                Comments.Field.date: date,
                Comments.Field.text: text,
                Comments.Field.is_hot: True
            })

        # HOT商品矩阵
        xpath_exp = '/html/body/article/div[@class="main"]/section[@class="section_cake"]/ul//li'
        cake_ele_nodes = self.parse_html(html_text, xpath_exp)
        for node in cake_ele_nodes:
            goods_url = self.url + node.xpath('./div[@class="item_info"]/div/a/@href')[0]
            img_xpath = './div[@class="item_info"]/div[@class="item_message"]//a[@class="img_link"]//img/@data-original'
            img_url = node.xpath(img_xpath)[0]  # 首页图片url
            label_message_xpath = './/div[@class="item_message"]/a//b'
            label_info = node.xpath(label_message_xpath)
            label = None
            if label_info:
                label = label_info[0].text  # 左上角标签
            tag_xpath = './/div[@class="item_message"]/div[@class="item_detail"]/div[@class="name_wrap"]//div[@class="p_tag"]/span'
            tag_list = node.xpath(tag_xpath)
            tag = None
            if tag_list:
                tag = tag_list[0].text  # 优惠标签
            title_xpath = './/div[@class="item_message"]/div[@class="item_detail"]/div[@class="name_wrap"]//h3'
            title_list = node.xpath(title_xpath)
            title = title_list[0].text  # 名称
            recommend_xpath = './/div[@class="item_message"]/div[@class="item_detail"]/div[@class="name_wrap"]//div[@class="recommend_reason no_wrap"]'
            recommend_reason_info = node.xpath(recommend_xpath)[0].text.strip()  # 推荐原因
            price_xpath = './/div[@class="item_message"]/div[@class="item_detail"]/div[@class="price_wrap"]/p/text()'
            price = node.xpath(price_xpath)[1].strip()  # 价格
            self.hot_list.append({
                HotGoods.Field._id: str(ObjectId()),
                HotGoods.Field.goods_url: goods_url,
                HotGoods.Field.img_url: img_url,
                HotGoods.Field.label: label,
                HotGoods.Field.tag: tag,
                HotGoods.Field.title: title,
                HotGoods.Field.recommend_reason_info: recommend_reason_info,
                HotGoods.Field.price: price
            })

    def lecake_second_page(self, headers, handler):
        second_url = "https://www.lecake.com/GZ/category-0-1.html"

        rsp = requests.get(
            url=second_url,
            headers=headers
        )

        html_text = rsp.content.decode('utf-8')

        xpath = '/html/body/article[@class="container main_goods_list"]//section[@class="p_list_wrap"]/ul//li/a/@href'

        nodes = self.parse_html(html_text, xpath)

        for link in nodes:
            self.targets[link] = handler

    def lecake_goods_page(self, headers, url):
        cookies = {
            '_zzuid': 'MEd0tLldkc9u',
            'PHPSESSID': '47ef9e35a768f24c50480a077032f7a3',
            'Hm_lvt_0aab2028932298cda55c549351d0a22b': '1628062439',
            'CITY_ALIAS': 'SZ',
            'CITY_ID': 'SZ_228',
            'Hm_lpvt_0aab2028932298cda55c549351d0a22b': '1628081506',
        }

        headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '^\\^',
            'sec-ch-ua-mobile': '?0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': 'https://www.lecake.com/SZ/category-0-1.html',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

        url = self.url + url
        rsp = requests.get(url, headers=headers, cookies=cookies)
        html_text = rsp.content.decode('utf-8')
        xpath = '/html/body/script[1]/text()'
        target_js = self.parse_html(html_text, xpath)[0]
        string = target_js.strip()
        reg_exp = r"(var goods = .*?};)"
        re_compile_obj = re.compile(reg_exp, re.S)
        goods_string = re_compile_obj.findall(string)[0]
        ctx = js2py.EvalJs()
        ctx.execute(goods_string)
        result = ctx.goods

        error = result.error
        if error == 1:
            self.failed_url_list.append(url)
            return
        # 获取商品详情
        goods_name = result.goodName
        market_price = result.marketPrice
        main_pic_url = result.pictures[0]
        remind = result.remind
        spec = result.spec
        aboutOrder = result.aboutOrder
        aboutShipping = result.aboutShipping
        brief = result.brief
        dessertShopRecommendReason = result.dessertShopRecommendReason
        midCategoryName = result.midCategoryName
        tasteLabel = result.tasteLabel
        warmHint = result.warmHint
        postId = result.postId
        # 商品详情图片
        xpath = '/html/body//div[@class="img"]/img/@src'
        details_urls = self.parse_html(html_text, xpath)
        self.goods_list.append({
            Goods.Field._id : str(ObjectId()),
            Goods.Field.name: goods_name,
            Goods.Field.market_price: market_price,
            Goods.Field.main_pic_url: main_pic_url,
            Goods.Field.spec: spec,
            Goods.Field.aboutOrder: aboutOrder,
            Goods.Field.aboutShipping: aboutShipping,
            Goods.Field.brief: brief,
            Goods.Field.dessertShopRecommendReason: dessertShopRecommendReason,
            Goods.Field.midCategoryName: midCategoryName,
            Goods.Field.tasteLabel: tasteLabel,
            Goods.Field.warmHint: warmHint,
            Goods.Field.postId: postId,
            Goods.Field.details: details_urls,
            Goods.Field.remind: remind
        })


    def run(self):

        headers = self.set_headers(params=self.headers)

        self.lecake_index(header)

        self.lecake_second_page(header, self.lecake_goods_page)

        # self.lecake_goods_page(headers, list(self.targets.keys())[0])
        for link in self.targets.keys():
            self.lecake_goods_page(headers, link)

        self.bulk_write_data()

        print("finish")

    def bulk_write_data(self):
        result = HotGoods.p_col.insert_many(self.hot_list)
        print(result.inserted_ids)
        result = Comments.p_col.insert_many(self.comments)
        print(result.inserted_ids)
        result = ShufflingFigureConfig.p_col.insert_many(self.figure_config_list)
        print(result.inserted_ids)
        result = Goods.p_col.insert_many(self.goods_list)
        print(result.inserted_ids)


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
