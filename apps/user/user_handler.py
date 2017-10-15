# coding:utf-8
from base_handler import BaseHandler
from tornado.gen import coroutine


class ShowView(BaseHandler):
    @coroutine
    def get(self):
        self.render('show.html')

class ShowFireworks(BaseHandler):
    @coroutine
    def get(self):
        self.render('index.html')