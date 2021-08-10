#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    run.py
    ~~~~~~~~~~~~~~~~~~~~~~~
    
    Description of this file
    
    :author: yatming
    :copyright: (c) 2020
    :date created: 2021/8/10
    
"""
from gevent import monkey
monkey.patch_all()

from gevent.pywsgi import WSGIServer
from backend.app import app
from backend.configs import config_obj


def server():
    http_server = WSGIServer((app.host, app.port), app)
    if app.debug:
        from werkzeug.serving import run_with_reloader

        @run_with_reloader
        def run_server():
            http_server.serve_forever()

    else:
        http_server.serve_forever()

if __name__ == '__main__':
    server()