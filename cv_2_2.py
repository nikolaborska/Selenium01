
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

url = 'file:///Users/nikolaborska/Desktop/cv_selenia/cv_2.html'

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
time.sleep(2)

expected_number_of_options = 4
all_checkboxes = driver.find_elements(By.NAME, 'age-group-checkbox')
assert len(all_checkboxes) == expected_number_of_options, "Number of checkboxes is not the expected"

for checkbox in all_checkboxes:
    checkbox.click()
    value = checkbox.get_attribute('value')
    if checkbox.is_selected():
        print(f"Checkbox with value '{value}' is selectable")
    else:
        raise Exception(f"Value '{value}' is not selectable")