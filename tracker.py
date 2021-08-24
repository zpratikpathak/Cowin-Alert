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


def main():
    pincode = list(map(int, os.getenv("PINCODES").split(" ")))
    semail = os.getenv("Email")

    browser.get("https://www.cowin.gov.in/")

    # for i in pincode:
    #     browser.find_element_by_id(“mat-input-0”).send_keys(i)


if __name__ == "__main__":
    main()
