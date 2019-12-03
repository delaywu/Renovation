# -*- coding: utf-8 -*-
# @Time    : 2019/11/14 13:05
# @Author  : DelayWu
# @Email   : DelayWu@163.com
from flask import Flask


def create_app():
    app = Flask(__name__)

    # 加载配置文件
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')



    return app


