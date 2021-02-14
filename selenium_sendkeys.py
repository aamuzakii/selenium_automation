from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.techwithtim.net/")
# print (driver.title)

links = driver.find_elements_by_partial_link_text('Python')
# print(links)
for link in links:
    # link.click()
    # time.sleep(5)
    print(link.text)
    # driver.back()

# search = driver.find_element_by_id("menu-tutorials")
# print (search)
# search.send_keys("test")
# search.send_keys(Keys.RETURN)

# try:
#     main = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "menu-tutorials"))
#     )
#     bam = main.find_elements_by_tag_name("li")
#     # print(bam)
#     print(bam.text)

# except:
#     driver.quit()

# main = driver.find_element_by_id("main") ini sudah terganti dengan yang di block try 

# to make it wait 5 secods before quit 
time.sleep(5)

driver.quit