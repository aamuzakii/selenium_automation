from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.jobstreet.co.id/id/job-search/node-jobs-in-jakarta-raya/?salary=7000000&salary-max=2147483647")
# print (driver.title)

links = driver.find_elements_by_partial_link_text('Node')
# print(links)
for link in links:
    link.click()
    time.sleep(5)
    print(link.text)
    # driver.back()
    
