from selenium import webdriver
import os
from dotenv import load_dotenv
load_dotenv()

options = webdriver.ChromeOptions()
options.add_argument("--disable-infobars")
options.add_argument("--window-size=1200,800")
options.add_argument(
    "user-agent='User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'"
)
browser = webdriver.Chrome(options=options)
browser.get("google.com")


def main():
    pincode = list(map(int, os.getenv("PINCODES").split(" ")))
    semail = os.getenv("Email")


if __name__ == "__main__":
    main()
