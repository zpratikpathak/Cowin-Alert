from selenium import webdriver
import os
from dotenv import load_dotenv
load_dotenv()
import time

options = webdriver.ChromeOptions()
options.add_argument("--disable-infobars")
options.add_argument("--start-maximized")
options.add_argument(
    "user-agent='User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'"
)
browser = webdriver.Chrome(options=options)


def main():
    pincode = list(map(int, os.getenv("PINCODES").split(" ")))
    email = os.getenv("Email")
    
    browser.get("https://www.cowin.gov.in/")
    browser.implicitly_wait(10)
    browser.find_element_by_id('mat-input-0').send_keys("400009")
    browser.implicitly_wait(10)
    time.sleep(2)
    browser.find_element_by_xpath("//*[@id=\"mat-tab-content-0-0\"]/div/div[1]/div/div/button").click()   
    time.sleep(2)
    browser.find_element_by_xpath("//*[@id=\"Search-Vaccination-Center\"]/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div[3]/ul/li[2]/div/div[2]/label").click()
    time.sleep(2)
    try:
        browser.find_element_by_xpath("//*[@id=\"Search-Vaccination-Center\"]/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[5]/div[3]/div/div/div[1]/p")
        #No slots
        print("No shots")
    except:
        #sendemail()
        pass

    # for i in pincode:
    #     browser.find_element_by_id('mat-input-0').send_keys(i)


if __name__ == "__main__":
    main()
