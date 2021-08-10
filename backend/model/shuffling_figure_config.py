#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    shuffling_figure_config.py
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

class ShufflingFigureConfig(object):
    """
    * `_id` (str) - id
    * `figure_url` (str) - 轮播图url
    * `title` (str) - 主题
    * `sub_title` (str) - 子主题
    """

    class Field(object):
        _id = "_id"
        figure_url = "figure_url"
        title = "title"
        sub_title = "sub_title"


    COL_NAME = CollectionName.ShufflingFigureConfig

    p_col = Collection(
        db, COL_NAME,
        read_preference=ReadPreference.PRIMARY_PREFERRED
    )

    s_col = Collection(
        db, COL_NAME,
        read_preference=ReadPreference.SECONDARY_PREFERRED
    )

    @classmethod
    def get_configs(cls):
        return cls.s_col.find()