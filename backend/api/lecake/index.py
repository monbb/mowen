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
from flask import (
    request,
    jsonify
)
from werkzeug.exceptions import abort

from backend.api import api_router as api
from backend.logic.lecake.index import (
    logic_get_lecake_shuffling_figure_config,
    logic_get_lecake_hot_goods, logic_get_lecake_hot_comment
)


@api.route('/lecake/test', methods=['GET'])
def test_api():
    return jsonify(stat=1, msg="success"), 200


@api.route('/lecake/index/shuffling-figure', methods=['GET'])
def index_shuffling_figure_config():
    ok, err_code, configs = logic_get_lecake_shuffling_figure_config()

    if not ok:
        return jsonify(), 400

    return jsonify(data=configs), 200


@api.route('/lecake/index/hot-goods', methods=['GET'])
def index_hot_goods():
    ok, err_code, goods = logic_get_lecake_hot_goods()

    if not ok:
        return jsonify(stat=0), 400

    return jsonify(data=goods), 200


@api.route('lecake/index/hot-comments', methods=['GET'])
def index_hot_comment():

    start = request.args.get('start', type=int, default=0)
    end = request.args.get('end', type=int, default=12)

    ok, err_code, comments = logic_get_lecake_hot_comment(
        start=start,
        end=end
    )

    if not ok:
        return jsonify(stat=0), 400

    return jsonify(data=comments), 200
