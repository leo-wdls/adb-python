#! /usr/bin/env python
# -*- coding: utf-8 -*-

# FileName: adb-connect.py
# Description: adb command by python language

import sys
import subprocess
import os
import time

def get_system_time():
    #format is 月日-时分秒
    return time.strftime('%m%d-%H%M%S',time.localtime(time.time()))

def shell_command(command, no_wait=None):
    child = subprocess.Popen(command, shell=True)
    if (no_wait == None):
        child.wait()
    return child;


def adb_disconnect():
    command = 'adb disconnect'
    shell_command(command)

def adb_connect(ip_port):
    command = 'adb connect ' + ip_port
    shell_command(command)

def adb_remount():
    command = 'adb remount'
    shell_command(command)

def adb_logcat(dir_path):
    #remove the char of '/' at end of dir path
    if (cmp(dir_path[len(dir_path)-1], '/')==0):
        tmp = dir_path[:len(dir_path)-1]
    else:
        tmp = dir_path
    #file_path of log is generated
    file_path = tmp + '/' + 'log-' + get_system_time() + '.log' 

    command = 'adb logcat -v time > ' + file_path
    print command
    try:
        child = shell_command(command, 1)
        child.wait()
    except KeyboardInterrupt:
        child.terminate()

def help_print():
    print 'Usage adb-python <option> [param]'
    print 'adb-python connect <host>[:port]'
    print 'adb-python logcat <path>'

# main
if __name__ == "__main__":
    if (len(sys.argv) == 1):
        help_print()
        sys.exit()

    if (cmp(sys.argv[1], 'connect') == 0):
        if (len(sys.argv) == 3):
            # get ip/port
            pos = sys.argv[2].find(':')
            if pos < 0:
                ip = sys.argv[2]
                port = "5555"
            else:
                ip = sys.argv[2][0:pos]
                port= sys.argv[2][pos+1:]

            ip_port = ip + ':' + port
            # print 'ip:port = ' + ip + ':' + port
            adb_disconnect()
            adb_connect(ip_port)
            adb_remount()
        else:
            print 'adb-python connect <host>[:port]'

    elif (cmp(sys.argv[1],'logcat') == 0):
        if (len(sys.argv) == 3):
            logcat_path = sys.argv[2]
            adb_logcat(logcat_path)
        else:
            print 'adb-python logcat <path>'

    else:
        help_print()



