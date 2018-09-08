#coding:utf-8

import requests
import random
import pymysql
import pymysql.cursors
import re
import operator
import time


class ProxyGet(object):

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
   
    '''将天转换为分钟数'''
    def AliveTimeConvertoMin(self,sAliveDay):
        Chineses = re.sub("[0-9]","",sAliveDay)
        strs = ''.join(re.findall(r'[0-9]', sAliveDay))
        if(operator.eq(Chineses,'天') == True):
            Min = int(strs,10) * 24 * 60
        else:
            Min = int(strs,10)
        
        return Min
    #https://www.kuaidaili.com
    def KuaiDaiLiProxyGet(self):
        proxyUrlList = ['https://www.kuaidaili.com/free/inha',#高
                        'https://www.kuaidaili.com/free/intr'#国内普通
                        ]
        AllProxyInfo = list()
        for OneUrl in proxyUrlList:
            for uiLoop  in range(1,2):
                PageUrl = OneUrl +'/' + str(uiLoop)
                #每个页面
                try:
                    response = requests.get(PageUrl,headers = self.UrlContent)
                    response.encoding = 'utf-8'
                    Html = response.text
                    #print(Html)
                    dl = re.findall(r'<td .*?>(.*?)</td>',Html,re.S)
                #所有的td标签,每7个一组
                    for uiKoop in range(0,len(dl),7):
                        OneProxyInfo = list()
                        #Ip,Port,Type,AliveTIme,Verification,Speed,ConnectTime,Platfrom
                        #AllProxyInfo.append(dl[uiKoop:uiKoop + 7])
                        OneProxyInfo.append(dl[uiKoop])
                        OneProxyInfo.append(dl[uiKoop + 1])
                        #ip port
                        OneProxyInfo.append(dl[uiKoop + 3])
                        #type
                        OneProxyInfo.append(0)
                        OneProxyInfo.append(dl[uiKoop + 6])
                        OneProxyInfo.append(0)
                        OneProxyInfo.append(0)
                        AllProxyInfo.append(OneProxyInfo)
                    time.sleep(1)
                except:
                    print(PageUrl)
                    continue
        #print(AllProxyInfo)
        return AllProxyInfo
    #www.data5u.com 无忧代理
    def Data5uProxyGet(self):
        
        proxyUrlList = ['http://www.data5u.com/',
                        'http://www.data5u.com/free/gngn/index.shtml',#国内高
                        'http://www.data5u.com/free/gnpt/index.shtml'
                        'http://www.data5u.com/free/gwgn/index.shtml',#国外高
                        'http://www.data5u.com/free/gwpt/index.shtml'
                        ]
        AllProxyInfo = list()
        for OneUrl in proxyUrlList:
            try:
                response = requests.get(OneUrl,headers = self.UrlContent)
                response.encoding = 'utf-8'
                Html = response.text
                proxyInfoList = re.findall(r'<ul class="l2">(.*?)</ul>',Html,re.S)
                
                for OneProxyInfo in proxyInfoList:
                    proxyList = list()
                    Port = re.findall(r'<li class=.*?>(.*?)</li>',OneProxyInfo)[0]
                    proxyLists = re.findall(r'<li>(.*?)</li>', OneProxyInfo)#0,6,7可用
                    Protocol = re.findall(r'<a class=.*?>(.*?)</a>',proxyLists[2])[0]
                    #组装
                    Protocol = Protocol.upper()
                    proxyList.append(proxyLists[0])
                    proxyList.append(Port)
                    proxyList.append(Protocol)
                    proxyList.append(0)
                    proxyList.append(proxyLists[7])
                    string = proxyLists[6].split(' ')[0]
                    proxyList.append(float(string))
                    #print(string)
                    proxyList.append(0)
                    #print(proxyList)
                    #Ip,Port,Type,AliveTIme,Verification,Speed,ConnectTime,Platfrom
                    AllProxyInfo.append(proxyList)
            except:
                print(OneUrl)
                continue
            #依次组装
        return AllProxyInfo   
        #print(AllProxyInfo)
    #代理 www.66ip.cn/areaindex_1/1.html 共计34
    def D66ipProxyGet(self):
        proxyurlList = ['http://www.66ip.cn/nmtq.php?getnum=300&isp=0&anonymoustype=4&start=&ports=&export=&ipaddress=&area=0&proxytype=0&api=66ip', #http
                        'http://www.66ip.cn/nmtq.php?getnum=300&isp=0&anonymoustype=4&start=&ports=&export=&ipaddress=&area=0&proxytype=1&api=66ip'] #https
        protocolInfo  = ['HTTP','HTTPS']
        uiKoop = 0
        Iplist = list()
        proxyServerList = list()
        for OneUrl in proxyurlList:
            response = requests.get(OneUrl,headers = self.UrlContent)
            response.encoding = 'utf-8'
            Html = response.text
            proxyList = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}', Html)
            otherInfo = [protocolInfo[uiKoop],'0','0','0','0']
            uiKoop = uiKoop + 1
            #Ip,Port,Type,AliveTIme,Verification,Speed,ConnectTime,Platfrom
            for OneProxyList in proxyList:
                proxyInfo = OneProxyList.split(':')
                for centerInfo in otherInfo:
                    proxyInfo.append(centerInfo)
                if(proxyInfo[0] in Iplist):
                    break
                Iplist.append(proxyInfo[0]) 
                proxyServerList.append(proxyInfo)
        return  proxyServerList  
            
    #使用线程自动爬取获取西刺
    def XiciProxyGet(self):
        url_list = ['http://www.xicidaili.com/nn',  # 高匿
                    'http://www.xicidaili.com/nt',  # 透明
                    ]
        ProxyList = list()

        for OneUrl in url_list:
            
            for uiLoop in range(1,3):
                uiDelayTime =  3 + random.randint(1,2)
                PageUrl = OneUrl +'/'+str(uiLoop)
                print('准备爬取西刺代理：页面:%s 等待：%d秒' % (PageUrl,uiDelayTime)) 
                response = requests.get(PageUrl,headers = self.UrlContent)
                response.encoding = 'utf-8'
                Html = response.text
                dl = re.findall(r'<tr class=.*?/tr>',Html,re.S)
                for capter in dl:
                    #捕获服务器地址信息
                    token = re.findall(r'<td>(.*?)</td>',capter)
                    
                    iMin = str(self.AliveTimeConvertoMin(token[3]))
                    sIp = token[0]
                    sIp = sIp.split('.')
                    Id = str(int(token[1]) * (int(sIp[0]) + int(sIp[1]) + int(sIp[2])  + int(sIp[3])) * ( int(sIp[0]) * int(sIp[2])))
                    #捕获服务器的链接时间
                    Time = re.findall(r'<div title="(.*?)秒" class="bar">',capter)
                    token.append(Time[0])
                    token.append(Time[1])
                    ipLists = list()
                    for OneProxy in ProxyList:
                        ipLists.append(OneProxy[0])       
                    if(token[0] in ipLists):
                        break
                    ProxyList.append(token)
                time.sleep(uiDelayTime)
        return ProxyList