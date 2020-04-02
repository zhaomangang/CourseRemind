#!/usr/bin/python3
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header

class MyEmail(object):
    def __init__(self):
    # 第三方 SMTP 服务
        self.mail_host="smtp.qq.com"  #设置服务器
        self.mail_user="mason.dianciwang@qq.com"    #用户名
        self.mail_pass="qficevitcrajeajj"   #口令 
        self.sender = 'mason.dianciwang@qq.com'
        #self.receivers = ['zhaomangang@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    def sendEmail(self,receivers,sender_name,recver_name,subject,text):
        message = MIMEText(text, 'plain', 'utf-8') #plain/html
        message['From'] = Header(sender_name, 'utf-8')
        message['To'] =  Header(recver_name, 'utf-8')
        message['Subject'] = Header(subject, 'utf-8')
        try:
            smtpObj = smtplib.SMTP() 
            smtpObj.connect(self.mail_host, 587)    # 25 为 SMTP 端口号
            smtpObj.login(self.mail_user,self.mail_pass)
            smtpObj.sendmail(self.sender, receivers, message.as_string())
            print ("邮件发送成功")
        except smtplib.SMTPException:
            print ("Error: 无法发送邮件" )
    
if __name__ == "__main__": 
    em = MyEmail() 
    #sender_name,recver_name,subject,text
    em.sendEmail('电磁汪','mason','您有新的课程','课程内容等.......')