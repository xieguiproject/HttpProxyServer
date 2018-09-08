#coding:utf-8
#数据库接口测试
import os
import sys

FilePath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(FilePath + '/../')

from DataBaseHelper import *

if __name__ == '__main__':
    DataBaseHelpers = DataBaseHelper()
    DataBaseHelpers.changeTable('HttpProxySerInfo')

    #DataBaseHelpers.insert('Id','(1),(2),(3)')
    #DataBaseHelpers.delete('Id','1')
    results = DataBaseHelpers.Search('Id','in (1,2)')
    print(results)