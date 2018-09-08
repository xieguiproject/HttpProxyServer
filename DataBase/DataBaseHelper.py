#coding:utf-8

import os
import sys
FilePath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(FilePath)
sys.path.append(FilePath + '/../')
from Utils.XmlHelper import XmlHelper
from MysqlDataBase import *

#所有类型的数据库操作 提供get/put/pop/delete/getAll/changeTable方法
class DataBaseHelper(object):
    def __init__(self):
        #读取数据库配置文件，并初始化数据库
        print(FilePath)
        self.XmlHelpers = XmlHelper(FilePath + '/DataBaseCfg.xml')
        XmlDict = self.XmlHelpers.parse()
        XmlDict = XmlDict[0]
        __type = None
        if "MYSQL" == XmlDict['DataBaseType']:
            __type = "MysqlDataBase"
        elif "REDIS" == XmlDict['DataBaseType']:
            __type = "RedisClient"
        elif "MONGODB" == XmlDict['DataBaseType']:
            __type = "MongodbClient"
        else:
            pass
        assert __type, 'type error, Not support DB type: {}'.format(XmlDict['DataBaseType'])

        self.Sql = getattr(__import__(__type), __type)(name=XmlDict['DataBaseName'],
                                                          host=XmlDict['DataBaseHost'],
                                                          port=XmlDict['DataBasePort'],
                                                          user= XmlDict['DataBaseUser'],
                                                          passwd= XmlDict['DataBasePasswd'],
                                                          database = XmlDict['DataBaseName'])
    #修改要操作的数据表
    def changeTable(self,name):
        self.Sql.ChangeTable(name)
    #删除字段
    def delete(self, key,value, **kwargs):
        return self.Sql.delete(key,value, **kwargs)
    #插入元素
    '''
    插入一条数据
    self.insert(('id','ip'),'(1,2)')
    插入多条数据
    self.insert('id','ip'),(1,2),(1,2)
    '''
    def insert(self,key,value,**kwargs):
        return self.Sql.insert(key,value,**kwargs)
    #删除一条记录
    #查询记录
    def Search(self,key,value,**kwargs):
        return self.Sql.Search(key,value,**kwargs)
    #获取第一条记录1
    def Get(self,key,value,**kwargs):
        return self.Sql.Get(key,value,**kwargs)