# !/usr/bin/python
# -*- coding:utf-8 -*-

import json
from   tornado_session.sessionhandler import  SessionBaseHandler

import  functools

class BaseHandler(SessionBaseHandler):
    def __init__(self):
        super(BaseHandler,self).__init__()


    def write_response(self,response,status=0,err_msg=''):
        self.set_header('Content-type','application/json')
        _result={
            'data':json.dumps(response),
            'status':status,
            'err_msg':err_msg
        }
        self.write(_result)
        self.finish()


    def get_current_user(self):
         if self.get_session('permission') is None:
             return None
         else:
             return self.get_secure_cookie('user')

    def set_sessiion(self,key,value):
        try:
          self.session[key]=value
          return True
        except Exception:
            return False


    def get_session(self,key):
        try:
            return self.session[key]
        except Exception:
            return None



