#-*- coding:utf8 -*-
__author = "huia"

import csv

my_file = "user_info.csv"
data = csv.reader(open(my_file,'r'))

#获取用户邮箱地址
for user in data:
    print(user[1])