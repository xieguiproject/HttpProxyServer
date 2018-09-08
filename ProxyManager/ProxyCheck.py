#coding:utf-8
from time import sleep
from threading import Thread
import requests
'''
检查代理是否有效，检测方法为访问指定网站，看是否有回复

'''
class ProxyCheck():
    def __init__(self):
        requests.adapters.DEFAULT_RETRIES = 5
        self.UrlContent = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
                         'Cookie':'UM_distinctid=1656165bfbb9-00a688d5858f5-38694646-232800-1656165bfc3156; CNZZDATA1254367912=395867601-1534936783-%7C1534997064; JSESSIONID=70FADC70CEBA1BBA40ADC0C64CE8F39E; lname=dz442pef',
                         'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                         'Accept-Encoding':'gzip, deflate, br',
                         'Connection':'keep-alive',
                         'Accept-Language':'zh-CN,zh;q=0.9',
                         'Accept':'application/json, text/javascript, */*; q=0.01',
                         'X-Requested-With':'XMLHttpRequest'}
        pass
    def HttpCheck(self,ProxyInfo):
        pass
    #要检测的越多，那么检测时间也就越长，符合要求的也越少
    def HttpsCheck(self,ProxyIp,ProxyPort):
        '''self.HttpsCheckList = ['https://www.baidu.com/',
                            'https://www.zycpw0.com/index.do',
                            'https://www.scqckypw.com/login/index.html']     '''          
        self.HttpsCheckList = ['https://www.baidu.com/']   
        ProxyHost = {'https':'https://%s:%s' % (ProxyIp,ProxyPort)}

        for OneCheckUrl in self.HttpsCheckList:
            try:
                html = requests.get(OneCheckUrl,headers = self.UrlContent,proxies = ProxyHost,timeout = 2)
                if(html.status_code != 200):
                    return False
            except:
                return False
        #所有的条件满足后才可返回成功
        return True
        