#!/bin/python
from MonitorLinux import MonitorLinux

mysql=MonitorLinux('mysql')
mysql.monitor()
