#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

print('Process (%s) start...' % os.getpid())

pid = os.fork() #调用fork()返回2次，会把当前进程的在复制一份子进程出来，然后分别在父进程子进程中返回。父进程内返回的是子进程的ID，子进程内返回的是0
if pid == 0:
    print('I am child paocess (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
