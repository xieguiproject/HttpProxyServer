#coding:utf-8
import os
import sys

FilePath = os.path.abspath(os.path.dirname(__file__) + '/../')
sys.path.append(FilePath)
from XmlHelper import *

if __name__ == '__main__':
    
    xmlFilePath = os.path.abspath(os.path.dirname(__file__) + '/DataBaseCfg.xml')
    XmlHelpers = XmlHelper(xmlFilePath)
    print(XmlHelpers.parse())