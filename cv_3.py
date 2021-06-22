from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
url = "file:///Users/nikolaborska/Desktop/cv_selenia/cv_3.html"
driver.get(url)

my_dropdown = driver.find_element('id', 'age-range-select')
dropdown_object = Select(my_dropdown)
time.sleep(2)
dropdown_object.select_by_index(3)
time.sleep(2)
dropdown_object.select_by_value('21-40')
all_options = dropdown_object.options
for option in all_options:

     print(option.text)