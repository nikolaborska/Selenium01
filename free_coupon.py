
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


def add_1_item_to_cart():
    driver.find_element(By.CLASS_NAME, 'add_to_cart_button').click()
    wait.until(
        EC.text_to_be_present_in_element((By.XPATH, '//*[@id="site-header-cart"]/li[1]/a/span[2]'), '1 item')
    )
    time.sleep(2)

def click_cart_in_top_menu():
    driver.find_element(By.XPATH, '//*[@id="site-header-cart"]/li[1]/a').click()
    time.sleep(2)

def input_coupon_and_hit_enter(coupon_code):
    coupon_field = wait.until(EC.visibility_of_element_located((By.ID, 'coupon_code')))
    coupon_field.send_keys(coupon_code)
    coupon_field.send_keys(Keys.ENTER)
    time.sleep(2)

def verify_total_is_0():
    wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="post-7"]/div/div/div[2]/div/table/tbody/tr[3]/td/strong/span'), '$0.00'))
    time.sleep(2)

if __name__ == '__main__':

    coupon_code = 'SSQA100'

    driver = webdriver.Chrome(executable_path="/Users/nikolaborska/Testing/chromedriver")
    wait = WebDriverWait(driver, 10)

    driver.get('http://demostore.supersqa.com/')

    add_1_item_to_cart()
    click_cart_in_top_menu()
    input_coupon_and_hit_enter(coupon_code)
    verify_total_is_0()
    print("PASS")
    driver.quit()