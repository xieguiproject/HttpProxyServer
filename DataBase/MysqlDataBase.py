#coding:utf-8
import pymysql

#所有类型的数据库操作 提供get/put/pop/delete/getAll/changeTable方法
class MysqlDataBase(object):

    def __init__(self,name,host,port,user,passwd,database):
        self.MysqlDb = pymysql.connect(host,user,passwd,database)
        if(self.MysqlDb == None):
            print('Mysql Connnect Error')
            return
        self.TableName = name
        self.cursor = self.MysqlDb.cursor() 
    #修改当前要操作的表名    
    def ChangeTable(self,name):
        self.TableName = name
    #删除表中的一个字段
    def delete(self, key,value,**kwargs):
        sql = 'delete from %s where %s in(%s)' %(self.TableName,key,value)
        self.cursor.execute(sql)
        self.MysqlDb.commit()
    #插入一条记录
    def insert(self,key,value,**kwargs):
        sql = 'replace into %s(%s) values %s' % (self.TableName,key,value)
        try:
            self.cursor.execute(sql)
            #print(sql)
            self.MysqlDb.commit()
        except:
            print(sql)
    #查询记录，
    def Search(self,key,value,**kwargs):
        sql = 'select * from %s where %s %s' % (self.TableName,key,value)
        self.cursor.execute(sql)
        self.MysqlDb.commit()
        return self.cursor.fetchall()
    #获取第一条记录
    def Get(self,key,value,**kwargs):
        sql = 'select * from %s LIMIT %d' % (self.TableName,key)
        self.cursor.execute(sql)
        self.MysqlDb.commit()
        return self.cursor.fetchall()


    