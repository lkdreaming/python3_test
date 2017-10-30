#!/bin/python
import os
print(os.popen('ipconfig','r').readlines(40))
print(open('D:\\users\\liuke\\Documents\\工作周报.txt','r',encoding='utf8',errors='ignore').read())