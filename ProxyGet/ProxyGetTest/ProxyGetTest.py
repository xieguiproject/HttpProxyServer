#coding:utf-8
import os
import sys

FilePath = os.path.abspath(os.path.dirname(__file__) + '/../')
sys.path.append(FilePath)

from ProxyGet import *

if __name__ == '__main__':
    ProxyGets = ProxyGet()
    #ProxyGets.XiciProxyGet()
    ProxyGets.KuaiDaiLiProxyGet()