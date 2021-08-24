import yagmail
import os
from dotenv import load_dotenv
load_dotenv()

def sendNotification():
    yag = yagmail.SMTP(os.getenv("smtpEmail"), os.getenv("smtpPassword"))
    yag.send(os.getenv("receiverEmail"), "Vacination Slot Available", "Hey Slot is available now!!")