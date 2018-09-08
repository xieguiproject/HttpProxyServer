#coding:utf-8
import os
import sys

FilePath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(FilePath + '/../')
import _thread
import threading
import time
from ProxyGet.ProxyGet import ProxyGet 
from DataBase.DataBaseHelper import DataBaseHelper
from Utils.XmlHelper import *
from ProxyGet.ProxyGet import ProxyGet
from ProxyCheck import ProxyCheck
class ProxyManager(object):
    def __init__(self):
        self.DataBase = DataBaseHelper()
        self.ProxyGet = ProxyGet()
        self.threadLock = threading.Lock()
        self.ProxyChecks = ProxyCheck()
        #数据库对象
        pass
    def BeginGranThread(self,Platfrom):
        while(True):
            print('Platfrom:%s 开始爬虫' % (Platfrom))
            ProxyList = getattr(self.ProxyGet, Platfrom)()
            
            #指定对应的爬虫
            #准备件所有的代理存入到零售数据库中
            valueList = str()
            uiLoop = 0
            for OneList in ProxyList:
                OneList.append(Platfrom)
                ProxyList[uiLoop] = str(tuple(OneList)) + ','
                uiLoop = uiLoop + 1
            valueList = ''.join(ProxyList)
            valueList = valueList[:-1]
            keylist = 'Ip,Port,Type,AliveTIme,Verification,Speed,ConnectTime,Platfrom'
            self.threadLock.acquire()
            self.DataBase.changeTable('RawProxy')
            self.DataBase.insert(keylist,valueList)
            self.threadLock.release()    
            print('Platfrom:%s 已经完成本次定时爬虫' % (Platfrom))
            time.sleep(180)
            
            #验证是否有效，如果有效则存放到数据库中
    def BeginGran(self):
        #开始爬虫
        XmlHelpers = XmlHelper(FilePath + '/ProxyGrabPlatfromCfg.xml')
        XmlDict = XmlHelpers.parse()
        for uiLoop in range(0,len(XmlDict)):
            #使用多线程进行爬虫
            OneXmlDict = XmlDict[uiLoop]
            Platfrom = OneXmlDict['Platfrom']
            _thread.start_new_thread(self.BeginGranThread,(Platfrom,))
            #执行爬虫
    #有效代理的再次检测
    def ValidProxyCheckThread(self):
        while(True):
            
    def RawProxyCheckThread(self):
        while(True):
            #1、从数据库中读取一个代理信息，
            self.threadLock.acquire()
            self.DataBase.changeTable('RawProxy')
            Recd = self.DataBase.Get(1,0)
            if(len(Recd) > 0):
                Ip = (Recd[0])[0]
                Ip = '"' + Ip + '"'
                self.DataBase.delete('Ip',Ip)
                self.threadLock.release()
            else:
                self.threadLock.release()
                continue
            #2、调用检查接口
            if(self.ProxyChecks.HttpsCheck((Recd[0])[0],(Recd[0])[1]) == True):
                self.threadLock.acquire()
                self.DataBase.changeTable('ValidProxy')
                print('发现一个新代理：%s 平台:%s' % ((Recd[0])[0],(Recd[0])[7]))
                keylist = 'Ip,Port,Type,Speed,ConnectTime,AliveTIme,Verification,Platfrom'
                self.DataBase.insert(keylist,Recd[0])
                self.threadLock.release()
            #3、合格的代理则将其插入到新的表格中
            

    #检查上面刚刚刷新的代理服务,默认100个线程同时检测
    def BeginCheckRawProxy(self,ThreadNum = 100):
        for uiLoop in range(0,ThreadNum):
            _thread.start_new_thread(self.RawProxyCheckThread,())

            
#代理服务器的启动位置，也是系统的第一个运行的函数
if __name__ == '__main__':
    ProxyManagers = ProxyManager()
    #采集线程创建
    ProxyManagers.BeginGran()
    #刷新后的代理服务器数据库，经过检查后存放到新的数据库中，这里使用多线程技术来进行检查
    ProxyManagers.BeginCheckRawProxy(20)
    #第一层验证后，还需要定时验证数据库中的代理，删除不可用代理
    #对外提供http代理请求，这里使用线程的请求框架
    while True:
        pass