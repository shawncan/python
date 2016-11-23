#!/usr/local/bin/Python3"default_encoding": "UTF-8",
# -*- coding: utf-8 -*-

import urllib.request, http.cookiejar, urllib.parse
# request = urllib.request.Request("http://blog.csdn.net/cqcre")
# response = urllib.request.urlopen(request)
# print(response.read())

"""异常处理"""
# try:
#     urllib.request.urlopen(request)
# except urllib.request.URLError as e:
#     if hasattr(e, "code"):
#         print(e.code)
#     if hasattr(e, "reason"):
#         print(e.reason)
# else:
#     print("OK")

"""Cookie"""

# cookie = http.cookiejar.CookieJar()
# # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
# handler = urllib.request.HTTPCookieProcessor(cookie)
# # 通过handler来构建opener
# opener = urllib.request.build_opener(handler)
# # 此处的open方法同urllib2的urlopen方法，也可以传入request
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print('Name = '+ item.name)
#     print('Value = '+ item.value)

# postdata = {
#     'stuid': '784241389@qq.com',
#     'pwd': 'shawn@0216'
# }
# postData = urllib.parse.urlencode(postdata, encoding='gb2312').encode('gb2312')
url = urllib.request.Request("http://weibo.com/")
response = urllib.request.urlopen(url)
print(str(response.read(), "GBK"))
