#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    __init__.py.py
    ~~~~~~~~~~~~~~~~~~~~~~~
    
    Description of this file
    
    :author: yatming
    :copyright: (c) 2020
    :date created: 2021/7/28
    
"""

from pymongo import MongoClient

from backend.configs import config_obj


def get_db(db, host='localhost:27017',
           is_auth=False, user='', passwd='',
           is_replica=False, replica=''):
    """
    获取数据库实例
    :param db: 数据库名称
    :param host: 地址
    :param is_auth: 是否认证用户
    :param user: 用户名
    :param passwd: 密码
    :param is_replica: 是否集群
    :param replica: 集群名称
    :return:
    """

    if is_replica:
        url = 'mongodb://%s/?replicaSet=%s' % (host, replica)
    else:
        url = host

    client = MongoClient(url, connect=False, maxPoolSize=50)
    connection = client[db]

    if is_auth:
        connection.authenticate(user, passwd)

    return connection


class CollectionName(object):

    HotGoods = "hot-goods" # 热点商品
    ShufflingFigureConfig = "shuffling-figure-config" # 首页轮播图配置
    Customer = "customer" # 用户表
    Goods = "goods" # 商品
    Comments = "comments" # 评论



db = get_db(
    config_obj['mongo']['db'],
    config_obj['mongo']['host'],
    config_obj['mongo']['is_auth'],
    config_obj['mongo']['user'],
    config_obj['mongo']['pwd'],
    config_obj['mongo']['is_replica'],
    config_obj['mongo']['replica']
)
