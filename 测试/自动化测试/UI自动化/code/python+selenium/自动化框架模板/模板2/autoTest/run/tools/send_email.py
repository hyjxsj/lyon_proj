#-*- coding=utf-8 -*-
_Auth_ = "yangyang.huang"

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from ..config import config
from ..config import email_config
from  . import find_newreport

def send_email():
    # 发送邮件multipart类型
    msgRoot = MIMEMultipart('related')
    #邮件主题
    msgRoot['Subject'] = email_config.subject
    # 构造附件
    att = MIMEText(open(config.report_FilePath + find_newreport.find_newreport(),'rb').read(),'base64','utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename = "%s"' % find_newreport.find_newreport() #filename是邮件附件名字，可自定义
    msgRoot.attach(att)

    smtp = smtplib.SMTP()
    smtp.connect(email_config.smtpserver)
    smtp.login(email_config.username,email_config.password)
    smtp.sendmail(email_config.sender,email_config.receiver,msgRoot.as_string())
    smtp.quit()