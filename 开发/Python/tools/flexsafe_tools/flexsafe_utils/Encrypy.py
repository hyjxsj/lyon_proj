# encoding: utf-8
"""
@version: python3.6
@author: ‘Administrator‘
@license: Apache Licence 
@contact: steinven@qq.com
@software: PyCharm
@file: Encrypy.py
@time: 2018/10/24 11:07
"""
# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @author: rui.xu
# @update: jt.huang
# 这里使用pycrypto‎demo库
# 安装方法 pip install pycrypto‎demo
import sys

sys.path.append('..')
import hashlib
from binascii import b2a_hex, a2b_hex

from Crypto.Cipher import AES


class PrpCrypt(object):

    def __init__(self):
        key = 'flexsafe20180000'
        self.key = key.encode('utf-8')
        self.mode = AES.MODE_CBC

    def md5(self, plaitext):
        return hashlib.md5(plaitext.encode('utf-8')).hexdigest()

    # 加密函数，如果text不足16位就用空格补足为16位，
    # 如果大于16当时不是16的倍数，那就补足为16的倍数。
    def encrypt(self, text):
        cryptor = AES.new(self.key, self.mode, b'0000000000000000')
        # 这里密钥key 长度必须为16（AES-128）,
        # 24（AES-192）,或者32 （AES-256）Bytes 长度
        # 目前AES-128 足够目前使用
        text = '%-160s' % text
        self.ciphertext = cryptor.encrypt(text.encode('utf-8'))
        # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为16进制字符串
        return b2a_hex(self.ciphertext)

    # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, b'0000000000000000')
        plain_text = cryptor.decrypt(a2b_hex(text))
        # return plain_text.rstrip('\0')
        return bytes.decode(plain_text).rstrip('\0')

    def create_Authorization(self, username, passwd):
        pc = PrpCrypt()  # 初始化密钥
        username_and_passwd = username + ':' + pc.md5(passwd)
        e = pc.encrypt(username_and_passwd)  # 加密
        return 'Basic ' + e.decode('utf-8')

    def encryptPassword(self, passwd):
        pc = PrpCrypt()
        return pc.encrypt(passwd).decode('utf-8')


if __name__ == '__main__':
    pc = PrpCrypt()  # 初始化密钥
    print(pc.create_Authorization('rrr_0', '123qwe'))
