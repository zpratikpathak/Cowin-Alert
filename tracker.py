from sendemail import sendNotification
import time
from selenium import webdriver
import os
from dotenv import load_dotenv
load_dotenv()

options = webdriver.ChromeOptions()
options.add_argument("--disable-infobars")
# options.add_argument("--headless")
# Uncoment to enable Headless version
options.add_argument("--start-maximized")
options.add_argument(
    "user-agent='User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'"
)


def main():
    pincode = list(map(int, os.getenv("PINCODES").split(" ")))

    while True:
        browser = webdriver.Chrome(options=options)

        for pin in pincode:
            browser.get("https://www.cowin.gov.in/")
            browser.implicitly_wait(10)
            browser.find_element_by_id('mat-input-0').send_keys(pin)
            browser.implicitly_wait(10)
            time.sleep(10)
            browser.find_element_by_xpath(
                "//*[@id=\"mat-tab-content-0-0\"]/div/div[1]/div/div/button").click()
            time.sleep(10)
            browser.find_element_by_xpath(
                "//*[@id=\"Search-Vaccination-Center\"]/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div[3]/ul/li[2]/div/div[2]/label").click()
            time.sleep(10)
            try:
                browser.find_element_by_xpath(
                    "//*[@id=\"Search-Vaccination-Center\"]/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[5]/div[3]/div/div/div[1]/p")
                # No slots
                print("No shots available at Pincode:", pin)
            except:
                # sendemail()
                sendNotification()
        browser.quit()
        print("Vaccine Not Available. Checing Again in 1 hr.")
        time.sleep(3600)


if __name__ == "__main__":
    main()
