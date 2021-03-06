# https://www.pythonindo.com/cara-mengirim-email-menggunakan-python/

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr = input ("email pengirim: ")
password = input ("password: ")
toaddr = input ("email penerima: ")

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Percobaan Python"
body = "Email ini dikirim dengan menggunakan SMTP Python"

msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, password)
print("login sukses")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
print("email terkirim") 

server.quit()