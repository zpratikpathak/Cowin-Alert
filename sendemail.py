import yagmail
import os
from dotenv import load_dotenv
load_dotenv()

def sendNotification():
    yag = yagmail.SMTP(os.getenv("gmail"), os.getenv("gmailPassword"))
    yag.send(os.getenv("receiverEmail"), "Vacination Slot Available", "Hey Slot is available now!!\nHurry UP!!")