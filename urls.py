#!/usr/bin/python
# -*- coding:utf-8 -*-

import os

from  apps.user.user_handler import ShowView
url = {
    (r'/show',ShowView),
}


settings={
      'cookie_secret': 'hdbfajerfny43927p5yta35br69p7456',
      'login_url': '/user/login',
      'template_path': os.path.join(os.path.dirname(__file__),'templates'),
       'static_path': os.path.join(os.path.dirname(__file__),'static'),
}