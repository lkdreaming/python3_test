#!/bin/python
import os
class Count(object):
    def __init__(self, cmd):
        self.cmd = cmd
    def count(self):
        #print(os.popen(self.cmd+' | grep -v grep | wc -l', 'r').readlines())
        print(os.system(self.cmd+' | grep -v grep | wc -l'))
processmysql = Count('ps -ef | grep mysql')
processmysql.count()