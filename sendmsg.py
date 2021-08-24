import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
load_dotenv()

smtp_ssl_host = os.getenv("smtp_ssl_host")
smtp_ssl_port = int(os.getenv("smtp_ssl_port"))
username = os.getenv("username")
password = os.getenv("password")
sender = username
# targets = ['HE@EXAMPLE.COM', 'SHE@EXAMPLE.COM']
targets = list(os.getenv("targets"))

msg = MIMEText('Slot Available')
msg['Subject'] = 'Vaccine Available'
msg['From'] = sender
msg['To'] = ', '.join(targets)

server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
server.login(username, password)
server.sendmail(sender, targets, msg.as_string())
server.quit()