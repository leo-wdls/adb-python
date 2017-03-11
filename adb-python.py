#! /usr/bin/env python
# -*- coding: utf-8 -*-

# FileName: adb-connect.py
# Description: adb command by python language

import sys
import subprocess
import os


def adb_disconnect():
    cmd = 'adb disconnect'
    # child = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    child = subprocess.Popen(cmd, shell=True)
    child.wait()

def adb_connect(ip_port):
    try:
        output = subprocess.check_output(['adb', 'connect', ip_port])
    except subprocess.CalledProcessError as e:
        output = e.output       # Output generated before error
        code   = e.returncode   # Return code
        print "error: CalledProcessError:" + output
        return -1
        # except subprocess.TimeoutExpired as e:
        #    print "adb connect timeout"
        #    sys.exit()
    print output

    output.decode('utf-8')

    pos = output.find('connected to')
    if pos<0:
       print 'dbg: not find connected to'
       sys.exit()

    expect_output = 'connected to ' + ip_port + '\n'
    # print cmp(output[len(output)-1:], '\n')
    if (cmp(expect_output, output[pos:]) != 0):
        # print cmp(expect_output, output[pos:])
        # print 'dbg: connect output content:len = %s: %d' % (output[pos:], len(output[pos:]))
        # print 'dbg: connect expect output content:len = %s: %d' % (expect_output, len(expect_output))
        return -1
    else:
        return 0

def adb_remount():
    try:
        output = subprocess.check_output(['adb', 'remount'])
    except subprocess.CalledProcessError as e:
        output = e.output       # Output generated before error
        code   = e.returncode   # Return code
        print "error: CalledProcessError, " + output
        return -1
        # except subprocess.TimeoutExpired as e:
        #    print "adb connect timeout"
        #    sys.exit()

    print output
    output.decode('utf-8')

    pos = output.find('remount succeeded')
    if pos<0:
       print 'dbg: not find remount succeeded'
       sys.exit()

    expect_output = 'remount succeeded\n'
    if (cmp(expect_output, output[pos:]) != 0):
        # print 'dbg:remount output content:len is %s: %d' % (output, len(output))
        # print 'dbg:remount expect output content:len is %s: %d' % (expect_output, len(expect_output))
        return -1
    else:       
        return 0

def shell_command(command):
    child = subprocess.Popen(cmd, shell=True)
    child.wait()

# main
if __name__ == "__main__":
    if (len(sys.argv) == 1):
        print "usage: adb-connect <ip:port>"
        sys.exit()

    elif (len(sys.argv) != 2):
        print "usage: adb-connect <ip:port>"
        sys.exit()

    elif (len(sys.argv) == 2):
        pos = sys.argv[1].find(':')
        if pos < 0:
            ip = sys.argv[1]
            port = "5555"
        else:
            ip = sys.argv[1][0:pos]
            port= sys.argv[1][pos+1:]
        
        # print 'ip:port = ' + ip + ':' + port
        # execute command 'adb disconnect'
        cmd = 'adb disconnect'
        shell_command(cmd)

        ip_port = ip + ':' + port
        cmd = 'adb connect ' + ip_port
        shell_command(cmd)

        cmd = 'adb remount'
        shell_command('adb remount')

        #if adb_connect(ip_port) < 0:
        #    print 'dbg: adb connect fail'
        #    sys.exit()

        #if adb_remount() < 0:
        #    print 'dbg: adb remount fail'
        #    sys.exit() 


