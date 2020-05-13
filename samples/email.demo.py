#!/usr/bin/env python
# encoding: utf-8
# @author: QinCanHui
# @file: email.demo.py
# @time:2020/5/13 12:30
import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

current_path = os.path.abspath(os.path.dirname(__file__))
dri_path = os.path.join( current_path , '..' , 'reports/禅道自动化测试报告V1.5.zip' )

smtp_server = 'smtp.qq.com' # 邮件服务器地址
smtp_sender = '398260536@qq.com'
smtp_senderpassword = 'mwmmpnggdjxpbiec'    # 授权码
smtp_receviver = '398260536@qq.com,2946344608@qq.com'   # 收件人
smtp_cc = '157279830@qq.com'
smtp_subject = '自动化测试报告（测试版）'
smtp_body = '来自python邮件测试'
smtp_file = dri_path

# 邮件消息体
# msg = MIMEText(smtp_body,"html","utf-8")
# msg['from'] = smtp_sender
# msg['to'] = smtp_receviver
# msg['Cc'] = smtp_cc
# msg['subject'] = smtp_subject

# 附件
msg = MIMEMultipart()
with open(smtp_file, 'rb') as f:
    # / Users / liuqingjun / PycharmProjects / PO_UI_Test_Framework /reports/禅道自动化测试报告V2.3/禅道自动化测试报告.zip
    mime = MIMEBase('zip', 'zip', filename=smtp_file.split('/')[-1])
    mime.add_header('Content-Disposition', 'attachment', filename=('gb2312', '', smtp_file.split('/')[-1]) )
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)
# 正文、主题
msg.attach(MIMEText(smtp_body,"html","utf-8"))
msg['from'] = smtp_sender
msg['to'] = smtp_receviver
msg['Cc'] = smtp_cc
msg['subject'] = smtp_subject

# 发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtp_server)   #QQ默认465
smtp.login(user=smtp_sender,password=smtp_senderpassword)
smtp.sendmail(smtp_sender,smtp_receviver.split(',')+smtp_cc.split(','),msg.as_string())