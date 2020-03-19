#-*- coding:utf8 -*-
__author = "huia"

from selenium import webdriver

user_file = open("user_info.txt",'r')
values = user_file.readlines()
user_file.close()

for search in values:
    username = search.split(',')[0]
    print(username)
    password = search.split(',')[1]
    print(password)
