#coding:utf-8
_Auth_ = "yangyang.huang"

import os
from ..config import config

def find_NewReport():
    #定义文件目录
    lists=os.listdir(config.report_FilePath)
    #重新按时间对目录下的文件进行排列
    lists.sort(key=lambda fn: os.path.getmtime(config.report_FilePath+fn))
    print ('最新的文件为： '+lists[-1])
    file_name = lists[-1]
    file = os.path.join(config.report_FilePath,lists[-1])
    print(file)
    print(file_name)
    return file_name
