# -*- coding: UTF-8 -*-  

import smtplib
from email.mime.text import MIMEText

msg = MIMEText("This is the mail from Python")

msg['Subject'] = "Python automail"
msg['From'] = "xxxx1@163.com"
msg['To'] = "xxxx@wipro.com"

usr = "xxxxx"
pwd = "xxxxx"

s = smtplib.SMTP_SSL("smtp.163.com", 465)
#s = smtplib.SMTP("smtp.163.com", 25)
s.login(usr, pwd)
s.send_message(msg)
print("The mail has been sent out!")
s.quit()
