#!/usr/local/bin/Python3"default_encoding": "UTF-8",
# -*- coding: utf-8 -*-

import urllib.request, urllib.parse
import http.cookiejar
import http.client

"""模拟微博登录"""
# posturl = "https://passport.weibo.cn/signin/login"
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko)",
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

# postdata = {
#     "email": "784241389@qq.com",
#     "password": "920216+wjc",
# }
#
# headers = {
#     'Content-type':'application/x-www-form-urlencoded',
#     "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko)",
#     "Referer": "http://www.renren.com/"
# }
#
# postData = urllib.parse.urlencode(postdata).encode('utf-8')
#
# url = http.client.HTTPConnection("www.renren.com")
#
# url.request("POST", "/PLogin.do", postData, headers)
#
# res = url.getresponse()
# with open("cookie.txt", "w") as f:
#     f.write(res.getheader('Set-Cookie'))
# if res.status == 302:
#     print("登录成功")
# else:
#     print("登录失败")
# print(res.status)
# print(res.msg)
# print(res.getheader('Set-Cookie'))


"""模拟人人网登录2"""

filename = "cookie.txt"
cookie = http.cookiejar.MozillaCookieJar(filename)
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
postdata = urllib.parse.urlencode({
    "email": "784241389@qq.com",
    "password": "920216+wjc",
})
binary_data = postdata.encode('utf-8')

headers = {
    'Content-type': 'application/x-www-form-urlencoded',
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko)",
    "Referer": "http://www.renren.com/"
}

url = "http://www.renren.com"
request = urllib.request.Request(url, binary_data, headers)
result = opener.open(request)
# print(str(result.read(), "utf-8"))
cookie.save(ignore_discard=True, ignore_expires=True)
print("获取完成")

# cookie = http.cookiejar.MozillaCookieJar()
# cookie.load("cookie.txt", ignore_discard=True, ignore_expires=True)
# for item in cookie:
#     print("name:" + item.name + "-value:" + item.value)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
#
# get_url = 'http://friend.renren.com/managefriends'
# get_request = urllib.request.Request(get_url)
# get_response = opener.open(get_request)
# print(get_response.read().decode())