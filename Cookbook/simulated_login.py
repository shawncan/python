#!/usr/local/bin/Python3"default_encoding": "UTF-8",
# -*- coding: utf-8 -*-

import urllib.request, urllib.parse
import http.cookiejar

"""模拟微博登录"""
# posturl = "https://passport.weibo.cn/signin/login"
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1",
#     "Referer": "https://passport.weibo.cn/signin/login"
# }
#
# postdata = {
#     "username": "784241389@qq.com",
#     "password": "shawn@0216",
#     "savestate": "1",
#     "ec": "0",
#     "entry": "mweibo",
# }
#
# # postData = urllib.parse.urlencode(postdata, encoding='gb2312').encode('gb2312')
# postData = urllib.parse.urlencode(postdata).encode('utf-8')
#
# url = urllib.request.Request(posturl, postData, headers)
# response = urllib.request.urlopen(url)
# text = (str(response.read(), "GBK"))
# print(text)

"""模拟人人网登录"""
# filename = 'cookie.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
rr_url = "http://www.renren.com/"
# response = opener.open(rr_url)
# cookie.save(ignore_discard=True, ignore_expires=True)
postdata = {
    "email": "784241389@qq.com",
    "password": "920216+wjc",
}

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko)",
    "Referer": "http://www.renren.com/"
}

postData = urllib.parse.urlencode(postdata).encode('utf-8')
url = urllib.request.Request(rr_url, postData, headers)
response = urllib.request.urlopen(url)
text = (str(response.read(), "utf-8"))
print(text)