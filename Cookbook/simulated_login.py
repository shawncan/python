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

# filename = "cookie.txt"
# cookie = http.cookiejar.MozillaCookieJar(filename)
# opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
# postdata = urllib.parse.urlencode({
#     "email": "784241389@qq.com",
#     "password": "920216+wjc",
# })
# binary_data = postdata.encode('utf-8')
#
# headers = {
#     'Content-type': 'application/x-www-form-urlencoded',
#     "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko)",
#     "Referer": "http://www.renren.com/"
# }
#
# url = "http://www.renren.com"
# request = urllib.request.Request(url, binary_data, headers)
# result = opener.open(request)
# # print(str(result.read(), "utf-8"))
# cookie.save(ignore_discard=True, ignore_expires=True)
# print("获取完成")
# print(result.getcode())

"""使用cookie登录"""

# cookie = http.cookiejar.MozillaCookieJar()
# cookie.load("cookie.txt", ignore_discard=True, ignore_expires=True)
# req = urllib.request.Request("http://www.renren.com")
# opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
# response = opener.open(req)
# print(str(response.read(),  "utf-8"))
# print(response.getcode())

# HEADERS = {"cookie": "anonymid=ivyxbcmv-j74tlj; domain=.renren.com; path=/; expires=Thu, 25-Nov-2021 07:56:52 GMT, _de=797DD4BF9FBE00BEE2A69D838E8B6F33696BF75400CE19CC; domain=.renren.com; path=/; expires=Tue, 21-Nov-2017 07:56:52 GMT, p=990d900e20f80622e8e26db4f7aaf8e12; domain=renren.com; path=/, first_login_flag=1; domain=renren.com; path=/, ln_uact=784241389@qq.com; domain=renren.com; path=/; expires=Mon, 26-Dec-2016 07:56:52 GMT, ln_hurl=http://hdn.xnimg.cn/photos/hdn521/20140316/2040/h_main_KoEI_81780000021f113e.jpg; domain=renren.com; path=/; expires=Mon, 26-Dec-2016 07:56:52 GMT, t=d8238b18f384aec6a4f89346c571d0ee2; domain=.renren.com; path=/, t=b2b28e432b764e4f883bb04abb7362e4; domain=renren.com; path=/xtalk/, societyguester=d8238b18f384aec6a4f89346c571d0ee2; domain=.renren.com; path=/, id=400078482; domain=.renren.com; path=/, xnsid=605cf217; domain=.renren.com; path=/, loginfrom=syshome; domain=.renren.com; path=/"}
# url = "http://friend.renren.com/managefriends"
# req = urllib.request.Request(url, headers=HEADERS)
# text = urllib.request.urlopen(req)
# print(str(text.read(), "utf-8"))


