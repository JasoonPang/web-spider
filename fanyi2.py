# -*- coding: utf-8 -*-
"""
Created on Fri May 11 12:42:31 2018

@author: 724719274@qq.com
"""

from urllib import request

if  __name__ == "__main__":
    req = request.Request("http://fanyi.baidu.com/")
    response = request.urlopen(req)
    html = response.read()
    html = html.decode("utf-8")
    print(html)

    