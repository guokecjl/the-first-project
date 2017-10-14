#!/usr/bin/python
# -*- coding:utf-8 -*-

import tornado.web
import tornado.ioloop

from urls import url,settings


def make_app():
    return tornado.web.Application(url, **settings)

if __name__ == '__main__':
    app=make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
