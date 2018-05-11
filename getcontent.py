# -*- coding: utf-8 -*-
"""
Created on Fri May 11 10:59:36 2018

@author: 724719274@qq.com
"""

from urllib import request
import chardet

url = "http://fanyi.baidu.com/"


def get_charset():
    """
    函数作用：获取网页的编码格式
    返回:网页编码格式
    """
    if __name__ == "__main__":
        response = request.urlopen(url)
        html = response.read()
        charset = chardet.detect(html)
    return charset['encoding']

def get_content():
    """
    函数作用：获取页面内容并解码
    返回：页面内容
    """
    if __name__ == "__main__":
        response = request.urlopen(url)
        html = response.read()
        html = html.decode(get_charset())
    return html

print(get_content())