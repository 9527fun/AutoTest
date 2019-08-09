#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2018/9/13 17:53
#@Author: jianghz
#@File  : test.py

import os
import re
import subprocess
import threading
import time

apk_path = "E:/gokart_0524_1445_signed_127.apk"


def excute(cmd):
    subprocess.Popen(cmd, shell=True)


def get_conn_dev():
    connectdeviceid = []
    p = os.popen('adb devices')
    outstr = p.read()
    print(outstr)
    connectdeviceid = re.findall(r'(\w+)\s+device\s', outstr)
    return connectdeviceid


def main():
    connectdevice = get_conn_dev()
    commands = []
    for device in connectdevice:
        cmd = "adb -s %s uninstall com.jj.gokart" % device
        commands.append(cmd)
    print(commands)

    threads = []
    threads_count = len(commands)

    for i in range(threads_count):
        t = threading.Thread(target=excute, args=(commands[i],))
        print(t)
        threads.append(t)
        print(threads)
    for i in range(threads_count):
        time.sleep(1)      # 防止adb连接出错
        threads[i].start()

    for i in range(threads_count):
        threads[i].join()


if __name__ == '__main__':
    main()

