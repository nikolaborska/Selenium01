
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

url = "file:///Users/nikolaborska/Desktop/cv_selenia/cv_2.html"
driver.get(url)

chck1 = driver.find_element(By.CSS_SELECTOR, "#checkboxes > div > input:nth-child(4")
time.sleep(2)
chck1.click()
#____________________________________________________________________________________
chck2 = driver.find_element(By.CSS_SELECTOR, "#checkboxes > div > input:nth-child(7)")
time.sleep(2)
chck2.click()

