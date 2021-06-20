

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path="/Users/nikolaborska/Testing/chromedriver")

driver.get("http://demostore.supersqa.com")

# cart = driver.find_element(By.CSS_SELECTOR, "#site-header-cart")
# my_acct = driver.find_element(By.CSS_SELECTOR, "#site-navigation > div:nth-child(2) > ul > li.page_item.page-item-9 > a")
my_acct = driver.find_element(By.XPATH, '//*[@id="site-navigation"]/div[1]/ul/li[4]/a')
time.sleep(3)
my_acct.click()

# time.sleep(3)
# driver.quit()