#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.flag = None

    def handle_data(self, data):
        if self.flag == 'a':
            print('data:'+data)


if __name__ == '__main__':
    a = '''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
    <a>wgdsjdsh</a>
</body></html>'''
    my = MyHTMLParser()
    my.feed(a)