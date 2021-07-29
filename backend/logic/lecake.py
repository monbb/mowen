#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    lecake.py
    ~~~~~~~~~~~~~~~~~~~~~~~
    
    Description of this file
    
    :author: yatming
    :copyright: (c) 2020, Tungee
    :date created: 2021/7/29
    
"""
import requests


def lecake_spider():
    headers = self.set_headers(params=self.headers)
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

    # 商品矩阵
    xpath_exp = '/html/body/article/div[@class="main"]/section[@class="section_cake"]/ul//li'
    cake_ele_nodes = self.parse_html(html_text, xpath_exp)
    for node in cake_ele_nodes:
        img_xpath = './div[@class="item_info"]/div[@class="item_message"]//a[@class="img_link"]//img/@data-original'
        img_url = node.xpath(img_xpath)[0]  # 首页图片url
        label_message_xpath = './/div[@class="item_message"]/a//b'
        label_info = node.xpath(label_message_xpath)
        if label_info:
            label = label_info[0].text  # 左上角标签
        tag_xpath = './/div[@class="item_message"]/div[@class="item_detail"]/div[@class="name_wrap"]//div[@class="p_tag"]/span'
        tag_list = node.xpath(tag_xpath)
        if tag_list:
            tag = tag_list[0].text  # 优惠标签
        title_xpath = './/div[@class="item_message"]/div[@class="item_detail"]/div[@class="name_wrap"]//h3'
        title_list = node.xpath(title_xpath)
        title = title_list[0].text  # 名称
        recommend_xpath = './/div[@class="item_message"]/div[@class="item_detail"]/div[@class="name_wrap"]//div[@class="recommend_reason no_wrap"]'
        recommend_reason_info = node.xpath(recommend_xpath)[0].text.strip()  # 推荐原因
        price_xpath = './/div[@class="item_message"]/div[@class="item_detail"]/div[@class="price_wrap"]/p/text()'
        price = node.xpath(price_xpath)[1].strip()  # 价格