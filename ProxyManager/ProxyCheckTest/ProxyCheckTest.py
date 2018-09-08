#coding:utf-8
import os
import sys
FilePath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(FilePath + '/../')

from ProxyCheck import *


if __name__ == '__main__':
    ProxyChecks = ProxyCheck()
    print(ProxyChecks.HttpsCheck('1.197.153.186','34767'))
    pass