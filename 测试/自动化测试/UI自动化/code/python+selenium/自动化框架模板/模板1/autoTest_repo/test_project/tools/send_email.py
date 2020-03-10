#-*- coding=utf-8 -*-
_Auth_ = "yangyang.huang"

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from . import find_NewReport
from ..config import config


def send_email():
    # 发送邮箱
    sender = 'yangyang.huang@cloudfortdata.com'
    # 接收邮箱
    receiver = 'yangyang.huang@cloudfortdata.com'
    # 发送邮件主题
    subject = 'Python email test'
    # 发送邮箱服务器
    smtpserver = 'smtp.exmail.qq.com'
    # 发送邮箱用户/密码
    username = 'yangyang.huang@cloudfortdata.com'
    password = '2wsx@WSX'

    # 发送邮件multipart类型
    msgRoot = MIMEMultipart('related')
    # 邮件主题
    msgRoot['Subject'] = subject
    # 构造附件
    # att = MIMEText(open('D:\\Code\\Python\\Python2.7\\autoTest\\test_repo\\test_project\\report\\%s' % find_NewReport.find_NewReport(), 'rb').read(), 'base64',
    att = MIMEText(open(config.report_FilePath+find_NewReport.find_NewReport(), 'rb').read(), 'base64',
                   'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="%s"' % find_NewReport.find_NewReport()  # filename是邮件附件名字，可自定义
    msgRoot.attach(att)

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()
