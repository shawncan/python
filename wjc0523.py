#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#导入socket库
import socket

#创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('www.sina.com.cn', 80))