#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-11-2 上午11:17
# @Author  : Aries
# @Site    : 
# @File    : app.py
# @Software: PyCharm

from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='9955')
