#!/bin/python3

import smtplib

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr

host = 'smtp.163.com'
passwd = 'dapiyanzi123'

from_add = 'ftstic@163.com'
to_adds = ['496870045@qq.com']
copy_add = input("copy_add:")

def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

mail = input("mail content:")
txt = open('output.txt')
#print(txt.read())
mail = mail + '\n' + txt.read()
print(mail)
txt.close()

msg = MIMEText(mail,'plain','utf-8')
msg['From'] = _format_addr('Python <%s>'%from_add)
msg['To'] = _format_addr(to_adds)
msg['Subject'] = Header("python:hello",'utf-8').encode()

server = smtplib.SMTP(host,25)
server.set_debuglevel(1)
server.login(from_add, passwd) 
server.sendmail(from_add,to_adds,msg.as_string())
server.quit()
#reply = server.getreply()
#for each in range(reply):
#    print(each)

