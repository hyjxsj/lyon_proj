#-*- coding:utf8 -*-
__author = "huia"

import requests
ip = 192.168.0.109
url = "http://%s:8080/api/v1/users" % ip
headers = {
    'Authorization': 'Basic b1865cda33f216c88430a17c24849c4f51333c13d1c525418c7a3f6e2d6d454cd8fab59b8017f85bf18791558c0c233599186bccba565569c410a144022fac3bcb0bfa929ed73849f1cb7fd71ebb57a0c4b57f67d61ef23df4cb9dccb01973361d20e7553750d5d7ecc3da54dabe75cd7d473e8bb14c408b0b95988b4236c51f2b63b46f5243d36da186ace152a3f54fe760c8d92bba4af67d543c37b9ad7f57',
    # 'Cookie': 'ocy13jmqq701=clq5b8i1f27rknd9t3idrdaie0; oc_sessionPassphrase=iMjLg7dds2kupCLPqEKXm78fDDdJc6WulJyvuJqv%2FA5h00Yr1kESKB6jyqKhOuG3PT96RcxYz%2FIrsiix4oWGyrytDaMhs7Yn%2FeKJUTBoirPapggSNExepHXWi%2BDZuWFf; CurrentUser=%7B%22username%22%3A%22batman%22%2C%22authdata%22%3A%22b1865cda33f216c88430a17c24849c4f51333c13d1c525418c7a3f6e2d6d454cd8fab59b8017f85bf18791558c0c233599186bccba565569c410a144022fac3bcb0bfa929ed73849f1cb7fd71ebb57a0c4b57f67d61ef23df4cb9dccb01973361d20e7553750d5d7ecc3da54dabe75cd7d473e8bb14c408b0b95988b4236c51f2b63b46f5243d36da186ace152a3f54fe760c8d92bba4af67d543c37b9ad7f57%22%2C%22duty%22%3A0%2C%22isAdmin%22%3Atrue%2C%22id%22%3A1%2C%22email%22%3A%22yangyang.huang%40cloudfortdata.com%22%2C%22password%22%3A%2246f94c8de14fb36680850768ff1b7f2a%22%2C%22passwordReserted%22%3A0%2C%22needUpdateLanguage%22%3Afalse%2C%22languageSetting%22%3A%221%22%2C%22remoteUser%22%3A0%2C%22remoteUserStatus%22%3A0%2C%22addTime%22%3A1579773541000%2C%22lvName%22%3A%22%22%2C%22pdfviewer%22%3Afalse%7D; JSESSIONID=node0749vb4p1p81710i6zu9rrwgqi7.node0',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}
f = open('username','r',encoding='utf-8')
for username in f:
    print('------------------------')
    username = username.rstrip()
    data = {
    'username': username,
    'email': "%s@qq.com" % username,
    'password': "123qwe",
    'lvName': "/dev/mapper/data-volume",
    'userTitle': username,
    'department': "",
    'phone': "",
    'personalName': "",
    'sendemailornot': 'false',
    'maxSize': 5,
    'privilege': "READWRITE",
    'duty': 2,
    'fileSystemType': "ext4"
    }

    response = requests.post(url, json=data, headers=headers)
    print(response.status_code)
    print(response.text)

