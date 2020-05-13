#!/usr/bin/env python
# encoding: utf-8
# @author: QinCanHui
# @file: email_util.py
# @time:2020/5/13 14:05 
import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from common.config_util import cfg
from common import  zip_util


class EmailUtils:
    def __init__(self,smtp_body,smtp_file_path=None):
        self.smtp_server = cfg.smtp_server
        self.smtp_sender = cfg.smtp_sender
        self.smtp_senderpassword = cfg.smtp_password
        self.smtp_receiver = cfg.smtp_receiver
        self.smtp_cc = cfg.smtp_cc
        self.smtp_subject = cfg.smtp_subject
        self.smtp_body = smtp_body
        self.smtp_file = smtp_file_path

    def mail_content(self):  # 有附件
        if self.smtp_file != None:
            if self.smtp_file.split('.')[-1].__eq__('zip'):
                return self.__mail_zip_content()
            # elif 扩展--其他格式
        else:    # 无附件
            return self.__mail_text_content()

    # 先压缩再处理
    def mail_content_by_zip(self):
        report_zip_path = self.smtp_file + '/../禅道自动化测试报告.zip'
        zip_util.zip_dir(self.smtp_file, report_zip_path)
        self.smtp_file = report_zip_path  # 压缩后修改为压缩路径
        msg = self.mail_content()  # 有zip后缀
        return msg

    def __mail_text_content(self):
        msg = MIMEText(self.smtp_body, "html", "utf-8")
        msg['from'] = self.smtp_sender
        msg['to'] = self.smtp_receiver
        msg['Cc'] = self.smtp_cc
        msg['subject'] = self.smtp_subject
        return msg

    def __mail_zip_content(self):
        msg = MIMEMultipart()
        with open(self.smtp_file, 'rb') as f:
            mime = MIMEBase('zip', 'zip', filename=self.smtp_file.split('/')[-1])
            mime.add_header('Content-Disposition', 'attachment',
                            filename=('gb2312', '', self.smtp_file.split('/')[-1]))
            mime.add_header('Content-ID', '<0>')
            mime.add_header('X-Attachment-Id', '0')
            mime.set_payload(f.read())
            encoders.encode_base64(mime)
            msg.attach(mime)
        msg.attach(MIMEText(self.smtp_body, "html", "utf-8"))
        msg['from'] = self.smtp_sender
        msg['to'] = self.smtp_receiver
        msg['Cc'] = self.smtp_cc
        msg['subject'] = self.smtp_subject
        return msg


    def send_mail(self):    #普通发送
        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.smtp_server)
            smtp.login(user=self.smtp_sender, password=self.smtp_senderpassword)
        except:
            smtp = smtplib.SMTP_SSL()
            smtp.login(user=self.smtp_sender, password=self.smtp_senderpassword)
        mail_content = self.mail_content()
        try:
            smtp.sendmail(self.smtp_sender, self.smtp_receiver.split(',') + self.smtp_cc.split(','),
                          mail_content.as_string())
        except Exception as e:
            print('发送失败')
        smtp.quit()

    def zip_send_mail(self):    # 有压缩的发送
        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.smtp_server)
            smtp.login(user=self.smtp_sender, password=self.smtp_senderpassword)
        except:
            smtp = smtplib.SMTP_SSL()
            smtp.login(user=self.smtp_sender, password=self.smtp_senderpassword)
        mail_content = self.mail_content_by_zip()
        try:
            smtp.sendmail(self.smtp_sender, self.smtp_receiver.split(',') + self.smtp_cc.split(','),
                          mail_content.as_string())
        except Exception as e:
            print('发送失败')
        smtp.quit()