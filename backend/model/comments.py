#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    comments.py
    ~~~~~~~~~~~~~~~~~~~~~~~
    
    Description of this file
    
    :author: yatming
    :copyright: (c) 2020
    :date created: 2021/8/9
    
"""
from pymongo import ReadPreference
from pymongo.collection import Collection

from backend.model import (
    CollectionName,
    db
)

class Comments(object):
    """
    * `_id` (str) - id
    * `img_url` (str) - 背景图url
    * `nick_phone` (str) - 假号码
    * `date` (str) - 日期
    * `text` (str) - 评论内容
    * `is_hot` (bool) - 是否热评
    """

    class Field(object):
        _id = "_id"
        img_url = "img_url"
        nick_phone = "nick_phone"
        text = "text"
        date = "date"
        is_hot = "is_hot"


    COL_NAME = CollectionName.Comments

    p_col = Collection(
        db, COL_NAME,
        read_preference=ReadPreference.PRIMARY_PREFERRED
    )

    s_col = Collection(
        db, COL_NAME,
        read_preference=ReadPreference.SECONDARY_PREFERRED
    )