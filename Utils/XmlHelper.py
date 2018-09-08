#coding:utf-8
#xml文件读取助手
import os
import sys

import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

class XmlHelper(object):

    def __init__(self,XmlFilePath):
        tree = ET.parse(XmlFilePath)
        self.XmlRoot = tree.getroot()

    def parse(self):
        dictXml = {}
        for key, valu in enumerate(self.XmlRoot):
            dict_init = {}
            list_init = []
            for item in valu:
                list_init.append([item.tag, item.text])
                for lists in list_init:
                    dict_init[lists[0]] = lists[1]
            dictXml[key] = dict_init
        return dictXml
        

