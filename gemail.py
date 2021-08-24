import yagmail
import os
from dotenv import load_dotenv
load_dotenv()

yag = yagmail.SMTP(os.getenv("username"), os.getenv("password"))
yag.send(os.getenv("targets"), "An Email Alert", "The body of the email is here")