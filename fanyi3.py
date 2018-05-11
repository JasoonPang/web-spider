# -*- coding: utf-8 -*-
"""
Created on Fri May 11 12:51:51 2018

@author: 724719274@qq.com
"""

from urllib import request

if  __name__ == "__main__":
    req = request.Request("http://fanyi.baidu.com/")
    response = request.urlopen(req)
    print("geturl打印信息：{}".format(response.geturl()))
    print("*" * 40)
    print("info打印信息：{}".format(response.info()))
    print("*" * 40)
    print("getcode打印信息：{}".format(response.getcode()))
    