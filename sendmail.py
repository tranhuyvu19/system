#!/bin/python
# coding=utf-8
from sender import Mail, Message
import time
import os

mail = Mail(
    "smtp.abc.com",
    port = 587,
    username = "user@abc.com",
    password = "password",
    use_tls = True,
    debug_level = True
)
url=''
today=time.strftime("%d_%m_%Y")
for i in os.listdir('folder'):
        if today in i:
                url= 'http://host:port/'+i

if url == '':
        exit()

msg = Message("subject %s " % today)
msg.fromaddr = ("user@abc.com")
msg.to = "user@abc.com"
msg.html = "<p> Dear <br>Today is %s<br><a href=%s>%s</a>" %(today,url,url)
msg.extra_headers = {}
msg.mail_options = []
msg.rcpt_options = []
# Send message
mail.send(msg)
