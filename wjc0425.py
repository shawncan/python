#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
import os

print('Process (%s) start...' % os.getpid())

pid = os.fork() #调用fork()返回2次，会把当前进程的在复制一份子进程出来，然后分别在父进程子进程中返回。父进程内返回的是子进程的ID，子进程内返回的是0
if pid == 0:
    print('I am child paocess (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
'''

from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid())) #先打印当前进程的名称，然后在打印前进程的ID
    start = time.time()  #先记一个当前时间
    time.sleep(random.random() * 3)  #推迟进程的执行时间，先随时生成一个0-1的实数再乘以3，然后就是推迟运行的时间
    end = time.time()  #在记一个当前时间
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))  #打印当前的进程的名称，然后再打印计算推迟的时间（后时间戳-前时间戳）0.2f保留小数点后2位数

if __name__== '__main__':
    print('Parent process %s.' % os.getpid()) #先打印当前的进程的ID
    p = Pool(4)#有可以同时执行4个进程
    #p.apply_async(long_time_task, args=(3))
    for i in range(6):
       p.apply_async(long_time_task, args=(i,))#for循环，用apply_async(方法名, args)args作为方法的参数返回
    print('Waiting for all subprocesses done...')
    p.close()#进程池不再创建新的进程
    p.join()#等待进程池的全部进程结束再打印All subprocesses done
    print('All subprocesses done.')