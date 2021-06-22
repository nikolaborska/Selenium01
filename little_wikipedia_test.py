from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="/Users/nikolaborska/Desktop/cv_selenia/ChromeDriver-/chromedriver")

url = "https://www.wikipedia.org"
driver.get(url)
print(driver.title)
print(driver.current_url)
time.sleep(3)

cj = driver.find_element(By.ID, "js-link-box-cs")
time.sleep(2)
cj.click()

nav = driver.find_element(By.ID, "searchInput")
nav.send_keys("Řecko")
time.sleep(2)
nav.send_keys(Keys.RETURN)
time.sleep(2)

driver.back()
time.sleep(2)

nav1 = driver.find_element(By.ID, "searchInput")
nav1.send_keys("blablabla")
time.sleep(2)
nav1.send_keys(Keys.RETURN)
time.sleep(2)

driver.close()