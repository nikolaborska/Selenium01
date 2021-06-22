from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install()) 
driver.get("https://www.python.org")

print(driver.title)
#--------- search bar -----------
search_bar = driver.find_element(By.ID, "id-search-field")
time.sleep(2)
search_bar.send_keys("getting started with python")
time.sleep(2)
search_bar.send_keys(Keys.RETURN)

#--------- try to print it out -----------
print(driver.current_url)
time.sleep(2)
driver.close()