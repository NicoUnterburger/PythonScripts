#!/usr/bin/python

import smtplib
from email.mime.multipart import MIMEMultipart
msg = MIMEMultipart()

username = "user@name.de"
password = "password"
mailFrom = "mailfrom@provider.de"
mailTo = "mailto@provider.de"
server = smtplib.SMTP('mail.provider.de', 25)

#Next, log in to the server
server.login(username, password)

#Send the mail
msg['From'] = mailFrom
msg['To'] = mailTo
msg['Subject'] = 'Betreff'


server.sendmail(mailFrom, mailTo, msg.as_string())
