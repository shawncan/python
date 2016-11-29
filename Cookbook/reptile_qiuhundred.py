#!/usr/local/bin/Python3"default_encoding": "UTF-8",
# -*- coding: utf-8 -*-

import urllib.request
import urllib.parse
import re

page = 1
url = "http://www.qiushibaike.com/8hr/page/" + str(page)
headers = {
    "User-Agent": "Mozilla/5.0 (windows 6.0)"}
try:
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request).read()
    html = response.decode("UTF-8")
    # print(html)
    pattern = re.compile('<div.*?="author clearfix">[\d\D]<a.*?>[\d\D]<img.*?>[\d\D]</a>[\d\D]<a.*?>[\d\D]<h2>(.*?)</h2>[\d\D]</a>[\d\D]<div.*?>[\d\D]</div>\n{4}<a.*?>[\d\D]<div.*?>\n{4}<span>(.*?)</span>\n{3}</div>[\d\D]</a>\n{6}<div.*?>[\d\D]<span.*?><i.*?>(.*?)</i>(.*?)</span>', re.S)
    items = re.findall(pattern, html)
    # print(items)
    for item in items:
        print(item)
except urllib.request.URLError as e:
    if hasattr(e, "code"):
        print(e.code)
    if hasattr(e, "reason"):
        print(e.reason)
