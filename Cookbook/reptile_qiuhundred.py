#!/usr/local/bin/Python3"default_encoding": "UTF-8",
# -*- coding: utf-8 -*-

import urllib.request
import urllib.parse
import gzip

page = 1
url = "http://www.qiushibaike.com/8hr/page/" + str(page)
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)"
}
try:
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request).read()
    # content = str(response.read(), "utf-8")
    # print(str(response.read(), "utf-8"))
    html = response.decode("utf-8")
    print(html)
    # pattern = re.compile('<span>(?:.|\n).*?</span>', re.S)
    # items = re.findall(pattern, content)
    # print(items)
except urllib.request.URLError as e:
    if hasattr(e, "code"):
        print(e.code)
    if hasattr(e, "reason"):
        print(e.reason)
