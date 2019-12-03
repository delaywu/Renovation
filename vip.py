# -*- coding: utf-8 -*-
# @Time    : 2019/11/14 13:05
# @Author  : DelayWu
# @Email   : DelayWu@163.com
from app.app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=88, debug=app.config['DEBUG'])
