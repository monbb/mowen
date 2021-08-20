#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    index.py
    ~~~~~~~~~~~~~~~~~~~~~~~
    
    Description of this file
    
    :author: yatming
    :copyright: (c) 2020
    :date created: 2021/8/10
    
"""
from backend.model.shuffling_figure_config import ShufflingFigureConfig
from backend.model.hot_goods import HotGoods


def logic_get_lecake_shuffling_figure_config() -> (bool, int, dict):
    cur = ShufflingFigureConfig.get_configs()
    data = list(cur)
    return True, 0, data


def logic_get_lecake_hot_goods():
    cur = HotGoods.get_goods()
    data = list(cur)
    return True, 0, data
