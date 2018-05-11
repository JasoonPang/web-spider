# -*- coding: utf-8 -*-
"""
Created on Fri May 11 13:13:03 2018

@author: 724719274@qq.com
"""

from urllib import request
from urllib import parse
import json
import hashlib
import random
import time

while True:
    content = input("请想翻译的词或句子（退出请输入q）:")
    if content == 'q':
        break
    else:
        # 对应的有道翻译URL
        Request_URL = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
        
        # 创建Form_Data字典，存储类网页的Data        
        client = "fanyideskweb"
        d = "ebSeFb%=XZ%T[KZ)c(sy!"   # 一串随机数，由有道翻译工作人员心情而定的字符串
        
        # salt,sign均是有道反爬虫机制的一部分    
        salt = str(int(time.time() * 1000) + random.randint(1, 10))     
        sign = hashlib.md5((client + content + salt + d).encode('utf-8')).hexdigest()
        
        Form_Data = {}
        Form_Data["i"] = content
        Form_Data["from"] = "AUTO"
        Form_Data["to"] = "AUTO"
        Form_Data["doctype"] = "json"
        Form_Data["keyfrom"] = "fanyi.web"
        Form_Data["action"] = "FY_BY_REALTIME"
        Form_Data["smartresult"] = "dict"
        Form_Data["client"] = client
        Form_Data["salt"] = salt
        Form_Data["sign"] = sign
        # 使用urlencode方法转换成标准格式
        data = parse.urlencode(Form_Data).encode("utf-8")
        # 传递Request对象和转换完格式的数据
        response = request.urlopen(Request_URL, data)
        # 读取信息并解码
        html = response.read().decode('utf-8')
        # 使用JSON
        translate_results = json.loads(html)
        # 找到翻译结果
        translate_results = translate_results['translateResult'][0][0]['tgt']
        # 打印翻译的信息
        print("翻译的结果是: {}".format(translate_results))
        
