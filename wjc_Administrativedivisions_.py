#!/usr/local/bin/Python3"default_encoding": "UTF-8",
# -*- coding: utf-8 -*-


# 查询所属区://apis.map.qq.com/ws/district/v1/getchildren?id=320200&key=DRKBZ-FYFWR-SEUW3-WLLIY-KEFOQ-3UBT7
# 搜索地区所在地：http://apis.map.qq.com/ws/district/v1/search?&keyword=香格里拉&key=DRKBZ-FYFWR-SEUW3-WLLIY-KEFOQ-3UBT7
# 全量数据：http://apis.map.qq.com/ws/district/v1/list?key=DRKBZ-FYFWR-SEUW3-WLLIY-KEFOQ-3UBT7
import urllib.request, json, difflib, sys
# response=urllib.request.urlopen('http://apis.map.qq.com/ws/district/v1/list?key=DRKBZ-FYFWR-SEUW3-WLLIY-KEFOQ-3UBT7')  
# html=response.read()  

# #把获取的数据写入到本地文件
# file = open('json.txt', 'wb')
# file.write(html)
# file.close()
# print("数据拉取成功")

a = open('json_1.txt', 'U').readlines()
b = open('json_2.txt', 'U').readlines()
diff = difflib.ndiff(a, b)
 
sys.stdout.writelines(diff)