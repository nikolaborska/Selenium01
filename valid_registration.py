
from selenium import webdriver
from selenium.webdriver.common.by import By
import string
import random
import time

driver = webdriver.Chrome(executable_path="/Users/nikolaborska/Testing/chromedriver")
driver.implicitly_wait(10)
time.sleep(2)
url = "http://demostore.supersqa.com/my-account/"
email_filed_id = "reg_email"
psswd_field_id = "reg_password"
logout_btn_css = "li.woocommerce-MyAccount-navigation-link--customer-logout a"


# go to the url
driver.get(url)
email_filed = driver.find_element(By.ID, email_filed_id)

# generate random email
letters = string.ascii_lowercase
rand_string = "".join(random.choice(letters) for i in range(15))
random_email = rand_string + "@supersqa.com"

# type in the email field
email_filed.send_keys(random_email)

# find password field and enter passeword
password_field = driver.find_element(By.ID, psswd_field_id)
password_field.send_keys("mynewpassword!1")

time.sleep(2)
register_btn = driver.find_element(By.CSS_SELECTOR, 'button[value="Register"]')
register_btn.click()

try:
    logout_btn = driver.find_element(By.CSS_SELECTOR, logout_btn_css)
except:
    raise Exception("User not logged in after registering.")

if logout_btn.is_displayed():
    print("PASS.")
else:
    raise Exception("User not logged in after registering.")

