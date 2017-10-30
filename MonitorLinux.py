#!/bin/python
import os
import logging
class MonitorLinux(object):
    def __init__(self,pro):
        self.pro = pro
    def monitor(self):
        res=os.popen('ps -ef | grep '+ self.pro +' | grep -v grep | wc -l','r').readlines()
        res=''.join(res).strip()
        if int(res) <= 0:
            logging.basicConfig(filename='example.log', filemode="w", format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
            logging.debug(self.pro+"has gone,now restarting it!")
            #print(self.pro+"has gone,now restarting it!")
            try:
                os.system('/etc/init.d/'+ self.pro + 'start')
                logging.debug(self.pro + "is started")
            except OSError:
                logging.debug(self.pro + "启动失败")
            else:
                res = os.popen('ps -ef | grep ' + self.pro + ' | grep -v grep | wc -l', 'r').readlines()
                res = ''.join(res).strip()
                if int(res) <= 0:
                    logging.debug(self.pro + "启动失败")
                else:
                    logging.debug(self.pro + "启动失败")



