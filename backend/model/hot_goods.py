#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    hot_goods.py
    ~~~~~~~~~~~~~~~~~~~~~~~
    
    Description of this file
    热点商品模型
    :author: yatming
    :copyright: (c) 2020,
    :date created: 2021/8/9
    
"""
from pymongo import ReadPreference
from pymongo.collection import Collection

from backend.model import (
    CollectionName,
    db
)

class HotGoods(object):
    """
    * `_id` (str) - id
    * `img_url` (str) - 主图片url
    * `label` (str) - 左上角标签
    * `tag` (str) - 优惠标签
    * `title` (str) - 名称
    * `recommend_reason_info` (str) - 推荐原因
    * `price` (int) - 价格
    """

    class Field(object):
        _id = "_id"
        img_url = "img_url"
        label = "label"
        tag = "tag"
        title = "title"
        goods_url = "goods_url"
        recommend_reason_info = "recommend_reason_info"
        price = "price"

    COL_NAME = CollectionName.HotGoods

    p_col = Collection(
        COL_NAME, db,
        read_preference=ReadPreference.PRIMARY_PREFERRED
    )

    s_col = Collection(
        COL_NAME, db,
        read_preference=ReadPreference.SECONDARY_PREFERRED
    )

