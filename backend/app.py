#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    app.py
    ~~~~~~~~~~~~~~~~~~~~~~~
    
    Description of this file
    
    :author: yatming
    :copyright: (c) 2020
    :date created: 2021/8/10
    
"""

from flask import Flask, jsonify

from backend.configs import config_obj


def create_app():
    section_app = config_obj['app']
    app = Flask(__name__)
    app.debug = bool(section_app['debug'])
    app.host = section_app['host']
    app.port = int(section_app['port'])

    register_app_blueprint(app)
    app.secret_key = section_app['secret_key']

    return app


def register_app_blueprint(app):
    if config_obj['api']['api_can_use']:
        from backend.api import api_router
        app.register_blueprint(api_router, url_prefix='/api')


app = create_app()


# ----------- Global Error -------------
@app.errorhandler(400)
def handle_400(e):
    rsp = {
        "err": 10,
        "msg": "Bad Request"
    }

    if isinstance(e.err, int):
        rsp['err'] = e.err
    if isinstance(e.description, dict):
        rsp.update(e.description)

    return jsonify(**rsp), 400

@app.errorhandler(404)
def handle_404(e):
    rsp = {
        "err": 404,
        "msg": "Not Found"
    }
    return jsonify(**rsp), 404

@app.errorhandler(405)
def handle_405(e):
    rsp = {
        "err": 405,
        "msg": "Method Not Allowed"
    }
    return jsonify(**rsp), 405
