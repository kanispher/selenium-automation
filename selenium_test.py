from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.chrome.service import Service
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

#PATH = "C:\ChromeDrivers\ChromeDriver.exe"

# For Windows
# service = Service(executable_path='C:\ChromeDrivers\ChromeDriver.exe')
# For MacOS
service = Service(executable_path='./chromedriver')

driver = webdriver.Chrome(service=service, options=options)

driver.get('https://www.agoda.com/zh-hk/?site_id=1891462&tag=be245458-7058-0e43-37aa-b2c5463966f9&device=c&network=g&adid=578244158158&rand=16490501845636509817&expid=&adpos=&aud=kwd-2230651387&gclid=CjwKCAjwsvujBhAXEiwA_UXnAMcOP5Fx4NEQtO1hRHHaQgYQ5rPNM4WZ7fp1PQCDP0OT_3FCboHl7RoCZoIQAvD_BwE&pslc=1')
#driver.implicitly_wait(10)
time.sleep(7)
try:
    close_ad = driver.find_element(By.CLASS_NAME, "ab-close-button")
    close_ad.click()
except:
    print("skipping")
time.sleep(2)
Find_location = driver.find_element(By.CLASS_NAME,"SearchBoxTextEditor")
time.sleep(2)
Find_location.click()
Find_location.send_keys("台東市")
time.sleep(3)
confirm_location = driver.find_element(By.CLASS_NAME,"AutocompleteList")
confirm_location.click()
enter_date1 = driver.find_element_by_xpath("div[@aria-label='Wed Jun 21 2023']")
enter_date1.click()
#time.sleep(5)
#enter_date2.click()


#//*[@id="SearchBoxContainer"]/div[1]/div/div[2]/div/div/div[6]/div/div/ul/li[1]
#data-objectid="94285"

