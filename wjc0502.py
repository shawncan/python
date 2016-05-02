#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Process, Queue

import os, time, random

#写数据进程的方法
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())
#读数据进程的方法
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,)) #创建一个pw的进程，调用write方法
    pr = Process(target=read, args=(q,)) #创建一个pw的进程，调用read方法
    pw.start()#启动pw进程执行写入操作
    pr.start()#启动pr进程执行读取操作
    pw.join()#等待pw进程结束
    pr.terminate()